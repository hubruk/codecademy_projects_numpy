import codecademylib
import numpy as np
from matplotlib import pyplot as plt

survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

total_ceballos = survey_responses.count('Ceballos')
print(total_ceballos)

percentage_ceballos = float(total_ceballos)/len(survey_responses)
print(percentage_ceballos)

binomial_ceballos = np.random.binomial(70, percentage_ceballos, size = 10000)
possible_surveys = binomial_ceballos/float(70)
print(binomial_ceballos,possible_surveys)
plt.hist(possible_surveys,range=(0,1), bins = 20)
plt.show()

ceballos_loss_surveys = np.mean(possible_surveys < 0.50)
print(ceballos_loss_surveys)

binomial_ceballos2 = np.random.binomial(70, percentage_ceballos, size = 7000)
large_survey = binomial_ceballos2/float(70)
ceballos_loss_new = np.mean(large_survey < 0.50)
print(ceballos_loss_new)
