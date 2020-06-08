try:
    employee_file_handle = open("employee", "a+")
    print(employee_file_handle.readable())
    print(employee_file_handle.writable())
    #print(employee_file_handle.read())
    #print((employee_file_handle.readline()))
    # print(employee_file_handle.readlines())
    employee_file_handle.write("\nSG|46|2365|648525")
    employee_file_handle.seek(0)
    print(employee_file_handle.tell())
    for employee in employee_file_handle.readlines():
        employee=employee.replace("\n","")
        print(employee)
        for emp_detail in employee.split("|"):
            print(emp_detail)
       # print(employee.split("|"))
    print(employee_file_handle.tell())
except Exception as e:
    print(e)
finally:
    employee_file_handle.close()
