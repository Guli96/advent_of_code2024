def is_safe(report):
    if report[0] < report[1]: #ascending
        return all(second - first in range(1,4) for first, second in zip(report, report[1:]) )
    elif report[0] > report[1]: #descending
        return all(first - second in range(1, 4) for first, second in zip(report, report[1:]))
    else:
        return False

def is_safe_with_tolerance(report: list):
    safe = False
    for i in range(len(report)):
        report_tolerance = report.copy()
        report_tolerance.pop(i)
        if is_safe(report_tolerance):
            safe = True
    return safe

def part1(reports):
    safe_reports = 0
    for report in reports:
        if is_safe([int(x) for x in report.split(' ')]):
            safe_reports += 1
    return safe_reports

def part2(reports):
    safe_reports = 0
    for report in reports:
        if is_safe_with_tolerance([int(x) for x in report.split(' ')]):
            safe_reports += 1
    return safe_reports