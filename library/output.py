def formatOutput(data):
    course_title, term, time, location, instructor, ta_list, num_hw, num_exams = data
    print(
        f"""Course Title: {course_title}
Term: {term}
Instructor: {instructor}
Location: {location}
Time: {time}
Number of Homework Assignments: {num_hw}
Number of Exams: {num_exams}
Number of TAs for this course: {len(ta_list)}"""
    )
