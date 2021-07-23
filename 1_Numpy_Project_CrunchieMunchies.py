import codecademylib
import numpy as np

calorie_stats = np.genfromtxt('cereal.csv', delimiter = ',')
print(calorie_stats)

average_calories = np.mean(calorie_stats)
print(average_calories)

calorie_stats_sorted = np.sort(calorie_stats)
print(calorie_stats_sorted)

median_calories = np.median(calorie_stats)
print(median_calories)

nth_percentile = np.percentile(calorie_stats, 3.5)
print(nth_percentile)

more_calories = np.mean(calorie_stats > 60)
print(more_calories*100)

calorie_std = np.std(calorie_stats)
print(calorie_std)

# Median in those data is 110. Average amount of cereal calories is 106.9, with standard deviation about 19. 96% of cereals have more than 63.2 calories. 
#YummyCorps the company for whom we did this calculation could communicate in their marketing campaigns the diffrence in amount of calories per serving compared to competitors.
