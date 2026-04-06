from google.cloud import firestore
from datetime import datetime
import uuid

db = firestore.Client()

def create_task(title: str, priority: str = "medium", due_date: str = "") -> dict:
    """Creates a new task and saves it to the database.
    
    Args:
        title: The task title or description.
        priority: Task priority - low, medium, or high.
        due_date: Optional due date like 'tomorrow' or '2025-04-10'.
    
    Returns:
        A dict with task_id and confirmation message.
    """
    doc_id = str(uuid.uuid4())[:8]
    db.collection("tasks").document(doc_id).set({
        "id": doc_id, "title": title, "priority": priority,
        "due_date": due_date, "status": "pending",
        "created_at": datetime.utcnow().isoformat()
    })
    return {"task_id": doc_id, "message": f"Task created: '{title}'", "priority": priority}


def list_tasks(status: str = "pending") -> dict:
    """Lists existing tasks from the database.
    
    Args:
        status: Filter by status - pending or completed.
    
    Returns:
        A dict containing list of tasks.
    """
    tasks = [t.to_dict() for t in db.collection("tasks").where("status", "==", status).stream()]
    return {"count": len(tasks), "tasks": tasks}


def save_note(title: str, content: str, tags: str = "") -> dict:
    """Saves a note or piece of information to the database.
    
    Args:
        title: Note title.
        content: The full note content.
        tags: Comma-separated tags like 'work,interview,prep'.
    
    Returns:
        A dict with note_id and confirmation message.
    """
    doc_id = str(uuid.uuid4())[:8]
    tag_list = [t.strip() for t in tags.split(",") if t.strip()]
    db.collection("notes").document(doc_id).set({
        "id": doc_id, "title": title, "content": content,
        "tags": tag_list, "created_at": datetime.utcnow().isoformat()
    })
    return {"note_id": doc_id, "message": f"Note saved: '{title}'"}


def get_notes(tag: str = "") -> dict:
    """Retrieves saved notes from the database, optionally filtered by tag.
    
    Args:
        tag: Optional tag to filter notes by.
    
    Returns:
        A dict containing list of notes.
    """
    ref = db.collection("notes")
    if tag:
        ref = ref.where("tags", "array_contains", tag)
    notes = [n.to_dict() for n in ref.stream()]
    return {"count": len(notes), "notes": notes}


def schedule_event(title: str, date: str, duration_hours: int = 1, description: str = "") -> dict:
    """Schedules a calendar event or time block.
    
    Args:
        title: Event title.
        date: Date and time like 'tomorrow 10am' or '2025-04-10 10:00'.
        duration_hours: How long the event lasts in hours.
        description: Optional event description.
    
    Returns:
        A dict with event_id and confirmation message.
    """
    doc_id = str(uuid.uuid4())[:8]
    db.collection("events").document(doc_id).set({
        "id": doc_id, "title": title, "date": date,
        "duration_hours": duration_hours, "description": description,
        "created_at": datetime.utcnow().isoformat()
    })
    return {"event_id": doc_id, "message": f"Event scheduled: '{title}' on {date} for {duration_hours}h"}