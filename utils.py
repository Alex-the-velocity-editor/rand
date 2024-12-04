import json
from exceptions import MarkExistError

def get_courses() -> list[dict]:
    with open("courses.json", "r", encoding="utf-8") as w:
        file_courses_str = w.read()
    return json.loads(file_courses_str)

def get_tutors() -> list[dict]:
    with open("tutors.json", "r", encoding="utf-8") as w:
        file_tutors_str = w.read()
    return json.loads(file_tutors_str)

def get_tutor_courses() -> list[dict]:
    with open("tutor_courses.json", "r", encoding="utf-8") as w:
        file_tutor_courses_str = w.read()
    return json.loads(file_tutor_courses_str)



def get_tutor_photo(tutor_id:int) -> str:
    for tutor in get_tutors():
        if tutor["id"] == tutor_id:
            return tutor["photo"]

def put_tutor_mark(user_id:int, tutor_id:int,  mark_value:int):
    with open("tutors_marks.json", "r", encoding="utf-8") as f:
        file_tutor_marks_str = f.read()
        tutor_marks:list[dict] = json.loads(file_tutor_marks_str)
        _check_user_mark(tutor_marks=tutor_marks, user_id=user_id, tutor_id=tutor_id)
        tutor_marks.append({"user_id": user_id,"tutor_id": tutor_id, "mark": mark_value })
    json_new = json.dumps(tutor_marks, indent=4)
    with open("tutors_marks.json", "w") as outfile:
        outfile.write(json_new)

def _check_user_mark(tutor_marks:list[dict], user_id:int, tutor_id:int):
       for mark in tutor_marks:
            if mark["user_id"] == user_id and mark["tutor_id"] == tutor_id:
                raise MarkExistError
            

def get_tutors_marks_sum(top:int = 10):
    user_marks = []
    tutors = get_tutors()
    with open("tutors_marks.json", "r", encoding="utf-8") as f:
        file_tutor_marks_str = f.read()
    tutor_marks:list[dict] = json.loads(file_tutor_marks_str)  
    for tutor in tutors:
        mark_rating = {}
        for tutor_mark in tutor_marks:
            if tutor["id"] == tutor_mark["tutor_id"]:
                if mark_rating.get("id"):
                    mark_rating["sum"] += tutor_mark["mark"]
                else:
                    mark_rating["id"] = tutor["id"]
                    mark_rating["sum"] = tutor_mark["mark"]
        user_marks.append(mark_rating)
    return sorted(user_marks, key=lambda x: x['sum'],reverse=True)[:top]



"""
    {   "user_id": "12412",
        "tutor_id": 1,
        "mark": -1 
    },
"""