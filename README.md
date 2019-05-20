# splunk_legacy_scripts
Python script for Zenduty-Splunk legacy alert integration

**Steps**:
  1. **On the Zenduty Dashboard:**
     1. To add a new Splunk integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.
     2. Next, go to "Services" and click on the "Manage" button correspoding to the relevant Service.
     3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Splunk (Legacy)" from the dropdown menu.
     4. Go to "Configure" under your integrations and copy the API KEY generated.
  
  2. **In Splunk:**
     1. Go to "$SPLUNK_HOME/bin/" and open "setSplunkEnv" file and create one variable "$ZENDUTY_KEY" and the value of this variable will be API KEY that you have copied earlier. So it will look like "$ZENDUTY_KEY= < API KEY >".
     2. Clone this Repository
     3. Copy the Python Script file and paste it into "$SPLUNK_HOME/bin/scripts"
     4. Sign In to Splunk. In the "Search and Report" app, search for the monitor metrics for Zenduty incidents to report on.
     5. Save this as an "Alert" from the "Save As" window in the top right corner. 
     6. Fill in the form and Click the "Add Actions" button under "Trigger Actions", select "Run a script" and write the name of the file which you have pasted in "$SPLUNK_HOME/bin/scripts" and save this Alert.
    
Splunk is now Integrated with your Zenduty account.
    
