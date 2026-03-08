tasks = []
next_id = 1


def add_task(title, description, task_type, start_date, end_date, status):
    global next_id

    task = {
        "id": next_id,
        "title": title,
        "description": description,
        "type": task_type,
        "start_date": start_date,
        "end_date": end_date,
        "status": status
    }

    tasks.append(task)
    next_id += 1

    return task


def get_tasks(status=None, task_type=None):
    result = tasks

    if status:
        result = [t for t in result if t["status"] == status]

    if task_type:
        result = [t for t in result if t["type"] == task_type]

    return result


def update_task(task_id, **kwargs):
    for task in tasks:
        if task["id"] == task_id:
            for key, value in kwargs.items():
                if key in task:
                    task[key] = value
            return task

    return None


def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return True


if __name__ == "__main__":
    add_task("הגשת דוח", "להגיש דוח חודשי", "עבודה", "2026-02-20", "2026-02-25", "פתוח")
    add_task("קניות", "לקנות חלב ולחם", "אישי", "2026-02-19", "2026-02-19", "פתוח")

    print("כל המשימות:")
    print(get_tasks())

    update_task(1, status="בוצע")

    print("\nמשימות שבוצעו:")
    print(get_tasks(status="בוצע"))