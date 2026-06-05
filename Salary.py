def calculateovertimesalary(base_salary, totalhoursworked):
    overtime_rate = 50000

    if totalhoursworked > 40:
        overtime_hours = totalhoursworked - 40
        overtime_pay = overtime_hours * overtime_rate
        final_salary = base_salary + overtime_pay
    else:
        final_salary = base_salary

    return final_salary

result = calculateovertimesalary(5000000, 45)
print("Gaji akhir karyawan: Rp", result)
