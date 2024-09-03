import random
import matplotlib.pyplot as plt

def number(min_val, max_val):
    return random.randint(min_val, max_val)

def gauss_random(mean, stddev):
    return int(random.gauss(mean, stddev) + 0.5)

def simulate(target_bonus):
    iteration = 0
    iNormalHitBonus_values = []
    highest_values = []

    while True:
        iteration += 1
        iSkillBonus = max(-30, min(int(gauss_random(0, 5)), 30))
        if abs(iSkillBonus) <= 20:
            iNormalHitBonus = -2 * iSkillBonus + abs(number(-8, 8) + number(-8, 8)) + number(1, 4)
        else:
            iNormalHitBonus = -2 * iSkillBonus + number(1, 5)
        
        iNormalHitBonus_values.append(iNormalHitBonus)
        
        # Kaydedilecek en yüksek 20 değer ve iterasyon bilgilerini güncelle
        if iNormalHitBonus < target_bonus:
            if len(highest_values) < 20:
                highest_values.append((iNormalHitBonus, iteration))
                highest_values.sort(reverse=True, key=lambda x: x[0])
            elif iNormalHitBonus > highest_values[-1][0]:
                highest_values[-1] = (iNormalHitBonus, iteration)
                highest_values.sort(reverse=True, key=lambda x: x[0])
        
        if iNormalHitBonus >= target_bonus:
            return iteration, iNormalHitBonus_values, highest_values

# Simülasyonu çalıştır
target_bonus = 40
result, values, top_20_values = simulate(target_bonus)

# Sonuçları yazdır
print(f"{target_bonus} değerine {result} iterasyonda ulaşıldı.")
print("Hedef bonus öncesi en yüksek 20 değer ve iterasyonları:")
for value, iter_num in top_20_values:
    print(f"Değer: {value}, Iterasyon: {iter_num}")

# Grafiği oluştur
plt.figure(figsize=(12, 6))
plt.plot(values, label='iNormalHitBonus')
plt.axhline(y=target_bonus, color='r', linestyle='--', label=f'Target Bonus ({target_bonus})')

# Hedef bonus öncesi en yüksek 20 değeri işaretle
for value, iter_num in top_20_values:
    plt.scatter(iter_num, value, color='b', zorder=5)
    plt.text(iter_num, value, f'{value}', fontsize=9, ha='right', color='b')

# Kaçıncı iterasyonda hedef bonus değerine ulaşıldığını göstermek için işaretleyici ekleyelim
target_iteration = result - 1
plt.scatter(target_iteration, values[target_iteration], color='g', zorder=5)
plt.text(target_iteration, values[target_iteration], f'{target_iteration}', fontsize=12, ha='right', color='g')

plt.xlabel('Iteration')
plt.ylabel('iNormalHitBonus')
plt.title(f'ortalama değerlerinin iterasyonlar boyunca değişimi')
plt.legend()
plt.show()
