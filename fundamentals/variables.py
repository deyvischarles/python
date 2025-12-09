name: str = "Deyvis"
age: int = 35
height: float = 1.70
balance: dict[str, float] = {"amount": 0.001055, "currency": "Satoshis"}
languages: list[str] = ["C", "C#", "Rust", "TypeScript", "Python"]
python_coding: bool = True

print("Name:", name)
print("Age:", age)
print(f"Height: {height:.2f} cm")

amount, currency = balance.values()
print(f"Balance: {amount:.3f} {currency}")

print("Languages:")
for i in languages :
    print(f"-> {i}")

print(f"Coding in Python: {'Yes' if python_coding else 'Not'}")

