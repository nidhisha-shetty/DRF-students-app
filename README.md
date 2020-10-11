# DRF-students-app
A DRF app built to manage students data through Rest APIs. This app has various features such as searching, sorting, and filtering data.

## Description
This app has three endpoints:

- CRUD operations \
    `POST`: Add details of a student. \
    Sample endpoint: `/student/`
    
    `PUT`: Update student details. \
    Sample endpoint: `/student/<id>/`

    `GET`: Get the list of students. \
    Sample endpoint: `/student/`

    `GET`: Get the student details. \
    Sample endpoint: `/student/<id>/`
    
    `DELETE`: Delete student details. \
    Sample endpoint: `/student/<id>/`
    
- Searching student details: \
  Sample endpoint: `/student/?search=<search_keyword>`
  
- Sorting student details (alphabetically): \
  Sample endpoint: `/student/?ordering=last_name`
  
- Sorting student details (in reverse order): \
  Sample endpoint: `/student/?ordering=-last_name`
  
- Filter student details: \
  Sample endpoint: `/student/?gender_female=true`
    
  
    
    
