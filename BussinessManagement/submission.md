<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3  Business Management</td></tr>
<tr><td> <em>Student: </em> Somanadh Koneti (sk3395)</td></tr>
<tr><td> <em>Generated: </em> 4/15/2023 8:51:51 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-3-business-management/grade/sk3395" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <div>Initial Preperation:</div><div><ol><li>Create two new dynos/VMs in Heroku:</li><ol><li>is601-ucid-mp3-dev</li><li>is601-ucid-mp3-prod</li></ol><li>Configure the heroku config vars and github secrets similar to how dev/prod were setup</li><li>Create two new secrets for github and set the values per the machine names in step 1</li><ol><li>HEROKU_APP_MP3_DEV</li><li>HEROKU_APP_MP3_PROD</li></ol><li>Duplicate your dev/prod yml files and have it listen to the mp3-dev and mp3-prod branches respectively</li><ol><li>Make sure you refer to the proper app secrets from step 3</li><li>You can merge these into regular dev/prod later but you'll want your final project to deploy over it (overwrite) on the normal dev/prod dynos/VM</li></ol><li>You can add this HW branch to the dev yml to test your deployments prior to the pull request to dev from step 4</li></ol></div><div><br></div><div><br></div><ol><li>checkout dev and pull any latest changes</li><li>Create a branch called mp3-prod and immediately push it</li><li>Create a branch called mp3-dev and immediately push it</li><li>Create a branch called MiniProject-3</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li><b>Immediate add/commit/push to github</b></li><li>Open a pull request to mp3-dev and keep it open until you're done adding the submission file</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li><li>&nbsp;pytest BusinessManagement/test/name_of_test.py -rA</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item and add a related commit message for clarity)<br></li><ol><li>Do not delete any provided comments</li></ol><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 10</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together and reuse the image</li><li>Ensure all screenshots are properly captioned in the deliverable section so it's clear what part you're trying to show</li></ol><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from mp3-dev to mp3-prod and merge it</li><ol><li>If you want to keep original dev/prod up to date you can merge the changes into those, but they will cause a deploy to occur for each so be mindful</li></ol><li>Navigate to the submission file under the BusinessManagement folder from mp3-prod</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>Some files will have "DO NOT EDIT" mentioned, please don't edit these. If there's a doubt about any of them ask.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>If a test case isn't possible to complete, capture the failed test case locally via `pytest BusinessManagement -rA` first, then you can rename the function to `off_original_name`.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div>Note: db.py has been updated to use pymysql instead of mysql-connector-python to aid in easier queries.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>May want to download branch as a zip, then copy/paste the files into your repo (if/when you do, please immediately do a git add/commit to record the baseline items)</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232254934-cd138d2c-8445-41b5-8bc8-58991609f11e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the index page being displayed (from dev)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/231901355-673c0c31-d5a3-4291-9786-3fc43a347f62.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot from the DB extension of vs code / IDE<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route (code)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232255035-7d2568e6-a2f2-40af-bb1a-0ca99157bf84.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for checking weather the file is csv or not<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232255119-aa9fc4ea-2fdc-4b9e-8364-08c8c4198078.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>reading file and appending into dictionary code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232255361-a46a368b-925f-4148-9558-dddfbe95f4f2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>processed records displaying in flash message code.if nothing loaded this part of importcsv-8<br>code executes<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232255615-d7d4fba2-60ca-4d4d-90fb-2f6d4e79dc06.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> showing the proper success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232255646-50ecb876-6b94-4b97-825e-6b1104c4b031.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the error message when the form was submitted without a file attached<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232255691-e12f4dac-918a-4af6-b6e8-42ae7d4d7f4a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the error message when the file is not a .csv file<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232255792-4dd2f73c-012c-4044-8397-82f4d9dddc63.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing some company data was uploaded<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232255833-4b876775-8988-43ee-8c55-34e7e4a10102.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing some employee data was uploaded<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/231903396-1788f35a-c560-4250-abfc-3e39185dca0e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>first_name, last_name, company (id), email was obtained with flash messages if missing. And<br>Insert query and flash message to print exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232256099-fb166501-fda4-42a1-8870-b3388e12c76a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> last_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232256134-82f28266-bcfe-469e-9498-20bf7fb6fcfd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>first_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232256163-24622629-e516-4060-ab99-5a68a52da4d5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232256231-00c4c717-b067-4edd-af31-c6ed1c3b339a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>filled in valid data prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232256251-32724894-0828-4e14-ad21-2d5b8a846349.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232256323-fd584deb-3013-47ac-8e03-62d71e55c471.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing of previous entered employee details<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/231908112-f644abce-bec6-4d8f-a723-7df2eb419afa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Screenshots of code for search route of employee. The select query is<br>used to retrive data and checking requested args for name, email, company, and<br>appending filter for name, email, company.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/231908267-30f54e05-276f-43be-918a-f7c59aed7ca6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Screenshots of code for search route of employee. error message if limit<br>is out of bound.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232256472-3eaf801f-b4f1-4d8e-afee-ae918977743a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>results with first_name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232256532-727c8784-a789-4f2c-9c1d-65bb0030bb5f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>results with last_name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232256630-be557297-b35b-434f-b2f1-74888a9cee99.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>results with email filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232256678-ad69e7cb-2307-46f5-b229-ee48eafc44b9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>results with company filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232256818-c31f30ba-93fd-40bf-b927-36a323961a60.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>one asc filter applied to email<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232256870-0146e829-3166-45db-a6ef-9f87dcf3506b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> one desc filter applied to email<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/231912594-d896da64-5695-4811-a4a6-445ce24733d6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code should retrieve id (from request args) first_name, last_name, company (id), email from<br>form. Missing id should be handled with a flash message and redirected back<br>to employee search. And Flash message first_name, last_name, email, company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/231913445-6b36a809-5dfc-4e9a-a2eb-ce628b38f66b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>update query<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/231913673-486f9a9f-2fd8-491a-bc7c-51262e646319.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Except blocks should have a user friendly message flashed and a print() of<br>the exception<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/231913948-fb6ead0a-cab0-4501-ba03-a31d440a5091.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Proper SELECT query should be visible<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/231914138-ccf50a37-d63e-4cd9-b4c7-2db3efd4566c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Employee data should be passed to the render_template()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232257910-87079958-cb0b-490a-8651-ee3fbc0c6318.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data before an edit first_name=zona<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232257951-70bce106-d852-4d74-9d21-40d04e86c0fc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data after an edit first_name=zona Gabriel<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232257860-f1b42fba-157c-4b9a-914c-675ba6b9deaa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>before edit of first_name=zona<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232257997-b56e196c-64d1-4dae-93de-c9b2dd84ad31.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data after an edit first_name=zona Gabriel<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/231914712-a8d37966-c513-4f26-b579-decfd7dcc988.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code retrieve form data for name, address, city, state, country, zip, website and<br>flash messages if missing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/231915672-019f75d4-905b-4667-bfb9-c8aef7ced703.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>insert query. And Except block should have a user-friendly message flashed and a<br>print() of the exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232258206-aedad021-085c-441e-8b6a-530bfb07a9d5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>filled in valid data prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232258248-af058d2c-cab7-4d97-a3f8-253d01bd45fa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232258518-3bfd387b-8ca0-4afd-964e-e0bcf92bfd8f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>zip,address,city,name,country error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232258550-d84819d3-b32c-4779-a0b9-b897d85c6d1b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>state error<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232258604-5e7f81f0-e996-43ce-a564-3a96e6dea94f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>new company DB record from VS Code / IDE<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/231916286-27a4b6a4-a3a5-425f-b082-6bd0cd618dbd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>SELECT query should fetch id, name, address, city, country, state, zip, website, employee<br>count (as employee) for the company (likely a sub-query is needed). Check request<br>args for name, country, state, column, order, limit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/231916618-1c0dbb5a-71f5-4827-a5d4-aff159ea595b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>append an equality filter for state if provided,if country provided and name. And<br>append sorting if column and order are provided and within the allows columsn<br>and allowed order asc,desc allowed_columns = [&quot;name&quot;, &quot;city&quot;, &quot;country&quot;, &quot;state&quot;]<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/231917003-7904691f-e0ce-4b21-a982-14bf4d216720.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>append limit (default 10) or limit greater than or equal to 1 and<br>less than or equal to 100 and printing error message if it exceeds.<br>And Except block should have a user friendly message flashed and a print()<br>of the exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232258747-89257a52-8866-4851-bfc2-4a4d09526b68.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>results with name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232258796-a41e1a9c-6734-4d9c-b1d4-d815e88439bf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>results with country filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232258834-505a92cf-63b3-4558-bbd1-14280086331d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>results with state filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232258870-c55f5ba9-0086-48c1-ae3f-e20ca8b5dc78.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>one asc filter applied  to name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232258908-18b67452-a766-4e3a-9c6e-489d71341796.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>one desc filter applied to name<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/231917880-8e2c23ad-baea-463f-bcd9-361d1fa8aa71.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code should retrieve id (from request args) name, address, city, state, country, zip,<br>website from form. If id isn&#39;t present flash related error message and redirect<br>to company search and flash messages if they are missing.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/231918255-7fb6459c-5e02-4429-a11b-8e85ab63333a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>query update code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/231918474-eb615fdb-5f7b-4968-bb01-2992f6a0ff18.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Proper SELECT query should be visible with the passed in data<br> and Company<br>data should be passed to the render_template()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232259183-04727f7f-f60a-4618-888a-6bace9b22ba1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data before an edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232259292-65a25348-4e09-4232-99f2-2c1fad9fc5ce.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data after an edit<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232259238-d245d301-579b-4a68-b2b7-4d5472629fac.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data before an edit address=Hamilton st<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232259318-aec9473e-b138-4236-a565-536f941f4bd4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data before an edit address=JSQ<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/231920401-1464b853-f6ea-4fc3-93fe-a5e3d9664deb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Deleting employee by id, if missing flashing the related message. And redirecting to<br>employee search, and All request args (minus id) are passed to the redirect<br>route<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232259566-8124d234-387e-4911-aedd-fb1d6ddef562.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>before<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232259601-7f50ef81-ac4b-403a-b4e0-219281cb7e10.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232259615-45a33026-7165-4d2e-a085-edcdd0b39b45.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after result<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232259656-911cbb51-804b-4ba6-b59c-717dca07eda7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>deleting company by id, if missing flashing the related message. All request args<br>are passed to the redirect route. And redirecting to company search<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232259778-74440d66-fd14-46ed-9fa6-97ba8d73e8fd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>before<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232259800-11772b77-179e-452e-8477-6c4707f4ec59.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232260170-7c161b74-4357-408c-ba49-7c6a83ccdd53.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>passed test cases<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <p>faced issues in clearing test cases, and connecting database with python .<br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-3-business-management/grade/sk3395" target="_blank">Grading</a></td></tr></table>