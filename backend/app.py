from flask import Flask, request, jsonify
from flask_cors import CORS
from db import db, HydrationPlan

app = Flask(__name__)
CORS(app)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hydration.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/api/plans', methods=['GET'])
def get_plans():
    plans = HydrationPlan.query.all()
    return jsonify([plan.to_dict() for plan in plans])

@app.route('/api/plans', methods=['POST'])
def create_plan():
    data = request.get_json()
    plan = HydrationPlan(
        start_date=data['start_date'],
        end_date=data['end_date'],
        daily_goal=data['daily_goal'],
        schedule=data.get('schedule', [])
    )
    db.session.add(plan)
    db.session.commit()
    return jsonify(plan.to_dict()), 201

#by plan ID
@app.route('/api/plans/<int:plan_id>', methods=['GET'])
def get_plan(plan_id):
    plan = HydrationPlan.query.get(plan_id)
    return jsonify(plan.to_dict()) if plan else ('', 404)

@app.route('/api/plans/<int:plan_id>', methods=['PUT'])
def update_plan(plan_id):
    plan = HydrationPlan.query.get(plan_id)
    if not plan:
        return jsonify({'error': 'Plan not found'}), 404
    
    data = request.get_json()
    plan.start_date = data.get('start_date', plan.start_date)
    plan.end_date = data.get('end_date', plan.end_date)
    plan.daily_goal = data.get('daily_goal', plan.daily_goal)
    plan.schedule = data.get('schedule', plan.schedule)
    
    db.session.commit()
    return jsonify(plan.to_dict())

@app.route('/api/plans/<int:plan_id>', methods=['DELETE'])
def delete_plan(plan_id):
    plan = HydrationPlan.query.get(plan_id)
    if not plan:
        return jsonify({'error': 'Plan not found'}), 404
    
    db.session.delete(plan)
    db.session.commit()
    return jsonify({'message': 'Plan deleted'}), 200

##By date
@app.route('/api/plans/date/<date>', methods=['GET'])
def get_plans_by_date(date):
    plans = HydrationPlan.query.filter(
        (HydrationPlan.start_date <= date) & (HydrationPlan.end_date >= date)
    ).all()
    return jsonify([plan.to_dict() for plan in plans])

@app.route('/api/plans/date/<date>', methods=['PUT'])
def update_plan_by_id(date):
    plans = HydrationPlan.query.filter(
        (HydrationPlan.start_date <= date) & (HydrationPlan.end_date >= date)
    ).all()
    if not plans:
        return jsonify({'error': 'No plans found for the given date'}), 404
    
    data = request.get_json()
    for plan in plans:
        plan.start_date = data.get('start_date', plan.start_date)
        plan.end_date = data.get('end_date', plan.end_date)
        plan.daily_goal = data.get('daily_goal', plan.daily_goal)
        plan.schedule = data.get('schedule', plan.schedule)
        
    db.session.commit()
    return jsonify([plan.to_dict() for plan in plans])

@app.route('/api/plans/date/<date>', methods=['DELETE'])
def delete_plans_by_date(date):
    plans = HydrationPlan.query.filter(
        (HydrationPlan.start_date <= date) & (HydrationPlan.end_date >= date)
    ).all()
    if not plans:
        return jsonify({'error': 'No plans found for the given date'}), 404
    
    for plan in plans:
        db.session.delete(plan)
    db.session.commit()
    return jsonify({'message': f'Plans deleted for date: {date}'}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)
