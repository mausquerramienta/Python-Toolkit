# Day 2 Project
# Ask for name
# Ask for sales amount
# Calculate 13% commission

print("-" * 40)
print("💰 COMMISSION CALCULATOR 💰")
print("-" * 40)

name = input("👤 Enter your name: ")
sales = float(input("💵 Enter total sales amount: $"))
commission = round(sales * 0.13, 2)

print("-" * 40)
print(f"✅ Hello {name}!")
print(f"📊 Total Sales: ${sales:,.2f}")
print(f"🏆 Earned Commission (13%): ${commission:,.2f}")
print("-" * 40)
