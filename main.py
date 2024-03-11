import concurrent.futures
import random as rd
import time


class Trapezoid:
    def __init__(self, parameters=None):
        if parameters is None:
            self.a = 0
            self.b = 0
            self.h = 0
        self.a = parameters[0]
        self.b = parameters[1]
        self.h = parameters[2]

    def __str__(self):
        return f'Isosceles trapezoid large base -> {self.b}, small base -> {self.a}, height ->{self.h}'

    def area(self):
        return (self.a + self.b) / 2 * self.h

    def __lt__(self, other):
        if isinstance(other, Trapezoid):
            return self.area() < other.area()

        return False

    def __eq__(self, other):
        if isinstance(other, Trapezoid):
            return self.area() == other.area()

        return False

    def __ge__(self, other):
        if isinstance(other, Trapezoid):
            return not self.__lt__(other)

        return False

    def __add__(self, other):
        if isinstance(other, Trapezoid):
            return self.area() + other.area()

        return -1

    def __sub__(self, other):
        if isinstance(other, Trapezoid):
            return self.area() - other.area()

        return -1

    def __mod__(self, other):
        if isinstance(other, Trapezoid):
            return self.area() % other.area()

        return -1


class Rectangle(Trapezoid):
    def __init__(self, parameters=None):
        super().__init__((parameters[0], parameters[1], 0))

    def area(self):
        return self.a * self.b

    def __str__(self):
        return f'Rectangles height -> {self.a}, width -> {self.b}'


class Square(Rectangle):
    def __init__(self, parameters=None):
        super().__init__((parameters[0], 0, 0))

    def area(self):
        return self.a**2

    def __str__(self):
        return f'Squares side -> {self.a}'


def calc_figures_areas(figures_array):
    for figure in figures_array:
        figure.area()


def generate_and_calculate(array_cnt):
    figures_array = generate_array(array_cnt)
    calc_figures_areas(figures_array)


def run_regular(figure_cnt):
    start = time.perf_counter()

    generate_and_calculate(figure_cnt)

    finish = time.perf_counter()

    print('Regular finished in: ', round(finish - start, 2), ' second(s).')


def run_threads(figure_cnt, thread_cnt):
    start = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor(max_workers=thread_cnt) as exe:
        for _ in range(thread_cnt):
            exe.submit(generate_and_calculate, figure_cnt // thread_cnt)

    finish = time.perf_counter()
    print('Threads finished in: ', round(finish - start, 2), ' second(s).')


def run_processes(figure_cnt, process_cnt):
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor(max_workers=process_cnt) as exe:
        for _ in range(process_cnt):
            exe.submit(generate_and_calculate, figure_cnt // process_cnt)

    finish = time.perf_counter()
    print('Processes finished in: ', round(finish - start, 2), ' second(s).')


def run_mixed(figure_cnt, thread_cnt, process_cnt):
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor(max_workers=process_cnt):
        for _ in range(process_cnt):
            with concurrent.futures.ThreadPoolExecutor(max_workers=thread_cnt) as exe_thread:
                for _ in range(thread_cnt):
                    exe_thread.submit(generate_and_calculate, figure_cnt // thread_cnt // process_cnt)

    finish = time.perf_counter()
    print('Mixed finished in: ', round(finish - start, 2), ' second(s).')


def generate_array(size=100000):
    trapezoids = [
        Trapezoid((rd.randint(1, 200), rd.randint(1, 200), rd.randint(1, 200))) for _ in range(size)
    ]
    rectangles = [
        Rectangle((rd.randint(1, 200), rd.randint(1, 200))) for _ in range(size)
    ]
    squares = [
        Square((rd.randint(1, 200),)) for _ in range(size)
    ]

    return trapezoids + rectangles + squares


def test_overridden_methods():
    print('2 Trapezoids: ')
    t1 = Trapezoid((100, 100, 50))
    t2 = Trapezoid((150, 200, 70))
    print(t1.area(), t2.area())
    print(t1 + t2)
    print(t2 - t1)
    print(t1 % t2)

    print('--------------------------------')
    print('2 Rectangles')
    r1 = Rectangle((100, 100))
    r2 = Rectangle((150, 200))
    print(r1.area(), r2.area())
    print(r1 + r2)
    print(r2 - r1)
    print(r1 % r2)

    print('--------------------------------')
    print('Mixed')
    t3 = Trapezoid((100, 100, 50))
    s1 = Square((50,))
    print(t3.area(), s1.area())
    print(s1 + t3)
    print(t3 - s1)
    print(s1 % t3)


def test_calculations(figure_cnt=100000):
    print(f'Test with {figure_cnt} figures:')
    run_regular(figure_cnt)
    run_threads(figure_cnt, 200)
    run_processes(figure_cnt, 20)
    run_mixed(figure_cnt, 25, 4)


def main():
    # test_overridden_methods()
    test_calculations()


if __name__ == "__main__":
    main()
