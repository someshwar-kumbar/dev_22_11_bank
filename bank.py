import sys
if len(sys.argv) != 3:
    print("Usage: python3 bank_balance.py <initial> <deposit>")
    sys.exit(1)
initial= float(sys.argv[1])
deposit= float(sys.argv[2])

updated_balance = initial+ deposit

print("Initial Balance:", initial)
print("Deposit Amount:", deposit)
print("Updated Balance:", updated_balance)
