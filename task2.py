from typing import List, Dict
from dataclasses import dataclass

@dataclass
class PrintJob:
    id: str
    volume: float
    priority: int
    print_time: int

@dataclass
class PrinterConstraints:
    max_volume: float
    max_items: int


def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:
    # Перетворюємо в dataclass
    jobs = [PrintJob(**job) for job in print_jobs]
    printer = PrinterConstraints(**constraints)

    # 1. Сортуємо за пріоритетом (1 найважливіший)
    jobs.sort(key=lambda x: x.priority)

    print_order = []
    total_time = 0

    i = 0
    n = len(jobs)

    while i < n:
        current_volume = 0
        current_items = 0
        current_group = []
        group_times = []

        # 2. Формуємо групу
        while i < n:
            job = jobs[i]

            if (current_volume + job.volume <= printer.max_volume and
                current_items + 1 <= printer.max_items):

                current_group.append(job)
                group_times.append(job.print_time)
                current_volume += job.volume
                current_items += 1
                i += 1
            else:
                break

        # 3. Додаємо порядок
        for job in current_group:
            print_order.append(job.id)

        # 4. Час = максимум у групі
        if group_times:
            total_time += max(group_times)

    return {
        "print_order": print_order,
        "total_time": total_time
    }

if __name__ == "__main__":
    test_jobs = [
        {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 2, "print_time": 150}
    ]

    constraints = {
        "max_volume": 300,
        "max_items": 2
    }

    result = optimize_printing(test_jobs, constraints)
    print(result)