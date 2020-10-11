# DRF-students-app
A DRF app built to manage students data through Rest APIs. This app has various features such as searching, sorting, and filtering data.

## Description
This app has the following endpoints:

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
    
- Searching student details through keywords: \
  Sample endpoint: `/student/?search=<search_keyword>`
  
- Sorting student details (alphabetically) through field names: \
  Sample endpoint: `/student/?ordering=last_name`
  
- Sorting student details (in reverse order) through field names: \
  Sample endpoint: `/student/?ordering=-last_name`
  
- Filter student details through field names: \
  Sample endpoint: `/student/?gender_female=true`
    
  
    
    
