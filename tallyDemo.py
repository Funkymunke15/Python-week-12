# Davis Arita


from tally import Counter

tally = Counter()

tally.click()
tally.click()

result = tally.getValue()
print("Value:", result)

tally.click()
result = tally.getValue()
print("Value:", result)