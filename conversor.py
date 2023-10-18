cel = int(input('Informe a temperatura em °C: '))
f = int(input('Informe a temperatura em °F: '))

# Convertendo °C para °F
conv1 = (9 * cel // 5) + 32
print(f'A temperatura em farenheit é {conv1}')

# Convertendo °F para °C
conv2 = (f - 32 // 5) * 5
print(f'A temperatura em farenheit é {conv2}')
