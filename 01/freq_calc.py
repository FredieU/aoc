#! /usr/bin/python3

import csv, time

# Initialise empty list to store frequency changes as integers
freq_list = []

with open('freq_changes.csv') as csv_file:
  freq_changes = csv.reader(csv_file)

  # Loop through rows in csv and append values to frequency list
  for row in freq_changes:
    freq_list.append(int(row[0]))

# Starting frequency
current_freq = 0
# List to store previous frequencies to find first duplicate
current_freq_list = []

dup_freq = True
run = 0
while dup_freq:
  run += 1
  print(f'Run: {run}')

  for freq in freq_list:
    current_freq += freq
    print(f'Current Frequency: {current_freq}')
    time.sleep(1)

    if current_freq in current_freq_list:
      print(f'DUPLICATE FREQUENCY: {current_freq}')
      dup_freq = False
      break
    else:
      current_freq_list.append(current_freq)