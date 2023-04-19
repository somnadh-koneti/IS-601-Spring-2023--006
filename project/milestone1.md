<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Somanadh Koneti (sk3395)</td></tr>
<tr><td> <em>Generated: </em> 4/19/2023 2:13:21 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone1-deliverable/grade/sk3395" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232671597-24571a1f-667d-4b36-a866-2a0d5c2afda4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> invalid email validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232671820-587440dd-6bd0-413a-849b-4da00266717e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid password validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232671977-01407a6c-3c7b-4aaa-9671-c9e0ab183b41.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>passwords not much validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232672240-c920109b-52fd-41e7-875d-b0deb1f58102.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>form with valid data filled in before the form is submitted<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232702251-2cf96346-a98c-4fac-b7e6-a35fafee0bd4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>username not available validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232702620-9531e6e3-cd99-41fc-8302-5bce8de69c0a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email not available validation<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232703120-9549a182-39c0-4167-bf04-becb8ea4afc4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>valid user data from Task 1<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/14">https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/14</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>WTforms validators used to validate data both in frontend and backend, username must<br>be of length 2 &amp; 30 char and each user name must be<br>unique, email validation is done using email validator. password and confirm password both<br>must be same and should be length of min 8 char and bcrypt<br>hashing algorithm used to convert passcode into hashed password . email, hashed password,<br>username is stored in the user table.&nbsp;&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232708830-c7c7cfeb-cf3b-4899-898e-ef99a0799286.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>password mismatch validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232709151-01949ad1-7248-47f5-b8e6-f243aa085c11.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>validation based on non-existing user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232708408-4aed7448-b531-4616-9307-a6fad1bb087c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of successful login<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/14">https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/14</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>login form is handled using wt forms,here we will not use confirm pwd<br>field and use username or email field used in registration.</div><div>2. In the front<br>end, if the username or email field checks if data is entered or<br>not, and if the field has '@' it will use email validator else<br>it checks for the username format, if the length is between 2 &amp;<br>30 or not, and checks if password is entered or not.In the backend,<br>we fetch the data from users table passing email/username, if we get something<br>we compare the password &amp;then check if user is assigned roles</div><div>3. In the<br>front end, we first check if password entered &amp; then in back we<br>fetch the password from database based on username/email &amp; then check if the<br>passwords match, if they match then we delete the password from that point<br>in the program.</div><div>4. we fetch username, email, password from users table passing username/email,<br>and then check if passwords match, and then check if the user is<br>assigned is any roles from user roles tables &amp; fetch it.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232713057-69c1e22c-1a31-4290-aa77-6d641d34894a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the successful logout message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232713670-e91a172a-c3dd-406b-9ee5-97c39769446b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the logged out user can&#39;t access a login-protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/14">https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/14</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>we use flask_login package to work with user session &amp; manage it,&nbsp;</div><div><br></div><div>&lt;span</div><div>style="font-family: Arial;"&gt;In</div><div>our<br>main.py we’ll utilize LoginManager, t&lt;span</div><div>style="font-size: small; font-family: Arial;"&gt;his</div><div>handles</div><div>our user session and</div><div>provides helpful utilities</div><div>&lt;span</div><div>style="box-sizing:<br>border-box;"&gt;Since we’re using an app</div><div>factory we’ll defined a variable for login_manager outside of<br>the factory, then inside the factory we use its init_app() method to associate<br>the app .Next, inside of the app factory we’ll use theuser_loader decorator, this<br>will run a&nbsp; process to lookup a user by id</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232713670-e91a172a-c3dd-406b-9ee5-97c39769446b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the logged out user can&#39;t access a login-protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232715449-b9116a29-cab0-4ee4-a3ea-68ea7be99e25.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing a user without an appropriate role can&#39;t access the role-protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232715978-6c512369-3ca9-4e4c-941e-3db5cb0b7ddf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Roles table with valid data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232981703-b6fa3b86-5619-4904-a4ae-741a4ce9048b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> screenshot of the UserRoles table with valid data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/14">https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/14</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>Since we’re using an app factory we’ll defined a variable for login_manager outside<br>of the factory, then inside the factory we use its init_app() method to<br>associate the app, For the login protected pages, we decorate the views with<br>@login_required function, If the user is not logged in, it calls the &lt;span<br>class=&quot;pre&quot; style=&quot;hyphens: none;&quot;&gt;LoginManager.unauthorized function<br></p><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>similar to login protected page, here we use @admin_permission_require function from roles. permissions<br>package, If the user is not a admin,&nbsp; we raise 403 exception anddisplay<br>403 html page saying permission denied.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232708408-4aed7448-b531-4616-9307-a6fad1bb087c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>landing-page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232725120-5998711a-6bf5-4371-b7f6-aa3915c29a09.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>styled form<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232726585-6327b9b6-447b-402e-80cf-359a3665f3fa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>UI which doesn&#39;t  have any odd artifacts that are unstyled.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232726969-501c3c56-bb6d-4534-b11d-732d2a76676d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data output in a clean manner <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/14">https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/14</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p>we use the styles from bootstrap, navbars require a wrapping .navbar with .navbar-expand-lg<br>for responsive collapsing at large break point, and bg-light for color. .navbar-brand for<br>the project name.,.navbar-nav for a full-height and lightweight navigation<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232713670-e91a172a-c3dd-406b-9ee5-97c39769446b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the logged out user can&#39;t access a login-protected page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232715449-b9116a29-cab0-4ee4-a3ea-68ea7be99e25.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing a user without an appropriate role can&#39;t access the role-protected page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232671977-01407a6c-3c7b-4aaa-9671-c9e0ab183b41.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>password not much validation<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/14">https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/14</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <p>we use flask error handler functions for 403 &amp; 404 errors, and atmost<br>places we see what code is doing in backend and write a flash<br>message for that, if any field is missing or else other.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232725120-5998711a-6bf5-4371-b7f6-aa3915c29a09.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>User Profile page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/14">https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/14</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <p>when profile page is opened, if it is not a POST request then<br>email,username are fetched from users table passing user id, then the are rendered<br>into the profile form.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232738703-edcdaa02-4a5c-40f9-a7ef-4fbfd21a03c1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>username validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232738957-864400f9-84f8-4284-94b5-2b1a7a1a7947.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232740291-9abac67f-7b8c-49aa-9726-5bb6d036c00e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email/username already in use message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232741134-9d6bee29-1294-462d-9d42-092b59f77ed6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>password mismatch message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232741592-5dd343d6-1e73-43bd-8c63-2dfb8a0402eb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>password validation message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232742192-223fd9f2-95c9-4cdb-afea-a2088a180976.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>before the email=<a href="mailto:&#115;&#x6f;&#109;&#x6e;&#97;&#100;&#x68;&#51;&#51;&#51;&#51;&#64;&#x67;&#109;&#105;&#97;&#x6c;&#x2e;&#x63;&#x6f;&#x6d;">&#115;&#x6f;&#109;&#x6e;&#97;&#100;&#x68;&#51;&#51;&#51;&#51;&#64;&#x67;&#109;&#105;&#97;&#x6c;&#x2e;&#x63;&#x6f;&#x6d;</a><br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/232742714-aeb768a8-5ff9-4752-880e-b157edb8ee25.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after update the email=<a href="mailto:&#115;&#107;&#x33;&#51;&#x40;&#x67;&#x6d;&#97;&#x69;&#x6c;&#46;&#x63;&#x6f;&#109;">&#115;&#107;&#x33;&#51;&#x40;&#x67;&#x6d;&#97;&#x69;&#x6c;&#46;&#x63;&#x6f;&#109;</a><br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/14">https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/14</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <p>The code first checks for if it is POST request, if it is,then<br>it checks if current_password, password &amp; confirm are given, then it retrieves password<br>from users table, then the current password &amp; pwd from DB are compared<br>to check if they are the same or not, if they are not<br>same we will raise a invalid password flask, if they are same then<br>the new password is hashed &amp; updated in the database. Then the username<br>&amp; email are updated in the database and a flash message &quot;saved profile&quot;<br>is displayed.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>learnt how to create login web page and how to validate the user<br>input ,and update the user data in database .<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sk3395-prod.herokuapp.com/login">https://is601-sk3395-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone1-deliverable/grade/sk3395" target="_blank">Grading</a></td></tr></table>