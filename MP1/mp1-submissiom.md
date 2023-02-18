<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - Tracker App</td></tr>
<tr><td> <em>Student: </em> Somanadh Koneti (sk3395)</td></tr>
<tr><td> <em>Generated: </em> 2/18/2023 3:41:09 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-1-tracker-app/grade/sk3395" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout dev branch and pull any pending changes&nbsp;</li><ol><li>&nbsp;git checkout dev</li><li>&nbsp;git pull origin dev</li></ol><li>Create a new branch for this assignment (see Desired Branch Name)</li><ol><li>git checkout -b MP1-Tracker</li></ol><li>Create a new folder called MP1 in your local repository</li><li>Create a new file called tracker.py</li><li>Copy/paste the content from this template:&nbsp;&nbsp;<a href="https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da">https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da</a></li><li>Add/commit/push the template file</li><ol><li>git add --all</li><li>git commit -m "adding template"</li><li>git push origin MP1-Tracker</li></ol><li>Create a pull request from MP1-Tracker to dev (keep it open, do not close it until you're done)</li><li>Solve the various todo items (also noted below in the deliverables) and fill in the evidence</li><ol><li>Periodically add/commit; recommended after each solved item or every few items</li></ol><li>Save and copy/download the markdown</li><li>Create a new file mp1-submission.md in the MP1 folder</li><li>Add the markdown content</li><li>add/commit/push all the pending files for this assignment (tracker.py and mp1-submission.md)</li><li>If everything looks good on the pull request complete the merge</li><li>Create a new pull request from dev to prod and merge it to update prod (not used yet but you want to keep this up to date)</li><li>checkout dev locally and pull the changes to be up to date</li><li>Navigate to the prod branch on github and find the mp1-submission.md file and get the link to the file to submit to canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Add Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited add_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/219849913-f7ad00ba-8c71-4e05-9a1c-3b835cd96835.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of edited add_task() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of add_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/219850163-cf25b76c-90f3-412e-a3e8-37b32a55911a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of success of add_task()<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/219850275-cd2bcea9-b299-4af6-950b-4fe96ff5ee47.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screentshot of failure of add_task()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for add_task()</td></tr>
<tr><td> <em>Response:</em> <p>updating&nbsp;<span style="font-size: 13px;">&nbsp;lastActivity with the current datetime value by datetime.now().setting up the name<br>,description,due to their respective variables in task, passing due as a parameter to<br>str_to_datetime() function to convert into one of the following form mention in function.<br>And appending task to the list. Checking weather the user entered name and<br>description and due, if any value was&nbsp; missing print &quot;Task not entered&quot; .</span><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Process Update Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited process_update() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/219850612-308ea1f3-9123-4856-94b4-3adb573bf2a2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of process update()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain the solutions to the checklist items for process_update()</td></tr>
<tr><td> <em>Response:</em> <p>check the index number exist in the list. If not print task does<br>not exist, if exist get the user input and call the function update_task()<br>and pass the user input as parameters&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Update Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited update_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/219850690-5450d291-4026-4fb7-988a-f7739473f303.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of update_task()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of update_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/219850893-1b0fa6b2-836e-4929-855e-11d28a36f9d1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/219850968-64f89a8d-b490-4a86-9d4e-28182b07da56.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>failure<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for update_task()</td></tr>
<tr><td> <em>Response:</em> <p>check the index number exist in the list. If not print task does<br>not exist, if exist use strip() to remove spaces starting, ending of the<br>string and check length of the string if it is equal to 0<br>, do not update variables and print &quot;No values to update&quot;, if not<br>equal to 0 update with new values and&nbsp; print &quot;updated successfully&quot; and update<br>lastActivity with datetime.now().<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Mark Task Done/Complete Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited mark_done() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/219851101-bed7dd11-3317-4d17-a705-aadebcf1003e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of mark_done()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of mark_done()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/219851273-d88b1c0e-fc1a-4079-a057-7924cc6ed9ec.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success, making a test mark done<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/219851383-6596bc80-6d66-49f9-ac57-962cfd333afa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>failure, trying to mark done a test which is previously marked as done<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for mark_done()</td></tr>
<tr><td> <em>Response:</em> <p>check the index number exist in the list. If not print &quot;task does<br>not exist&quot;, if exist check task[&quot;done&quot;] is false if it is, then update<br>task[&#39;&#39;done&#39;] with current date and time by using datetime.now() and print&#39;&#39; Task was<br>marked successfully&#39;. If it is not false print&quot; Task was done&quot;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> View Task Logic (and list) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited view_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/219851678-cc994450-c0cc-4488-9f0a-7c04292db8b8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of view_task()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of view_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/219851926-26c48855-e5ac-4c9b-a392-38250fc56fe3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/219852024-56bb7daf-cec9-436e-b862-35fe148fe9fb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>failure, invalid task number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot(s) of list_tasks() output showing a few examples</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/219852258-bd54e466-cf86-4587-8dc0-1252397617b7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>result of list_tasks() function<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited delete_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/219852452-b97b2ffe-650e-4219-96ca-c1f1ddc32478.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of delete_task()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of delete_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/219852535-97ac00ad-07e6-4b6f-8fc7-78e5b7c7ff51.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of succcess and failure of delete_task()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for delete_task()</td></tr>
<tr><td> <em>Response:</em> <p>check the index number exist in the list. If not print task does<br>not exist, if exist use tasks.pop() to remove the element from the and<br>pass index as parameter.&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Get Incomplete Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_incomplete_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/219852782-33b438fb-86f2-4c58-9642-b9530571aeaf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshots of get_incomplete_tasks()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_incomplete_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/219853022-ebd13164-e6d9-40d5-876f-d7ff93795565.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success screenshot<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/219853192-a61d8d09-e572-4ac3-8886-c76fc2285313.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>failure, no tasks to show<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_incomplete_tasks()</td></tr>
<tr><td> <em>Response:</em> <p>Use for loop to extract the data from the list and print the<br>data, if list is empty print &quot;No tasks to show&quot;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Get Over Due Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_overdue_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/219853447-0fd106cb-9cba-41b1-8783-0f1dbc83db3a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of get_overdue_tasks()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_overdue_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/219853358-a9687c0e-9c5d-4da0-91de-350f7217288a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>failure, shows no tasks<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/219853797-89e3fb9a-b104-4a4b-a5b9-b4fe66052879.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success screenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_overdue_tasks()</td></tr>
<tr><td> <em>Response:</em> <p>Use for loop to extract the data from the list&nbsp; and check the<br>tasks[&quot;done&quot;] is false and&nbsp;datetime.now() &gt; str_to_datetime(str(task[&#39;due&#39;])) if both are true store the data<br>in _tasks list and print the data, if list is empty print &quot;No<br>tasks to show&quot;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Get Time Remaining Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_time_remaining() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/219853898-f8fbf87a-b89c-4df1-9ede-cedc96ca0347.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of get_time_remaining()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_time_remaining()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/219854081-3d3c58d3-0856-463c-af5c-5f209c8cc680.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success and failure of results output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_time_remaining()</td></tr>
<tr><td> <em>Response:</em> <p>check the index number exist in the list. If not print task does<br>not exist, if exist store the datetime.now() value in now variable and store<br>the due_date value form task[&#39;done&#39;] in due variable. Substract the both due and<br>now variables and store it in rem variable. use rem.days to get number<br>of days, rem.days<em>24 to get number hours and store in hours variable, hours</em>60<br>to get number of minutes and store it in min variable, min*60 to<br>get number of seconds. And check if days or hours or min or<br>seconds variables are equal to 1 store them as day , if not<br>days. And store the variables in list, check if due_date &gt;present date print<br>&quot;due {list}&quot; else print &quot;overdue {list}&quot;.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of program output generated from filling in this deliverable (or close to it)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/219854366-737f1e70-296b-4f38-b4b4-8cd6cf710f0e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshots from deliverable outputs<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/219854399-f7e1d426-19ef-4431-886d-f1158ca7bbfc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshots from deliverable outputs<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/219854449-f85b31b3-ddb0-40f3-a460-48313c3d8b6a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshots from deliverable outputs<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/219854468-3c8da14a-352b-491f-b27c-203a6898f260.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshots from deliverable outputs<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/219854517-a614fae7-2a86-4dd0-af66-fccc2fc27a5c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshots from deliverable outputs<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/219854551-fdbc896e-54e2-40ab-bcd1-202d7f0eb8de.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshots from deliverable outputs<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) of the saved JSON file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/219854699-d4cdc325-3edb-45f0-b159-977e14997370.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>jason file screenshots<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Discuss any issues and how they were overcome or learnings from this project</td></tr>
<tr><td> <em>Response:</em> <p>No issues, learnt about datetime, Json, OS modules and how to create a<br>tracker.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request for this assignment (project branch to dev)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/4">https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/4</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-1-tracker-app/grade/sk3395" target="_blank">Grading</a></td></tr></table>