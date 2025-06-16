from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class HydrationPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.String(10), nullable=False)  # Store as string
    end_date = db.Column(db.String(10), nullable=False)    # Store as string
    daily_goal = db.Column(db.Integer, nullable=False)
    schedule = db.Column(db.JSON, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'daily_goal': self.daily_goal,
            'schedule': self.schedule
        }
