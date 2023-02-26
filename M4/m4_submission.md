<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Somanadh Koneti (sk3395)</td></tr>
<tr><td> <em>Generated: </em> 2/26/2023 2:49:41 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/m4-simple-calc/grade/sk3395" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you're working in an up to date branch</p><ul><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li><li><code>git checkout -b M4-Simple-Calc</code></li></ul><p>This will likely be started in class.</p><p>Steps:</p><ol><li>Create a new Folder called M4</li><li>Create a new file called MyCalc.py inside this folder</li><li>Create a MyCalc Class</li><li>Define basic addition / subtraction / multiplication / division functions<ol><li>These functions should update an internal variable as a running total/value called&nbsp;<code><b>ans</b></code></li><li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero for example)</li><li>Since you'll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li></ol></li><li>Define a "main" logic to run when the program runs</li><li>This logic should ask for user input<ol><li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol><li>This will do an immediate calculation, print it, and store the answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li><li>Alternatively, the input can be&nbsp;<code>ans</code>, any valid math operator, any valid number (i.e.,&nbsp;<code>ans</code>&nbsp;* 2)<ol><li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li></ol></li><li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass (test cases should have a series of data passed into them)<ol><li>Test number-add-number</li><li>Test ans-add-number</li><li>Test number-sub-number</li><li>Test ans-sum-number</li><li>Test number-mult-number</li><li>Test ans-mult-number</li><li>Test number-div-number</li><li>Test ans-div-number</li></ol></li><li>Create a new file called m4_submission.md inside the M4 folder</li><li>Fill out the below deliverables</li><li>Generate the markdown and paste it into the m4_submission.md</li><li><code>git add .</code></li><li><code>git commit -m "adding m4 hw"</code></li><li><code>git push origin M4-Simple-Calc</code></li><li>Create a pull request M4-Simple-Calc to dev</li><li>Create a pull request dev to prod (after the previous one is merged)</li><li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li><li>Submit this link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/221396037-abbe7a20-19f4-4546-aad3-e4f5fb51e452.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>add function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/221396117-49688c59-1d85-4313-8982-e2acdfb05047.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>subtraction function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/221396165-a5ce5866-18db-484c-ba37-72ceb340013c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>multiplication function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/221396212-c4d24352-47ac-4bac-990e-229c2d3258cb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>division function<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of passing number-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/221396663-260cc92a-2915-426d-b1e4-4970905ce852.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>passing number-add-number Test Case and code snippet Checklist<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/221396939-495eaf85-9060-4ef2-a09f-1706aebc5300.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Result of num - add - num<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of passing ans-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/221396650-e6ae1671-23c6-427f-9b85-a9c976491aab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>passing ans-add-number Test Case and code snippet<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/221397050-c0d4b5b2-09fc-4f5e-8665-697b9fe13143.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Result of ans (add) num <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of passing number-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/221396663-260cc92a-2915-426d-b1e4-4970905ce852.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>passing number-sub-number Test Case and code snippet<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/221397207-9c9d6694-b469-45c9-85d5-18f1acb615dd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Result of num-sub-num<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshots of passing ans-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/221396650-e6ae1671-23c6-427f-9b85-a9c976491aab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>passing ans-sub-number Test Case and code snippet<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/221397273-517036e8-ffca-4d3f-8186-32657da64b5e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Result ans-mul-num<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshots of passing number-mult-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/221396663-260cc92a-2915-426d-b1e4-4970905ce852.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>passing number-mult-number Test Case and code snippet<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/221397463-ef4613fd-5194-468c-bbf1-a658362f9475.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Result num-mult-num<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshots of passing ans-multi-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/221396650-e6ae1671-23c6-427f-9b85-a9c976491aab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> passing ans-multi-number Test Case and code snippet<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/221397540-d04f77c1-8ad6-4100-8976-9cd9e48bb286.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Result ans-mult-num<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshots of passing number-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/221396663-260cc92a-2915-426d-b1e4-4970905ce852.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> passing number-div-number Test Case and code snippet<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/221397715-9ea6355a-b1f2-4854-a20f-5bdc7809eb5a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Result num-div-num<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshots of passing ans-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/221396650-e6ae1671-23c6-427f-9b85-a9c976491aab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>passing ans-div-number Test Case and code snippet<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/221397755-9031d229-26b1-44aa-9a67-85bf49b4fd89.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Result ans-div-num<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <p>Learnt how to code, Basic Calculator by using functions and while loop without<br>using classes in python. Try and Except statement used in Division function to<br>avoid division by 0 error.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>By typing the input string ans-opr-num , if ans substring is available in<br>input() string the ans value and num value is sent to the respective<br>operator function and same for the num-opr-num.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/6">https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/6</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/m4-simple-calc/grade/sk3395" target="_blank">Grading</a></td></tr></table>