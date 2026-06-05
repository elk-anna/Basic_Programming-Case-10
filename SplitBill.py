def calculatesplitbill(total_bill, number_of_people, tip_percentage):

    tip = total_bill * (tip_percentage / 100)

    total_with_tip = total_bill + tip
    amount_per_person = total_with_tip / number_of_people

    return amount_per_person

result = calculatesplitbill(300000, 4, 10)
print("Each person should pay: Rp ", result)
