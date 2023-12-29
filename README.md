# ContactInfoMessageBuilder
Python script to pull specific contact information out of a CSV exported from ConnectWise Manage to generate a custom message.
This is used to build a quick list of important contacts and information about those contacts for a particular company in ConnectWise Manage.

Export contacts from Connectwise Manage by following these steps: 
  Companies > 
          Company > 
                Contacts > 
                      Export => This will export a file called contactlist.csv. 

The Type field to hold descriptive tags for specific contacs. There are also additional custom fields per contact that also have custom value choices. The order of and specific fields used will likely be different in your environment.
