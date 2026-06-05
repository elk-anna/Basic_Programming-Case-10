def calculateloyaltypoints(total_transaction, member_status):
    if member_status == False:
        return 0

    points = total_transaction // 20000
    return points

print(calculateloyaltypoints(150000, True))
print(calculateloyaltypoints(150000, False))
