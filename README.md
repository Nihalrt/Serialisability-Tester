# Serialisability Tester

This project offers a Python-based utility for evaluating the serialisability of execution schedules within database systems. It comprises two essential components: `schedule.py` and `serialisabilitytester.py`. This README provides an in-depth understanding of these components and their usage.

## `schedule.py`

`schedule.py` serves as the foundation for this project, providing classes and structures to model and manipulate execution schedules and database operations. Key elements include:

- `IOOperation`: This class represents an individual read or write operation on a database. It encapsulates attributes such as transaction ID, operation type (read or write), and the specific database element being accessed.

- `Schedule`: This class defines an ordered collection of `IOOperations`. It captures the chronological sequence of read and write operations that occur within a database execution schedule.

- `SimpleSchedule`: This class represents an ordered list of transaction IDs (integers). It signifies the order in which transactions are executed in a serial fashion.

These components provide the necessary data structures for defining and analyzing execution schedules.

## `serialisabilitytester.py`

`serialisabilitytester.py` implements critical functionality for assessing the serialisability of execution schedules. Key features include:

- `to_serial(schedule)`: This method accepts a `Schedule` as input and returns the lexicographically smallest serial `SimpleSchedule` that is conflict-equivalent to the provided schedule. If the input schedule is not conflict-serialisable, it returns `None`.

- `conflicts`: This script identifies conflicts between transactions based on read and write operations on the same database element. It then employs a topological sort to determine a serial order of execution.

## How to Use

To effectively utilize this project, follow these steps:

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/your-username/serialisability-tester.git
