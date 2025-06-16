# 💧 Water Hydration Tracker
A full-stack web application that allows users to schedule and track their daily water intake. Users can plan how many glasses of water they want per day, set reminders, and manage hydration plans by date.

---

## 🚀 Features
- Create hydration plans with:
  - Start and end date
  - Daily water goal (in glasses)
  - Custom time schedules for each glass
- View all hydration plans or filter by date
- Edit or delete existing plans
- Receive real-time hydration notifications (browser-based)
- Clean and responsive UI built using Vue.js

---
- **Frontend**: Vue.js (uses CDN)
- **Backend**: Flask API with SQLite
- **Flow**:
  1. Frontend sends hydration plan CRUD requests to Flask
  2. Flask handles DB operations and returns JSON
  3. Frontend schedules local timers for reminders

---
### Entity: `Plan`
| Field         | Type    | Description                   |
|---------------|---------|-------------------------------|
| id            | Integer | Unique ID (auto-increment)    |
| start_date    | String  | Format: YYYY-MM-DD            |
| end_date      | String  | Format: YYYY-MM-DD            |
| daily_goal    | Integer | Glasses per day               |
| schedule      | JSON    | Array of times e.g. `["09:00", "13:00"]` |

---

### 🧪 API Spec

| Method | Endpoint                      | Description             |
|--------|-------------------------------|-------------------------|
| GET    | `/api/plans`                  | Fetch all plans         |
| GET    | `/api/plans/date/<YYYY-MM-DD>`| Fetch plans for a date  |
| POST   | `/api/plans`                  | Create a new plan       |
| PUT    | `/api/plans/<id>`             | Update an existing plan |
| DELETE | `/api/plans/<id>`             | Delete a plan           |

---

## 📁 Codebase Structure

```
hydration-tracker/
│
├── backend/
│   ├── app.py                 # Flask API with CRUD routes
│   ├── db.py              # Plan model with SQLite DB
│   └── requirements.txt       # Python dependencies
│
├── frontend/
│   └── index.html             # Vue.js frontend (via CDN)
│
├── design/
│   ├── HLD.png                # High-Level Design diagram
│   └── LLD.png                # Low-Level Design diagram
│
└── README.md                  # You’re here
