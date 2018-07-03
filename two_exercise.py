ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

# Write a python expression that gets the email address of Ramit.
ramit_email = ramit['email']
print ramit_email

# Write a python expression that gets the first of Ramit's interests.
ramit_first_interest = ramit['interests'][0]
print ramit_first_interest

# Write a python expression that gets the email address of Jasmine.
jasmine_email = ramit['friends'][0]['email']

print jasmine_email

# Write a python expression that gets the second of Jan's two interest.
jan_second_interest = ramit['friends'][1]['interests'][1]

print jan_second_interest