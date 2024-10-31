from fastapi import FastAPI, HTTPException, Request
import sqlite3

app = FastAPI()

conn = sqlite3.connect('gym.db', check_same_thread=False)
cursor = conn.cursor()


@app.post("/user")
async def create_user_profile(request: Request):
    data = await request.json()
    cursor.execute(
        "INSERT INTO user_profile (name, age, height, weight) VALUES (?, ?, ?, ?)",
        (data["name"], data["age"], data["height"], data["weight"])
    )
    conn.commit()
    return {"message": "User profile created successfully"}

@app.get("/user")
def get_user_profile():
    cursor.execute("SELECT * FROM user_profile LIMIT 1")
    user = cursor.fetchone()
    if user:
        return {"id": user[0], "name": user[1], "age": user[2], "height": user[3], "weight": user[4]}
    raise HTTPException(status_code=404, detail="User profile not found")

@app.put("/user")
async def update_user_profile(request: Request):
    data = await request.json()
    cursor.execute(
        "UPDATE user_profile SET name=?, age=?, height=?, weight=? WHERE id=1",
        (data["name"], data["age"], data["height"], data["weight"])
    )
    conn.commit()
    return {"message": "User profile updated successfully"}

@app.delete("/user")
def delete_user_profile():
    cursor.execute("DELETE FROM user_profile WHERE id=1")
    conn.commit()
    return {"message": "User profile deleted successfully"}


@app.post("/workouts")
async def create_workout(request: Request):
    data = await request.json()
    cursor.execute(
        "INSERT INTO workouts (name, description) VALUES (?, ?)",
        (data["name"], data["description"])
    )
    conn.commit()
    return {"message": "Workout created successfully"}

@app.get("/workouts/{workout_id}")
def get_workout(workout_id: int):
    cursor.execute("SELECT * FROM workouts WHERE id=?", (workout_id,))
    workout = cursor.fetchone()
    if workout:
        return {"id": workout[0], "name": workout[1], "description": workout[2]}
    raise HTTPException(status_code=404, detail="Workout not found")

@app.put("/workouts/{workout_id}")
async def update_workout(workout_id: int, request: Request):
    data = await request.json()
    cursor.execute(
        "UPDATE workouts SET name=?, description=? WHERE id=?",
        (data["name"], data["description"], workout_id)
    )
    conn.commit()
    return {"message": "Workout updated successfully"}

@app.delete("/workouts/{workout_id}")
def delete_workout(workout_id: int):
    cursor.execute("DELETE FROM workouts WHERE id=?", (workout_id,))
    conn.commit()
    return {"message": "Workout deleted successfully"}

@app.get("/workouts")
def list_workouts():
    cursor.execute("SELECT * FROM workouts")
    workouts = cursor.fetchall()
    return workouts

@app.post("/exercises")
async def create_exercise(request: Request):
    data = await request.json()
    cursor.execute(
        "INSERT INTO exercises (workout_id, name, sets, reps, weight) VALUES (?, ?, ?, ?, ?)",
        (data["workout_id"], data["name"], data["sets"], data["reps"], data["weight"])
    )
    conn.commit()
    return {"message": "Exercise created successfully"}

@app.get("/exercises/{exercise_id}")
def get_exercise(exercise_id: int):
    cursor.execute("SELECT * FROM exercises WHERE id=?", (exercise_id,))
    exercise = cursor.fetchone()
    if exercise:
        return {"id": exercise[0], "workout_id": exercise[1], "name": exercise[2], "sets": exercise[3], "reps": exercise[4], "weight": exercise[5]}
    raise HTTPException(status_code=404, detail="Exercise not found")

@app.put("/exercises/{exercise_id}")
async def update_exercise(exercise_id: int, request: Request):
    data = await request.json()
    cursor.execute(
        "UPDATE exercises SET name=?, sets=?, reps=?, weight=? WHERE id=?",
        (data["name"], data["sets"], data["reps"], data["weight"], exercise_id)
    )
    conn.commit()
    return {"message": "Exercise updated successfully"}

@app.delete("/exercises/{exercise_id}")
def delete_exercise(exercise_id: int):
    cursor.execute("DELETE FROM exercises WHERE id=?", (exercise_id,))
    conn.commit()
    return {"message": "Exercise deleted successfully"}

@app.get("/exercises")
def list_exercises():
    cursor.execute("SELECT * FROM exercises")
    exercises = cursor.fetchall()
    return exercises

@app.post("/goals")
async def create_goal(request: Request):
    data = await request.json()
    cursor.execute(
        "INSERT INTO goals (goal, target_date) VALUES (?, ?)",
        (data["goal"], data["target_date"])
    )
    conn.commit()
    return {"message": "Goal created successfully"}

@app.get("/goals/{goal_id}")
def get_goal(goal_id: int):
    cursor.execute("SELECT * FROM goals WHERE id=?", (goal_id,))
    goal = cursor.fetchone()
    if goal:
        return {"id": goal[0], "goal": goal[1], "target_date": goal[2]}
    raise HTTPException(status_code=404, detail="Goal not found")

@app.delete("/goals/{goal_id}")
def delete_goal(goal_id: int):
    cursor.execute("DELETE FROM goals WHERE id=?", (goal_id,))
    conn.commit()
    return {"message": "Goal deleted successfully"}

@app.post("/progress")
async def track_progress(request: Request):
    data = await request.json()
    cursor.execute(
        "INSERT INTO progress (date, workout_id, notes) VALUES (?, ?, ?)",
        (data["date"], data["workout_id"], data["notes"])
    )
    conn.commit()
    return {"message": "Progress tracked successfully"}

@app.get("/progress/{progress_id}")
def get_progress(progress_id: int):
    cursor.execute("SELECT * FROM progress WHERE id=?", (progress_id,))
    progress = cursor.fetchone()
    if progress:
        return {"id": progress[0], "date": progress[1], "workout_id": progress[2], "notes": progress[3]}
    raise HTTPException(status_code=404, detail="Progress not found")

@app.get("/progress")
def list_progress():
    cursor.execute("SELECT * FROM progress")
    progress = cursor.fetchall()
    return progress
