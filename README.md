<h1>Overview</h1>
<h2>Program to iterate through a list of firewall ip's, and to export rules with zero hit counts from the ACL</h2>
1. **Zero_counts.py**: allows user to select a file through file explorer to run zero hit count check against.
2. **hitcounts.py**: user must edit script in notepad to input a list of ip addresses needed to be searched through for zero hit counts. User will need a copy of hitcnt folder(found on backup server) locally on their machine, and ammend directory of folder in script.
3. Alternatively, build a file of all firewall rules to be checked to use with step 1. 
