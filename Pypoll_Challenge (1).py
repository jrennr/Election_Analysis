#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -*- coding: UTF-8 -*-
"""PyPoll Challenge"""



# In[2]:


import csv
import os


# In[3]:


# Add our dependencies.# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")


# In[4]:


# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")


# In[5]:


# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")


# In[6]:


# Initialize a total vote counter.
total_votes = 0


# In[7]:


# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}


# In[8]:


# 1: Create a county list and county votes dictionary.
county_list = []
county_votes = {}


# In[9]:


# Track the winning candidate, vote count, and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# In[10]:


# 2: Track the largest county and county voter turnout.
largest_turnout = ""
largest_turnout_votes = 0


# In[11]:


# Read the csv and convert it into a list of dictionaries
with open("C:\\Users\\Columbia bootcamp\\Election_Analysis\\Starter_Code\\Resources\\election_results.csv") as election_data: 
   reader = csv.reader(election_data)


# In[17]:


# Read the header
#header = next(reader)


# In[18]:


# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Read the csv and convert it into a list of dictionaries
with open("C:\\Users\\Columbia bootcamp\\Election_Analysis\\Starter_Code\\Resources\\election_results.csv") as election_data:
    reader = csv.reader(election_data)

    # Now you can iterate through each row in the CSV file.
    for row in reader:
        candidate_name = row[0]  # Assuming candidate name is in the first column
        votes = int(row[1])  # Assuming votes are in the second column, and converting to an integer


# In[19]:


# Add to the total vote count
total_votes = total_votes + 1


# In[20]:


# Get the candidate name from each row.
candidate_name = row[2]


# In[21]:


# 3: Extract the county name from each row.
county_name = row[1]


# In[22]:


# If the candidate does not match any existing candidate, add it to
# the candidate list and begin tracking that candidate's voter count.
if candidate_name not in candidate_options:
candidate_options.append(candidate_name)
candidate_votes[candidate_name] = 0


# In[23]:


# Add a vote to that candidate's count
candidate_votes[candidate_name] += 1


# In[24]:


# 4a: Write an if statement that checks if the
# county does not match any existing county in the county list.
if county_name not in county_list:


# In[25]:


# 4b: Add the existing county to the list of counties.
county_list.append(county_name)



# In[26]:


# 4c: Begin tracking the county's vote count.
county_votes[county_name] = 0


# In[27]:


# 5: Add a vote to that county's vote count.
county_votes[county_name] += 1


# In[28]:


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:


# In[29]:


# Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n"
    )
    print(election_results, end="")
    txt_file.write(election_results)


# In[30]:


# 6a: Write a for loop to get the county from the county dictionary.
for county_name in county_votes:


# In[31]:


# 6b: Retrieve the county vote count.
county_count = county_votes[county_name]


# In[ ]:


# 6c: Calculate the percentage of votes for the county.
county_percentage = float(county_count) / float(total_votes) * 100


# In[ ]:


# 6d: Print the county results to the terminal.
county_results = f"{county_name}: {county_percentage:.1f}% ({county_count:,})\n"
print(county_results, end="")


# In[ ]:


# 6e: Save the county votes to a text file.
txt_file.write(county_results)


# In[ ]:


# 6f: Write an if statement to determine the winning county and get its vote count.
if county_count > largest_turnout_votes:
largest_turnout_votes = county_count
largest_turnout = county_name


# In[ ]:


# 7: Print the county with the largest turnout to the terminal.
largest_turnout_summary = (
    f"-------------------------\n"
    f"Largest County Turnout: {largest_turnout}\n"
    f"-------------------------\n"
)
print(largest_turnout_summary)


# In[ ]:


# 8: Save the county with the largest turnout to a text file.
txt_file.write(largest_turnout_summary)


# In[ ]:


# Save the final candidate vote count to the text file.
for candidate_name in candidate_votes:
# Retrieve vote count and percentage
votes = candidate_votes[candidate_name]
vote_percentage = float(votes) / float(total_votes) * 100
candidate_results = f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n"


# In[ ]:


# Print each candidate's voter count and percentage to the terminal.
print(candidate_results, end="")


# In[ ]:


# Save the candidate results to our text file.
txt_file.write(candidate_results)


# In[ ]:


# Determine winning vote count, winning percentage, and candidate.
if votes > winning_count and vote_percentage > winning_percentage:
winning_count = votes
winning_candidate = candidate_name
winning_percentage = vote_percentage


# In[ ]:


# Print the winning candidate (to terminal)
winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n"
    )


# In[ ]:


print(winning_candidate_summary)
# Save the winning candidate's name to the text file
txt_file.write(winning_candidate_summary)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




