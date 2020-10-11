# DRF-students-app
A DRF app built to manage students data through Rest APIs. This app has various features such as searching, sorting, and filtering data.

## Description
This app has three endpoints:

- CRUD operations
    Add details of a student. \
    Sample endpoint: POST (`/student/`)
    
    Update student details. \
    Sample endpoint: PUT (`/student/<id>/`)

    Get the list of students. \
    Sample endpoint: GET (`/student/`)

    Get the student details. \
    Sample endpoint: GET (`/student/<id>/`)
    
    Delete student details. \
    Sample endpoint: DELETE (`/student/<id>/`)
    
- Searching student details: \
  Sample endpoint: `/student/?search=<search_keyword>`
  
- Sorting student details (alphabetically): \
  Sample endpoint: `/student/?ordering=last_name`
  
- Sorting student details (in reverse order): \
  Sample endpoint: `/student/?ordering=-last_name`
  
- Filter student details: \
  Sample endpoint: `/student/?gender_female=true`
    
  
    
    
