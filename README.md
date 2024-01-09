# Examify - Streamlined GUI-Based Examination Management System

Examify is a simple and streamlined GUI-based Examination Management System implemented in Python using Tkinter.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Functional Requirements](#functional-requirements)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Examify is designed to provide a user-friendly interface for managing examination-related data. The system includes functionality for handling student information, exam details, subjects, results, attendance, and more.

## Features

- **Student Management:** Add, modify, and view student details.
- **Exam Management:** Handle exam-related data efficiently.
- **Subject Management:** Manage subjects and their details.
- **Result Management:** View and update student results.
- **Attendance Tracking:** Keep track of student attendance.
- **Branch Information:** Manage information related to different branches.

## Prerequisites

Ensure you have the following installed on your system:

- Python
- Tkinter library
- MySQL database (adjustments needed for different databases)

## Installation

1. Clone the repository.
   ```bash
   gh repo clone harshil-sanghvi/Examify-Streamlined-GUI-Based-Examination-Management-System
   cd Examify-Streamlined-GUI-Based-Examination-Management-System
   ```
2. Install dependencies.
3. Set up the database (modify the database configuration in the code).
   - Modify the database configuration in the code (e.g., MySQL username, password).
4. Run the application.
   ```bash
   python main.py
   ```

## Usage

- Navigate through the GUI to access different modules for managing examination-related data.
- Modify and update information as needed.
- Use the "Custom Query" feature for more advanced queries.

## Screenshots

### ER Diagram

The ER Diagram (Entity-Relationship Diagram) provides a visual representation of the entities and relationships within the Examify Examination Management System. It illustrates the structure of the database and the connections between different entities. The ER Diagram is crucial for understanding the data model and how various components relate to each other.

![ER Diagram](ER%20Diagram.png)

### Relational Model

The Relational Model represents the database schema in a tabular format, detailing the tables, attributes, and relationships. It serves as a blueprint for the actual database implementation. Each table corresponds to an entity, and the attributes define the properties of those entities. The relationships between tables are depicted, emphasizing the integrity and connectivity of the data.

![Relational Model](Relational%20Model.png)


## Functional Requirements

Read the functional requirements in [Functional Requirements.pdf](Functional%20Requirements.pdf).

## Contributing

Contributions are welcome! Fork the repository and create a pull request with your changes.

## License

This project is licensed under the [MIT License](LICENSE).
