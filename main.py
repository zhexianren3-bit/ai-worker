"""
AI 自律工作助手
自动完成任务，持续进化
"""
from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="AI Worker", version="1.0.0")

# 任务队列
tasks = []
# 工作记录
work_log = []

@app.get("/")
def root():
    return {"status": "工作中", "tasks": len(tasks)}

@app.post("/task")
def add_task(task: dict):
    """添加任务"""
    task["created_at"] = str(datetime.now())
    tasks.append(task)
    return {"success": True, "task_id": len(tasks)}

@app.get("/tasks")
def get_tasks():
    """获取任务列表"""
    return {"tasks": tasks, "count": len(tasks)}

@app.post("/complete")
def complete_task(task_id: int):
    """完成任务"""
    if 0 <= task_id < len(tasks):
        task = tasks[task_id]
        task["completed_at"] = str(datetime.now())
        work_log.append(task)
        return {"success": True}
    return {"success": False}

@app.get("/report")
def get_report():
    """工作报告"""
    return {
        "total_tasks": len(tasks),
        "completed": len(work_log),
        "pending": len(tasks) - len(work_log)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
