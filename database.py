import os

def create_course_folder(course_name, sections, students_info):
    base_path = os.path.join(os.getcwd(), course_name)
    os.makedirs(base_path, exist_ok=True)
    print(f"Main folder created: {base_path}")

    # Create subfolders for each section
    for section_name in sections.items():
        section_path = os.path.join(base_path, section_name)
        os.makedirs(section_path, exist_ok=True)
        print(f"Subfolder created: {section_path}")

# Define the course name
course_name = "Btech"

# Define sections and their students
sections = {
    "Section A",
    "Section B",
}

# Call the function
create_course_folder(course_name, sections, sections)
