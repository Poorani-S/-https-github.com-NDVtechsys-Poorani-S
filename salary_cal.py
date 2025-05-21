CTC=float(input("Enter Total Cost To Company"))
Bonus=float(input("Enter bonus in percentage"))
Total_Bonus= CTC*Bonus
Total_income = CTC+Total_Bonus
def calculate_old_regime_tax(taxable_income):
    tax = 0
    if taxable_income <= 250000:
        tax = 0
    elif taxable_income <= 500000:
        tax = (taxable_income - 250000) * 0.05
    elif taxable_income <= 1000000:
        tax = 250000 * 0.05 + (taxable_income - 500000) * 0.2
    else:
        tax = 250000 * 0.05 + 500000 * 0.2 + (taxable_income - 1000000) * 0.3
    return tax + tax * 0.04  # Adding 4% cess


def calculate_new_regime_tax(taxable_income):
    tax = 0
    if taxable_income <= 300000:
        tax = 0
    elif taxable_income <= 600000:
        tax = (taxable_income - 300000) * 0.05
    elif taxable_income <= 900000:
        tax = 300000 * 0.05 + (taxable_income - 600000) * 0.10
    elif taxable_income <= 1200000:
        tax = 300000 * 0.05 + 300000 * 0.10 + (taxable_income - 900000) * 0.15
    elif taxable_income <= 1500000:
        tax = 300000 * 0.05 + 300000 * 0.10 + 300000 * 0.15 + (taxable_income - 1200000) * 0.20
    else:
        tax = (300000 * 0.05 + 300000 * 0.10 + 300000 * 0.15 + 
               300000 * 0.20 + (taxable_income - 1500000) * 0.30)
    return tax + tax * 0.04 
Bonus_amount = CTC * Bonus
Total_income = CTC + Bonus_amount
standard_deduction = 50000
hra_exemption = 100000   
section_80C = 150000
old_taxable_income = Total_income - standard_deduction - hra_exemption - section_80C
new_taxable_income = Total_income - 50000 
old_tax = calculate_old_regime_tax(old_taxable_income)
new_tax = calculate_new_regime_tax(new_taxable_income)
comparison = new_taxable_income-old_taxable_income

print("comparison of two regimes:",comparison)
print("\n--- Tax Comparison ---")
print(f"Total Income (CTC + Bonus): ₹{Total_income:,.2f}")
print(f"Taxable Income (Old Regime): ₹{old_taxable_income:,.2f}")
print(f"Taxable Income (New Regime): ₹{new_taxable_income:,.2f}")
print(f"Tax Payable under Old Regime: ₹{old_tax:,.2f}")
print(f"Tax Payable under New Regime: ₹{new_tax:,.2f}")

if old_tax < new_tax:
    print("✅ Choose the OLD tax regime (less tax payable).")
elif new_tax < old_tax:
    print("✅ Choose the NEW tax regime (less tax payable).")
else:
    print("Both regimes result in the same tax.")
