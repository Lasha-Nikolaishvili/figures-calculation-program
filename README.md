
---

# Figures Calculation Program

The Figures Calculation Program is a Python application designed to demonstrate the performance impact of different concurrency strategies (regular, threading, multiprocessing, and mixed) on calculating areas of geometric figures. The program defines three types of figures: Trapezoid, Rectangle, and Square, each inheriting from the previous one, showcasing method overriding and inheritance in object-oriented programming.

## Features

- **Geometric Figures**: Trapezoids, Rectangles, and Squares with randomly generated parameters.
- **Concurrency Strategies**: Test the program's performance using different concurrency approaches, such as regular execution, threading, multiprocessing, and a mixed approach combining threads and processes.
- **Overridden Methods**: Illustrate the use of overridden methods for arithmetic operations (`+`, `-`, `%`) for Trapezoid, Rectangle, and Square instances.
- **Execution Time Measurement**: Measure the execution time for each concurrency strategy to assess performance.

## Prerequisites

Before running the Figures Calculation Program, ensure you have the following installed:

- Python 3.6 or higher

## Installation

1. Clone or download this repository to your local machine:

```bash
git clone <repository-url>
```

2. Navigate to the program's directory:

```bash
cd figures-calculation-program
```

3. Run the program:

```bash
python main.py
```

## Usage

The program contains various functions that demonstrate different aspects of the implemented classes and concurrency strategies:

- `test_overridden_methods()`: Test arithmetic operations on instances of Trapezoid, Rectangle, and Square classes.
- `test_calculations(figure_cnt)`: Measure the execution time for regular, threading, multiprocessing, and mixed concurrency strategies with a specified number of generated figures (default is 100,000).

To execute the tests, uncomment the desired function call in the `main()` function.

## Configuration

Adjust the parameters in the `test_calculations()` function based on your system's capabilities and the desired workload. You can change the number of figures (`figure_cnt`) and adjust the thread and process counts for the mixed concurrency strategy.

## Trials

1. parameters: | 100 threads | 6 processes | 20 threads in 5 processes
 * input size: 100 000 figures.
   * Regular finished in:  1.76  second(s).
   * Threads finished in:  1.42  second(s).
   * Processes finished in:  1.36  second(s).
   * Mixed finished in:  1.43  second(s).
 * input size: 500 000 figures.
   * Regular finished in:  9.43  second(s).
   * Threads finished in:  8.42  second(s).
   * Processes finished in:  5.24  second(s).
   * Mixed finished in:  7.78  second(s).
 * input size: 1 000 000 figures.
  * Regular finished in:  18.2  second(s).
  * Threads finished in:  17.2  second(s). 
  * Processes finished in:  10.14  second(s).
  * Mixed finished in:  17.18  second(s).
2. parameters: | 100 threads | 6 processes | 20 threads in 5 processes
 * input size: 100 000 figures.
  * Regular finished in:  1.77  second(s).
  * Threads finished in:  1.4  second(s).
  * Processes finished in:  2.44  second(s).
  * Mixed finished in:  1.44  second(s).
 * input size: 500 000 figures.
  * Regular finished in:  9.47  second(s).
  * Threads finished in:  7.95  second(s).
  * Processes finished in:  5.83  second(s).
  * Mixed finished in:  8.04  second(s).
 * input size: 1 000 000 figures.
  * Regular finished in:  19.16  second(s).
  * Threads finished in:  16.83  second(s).
  * Processes finished in:  10.3  second(s).
  * Mixed finished in:  17.59  second(s).