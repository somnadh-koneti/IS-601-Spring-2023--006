<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 2 - Burgers</td></tr>
<tr><td> <em>Student: </em> Somanadh Koneti (sk3395)</td></tr>
<tr><td> <em>Generated: </em> 3/21/2023 3:55:53 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-2-burgers/grade/sk3395" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb">https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb</a>&nbsp;</li><li>Put them into a subfolder in your repository folder (I called my folder BurgerMachine)</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/226519426-243d6de4-9246-4506-8d56-4d9cd7257150.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of calculate cost()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <p>iterating the elements from the list and using i.cost to find out the<br>cost of the product , and checking the data type int or float<br>and adding it to the variable val and return it .<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/226496357-bf9972ac-b63b-436a-b40c-afb421fd5d27.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of outofstockexception , needscleaningexception, invalidchoiceexception<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/226496571-fb4d3c60-25f6-4993-847a-e874252e9984.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of exceededremainingchoicesexecption , invalidpayment exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <p>OutOfStock Exception =&nbsp;first i was trying to find out in which stage the<br>out of exception was ocurred and printing the bun or patty or toppings<br>was out of stock. The bun or patty or topping variable&nbsp;stores the input<br>we enter.<div>&nbsp;NeedsCleaning Exception =&nbsp;I was asking the user to type the command clean.<br>if the user enters the correct commnad cleaning gets sucessfull, if the command<br>enterd is wrong machine cleaning fails and displays&nbsp;an message to enter correct command.</div><div>InvalidChoice<br>Exception =&nbsp;first i was trying to find out in which stage the invalid<br>choice exception was ocurred and printing the bun or patty or toppings entered<br>was not in list. The bun or patty or topping variable stores the<br>input we enter.<div>ExceededRemainingChoices Execption = first i was trying out to find out<br>in which stage the exceeeded remaining choices was ocurred and printing you have<br>exeeced the limit of chossing patty or toppings. if it is in patty<br>moving it to next stage toppings or if it is in toppings moving<br>it to next stage payment section .</div><div>InvalidPayment exception =&nbsp;if invalid payment exception occurs,<br>it will display an message enterd wrong amount payment failed.<br></div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/226541983-3cc85c42-148c-443d-816c-b0b4b2a8705c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of test 1,2,3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/226542277-a7df9eeb-46a5-4d0e-8f48-671d943feb7d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of test 4,5,6<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/226542570-2043c183-9931-4e8b-aa64-95154554396b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of test 7<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/226542809-affb7074-886c-429e-b1d1-a9511bd6cee4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of 8<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/226543305-046cc350-8866-4ee7-a96c-002881df259c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>All Tests 1-8 passing<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <p>test1= In this test we are checking wheather selection of bun is first<br>selection by currently selecting is equal to stage bun<div><br><div>test2 =&nbsp;the objective of the<br>test case is to handle outofstock exception when quantity of patties is 0.<br>we set quantity of the first patties[0].quantity=1. And then it handles the order<br>by machine handling method such as handle_bun, handle_patty. we use try and except<br>to catch an outofstock exception, if quantity is 0 and exception raised then<br>assert false will pass the test. If exception not raised machine.patties[0].quantity==1 will fail<br>and test is failed.</div><div><br></div><div>test3=&nbsp;the objective of the test case is to handle outofstock<br>exception when quantity of toppings is 0. we set quantity of the first<br>toppings[0].quantity=1. And then it handles the order by machine handling method such as<br>handle_bun, handle_patty and handle_toppings. we use try and except to catch an outofstock<br>exception, if quantity is 0 and exception raised then assert false will pass<br>the test. If exception not raised machine.toppings[0].quantity==1 will fail and test is failed.</div><div><br></div><div>test4=<br>the test checks that the machine can handle the max number of patties.<br>the test handles the burger with white burger bun and loops the max<br>limit number of turkey , and when the turkey reaches to -1 exceededremainingchoices<br>exception occurs.here,the assert keyword confirms the remaining number of patties added and final<br>patties are 0.&nbsp;&nbsp;</div><div><br></div><div>test5=&nbsp;&nbsp;the test checks that the machine can handle the max number<br>of toppings. the test handles the burger with white burger bun and loops<br>the max limit number of ketchups , and when the ketchup reaches to<br>-1 exceededremainingchoices exception occurs. assert keyword confirms the remaining number of toppings added<br>and final toppings are 0.</div><div><br></div><div>test6=&nbsp;the test first uses reset() function to reset the<br>remaining_patties and toppings and makes inprogress burger list empty and stage to bun.<br>we select bun, toppings, patty by machine handle methods and claculate the cost<br>by calculate_cost() function and compare it with the value we enterd , the<br>test case passes if it matches with the value we enterd.&nbsp;</div><div><br></div><div>test7=&nbsp;In this test<br>we select bun, toppings, patty by machine handle methods and claculate the cost<br>by calculate_cost() function and stores it in a variable and compare it with<br>handle pay and the process is repeated with other order and compare the<br>machine.total_sales with the sum of the variables. if the values are equal test<br>case passes.</div><div><br></div><div>test8= In this test we select bun, toppings, patty by machine handle<br>methods and claculate the cost by calculate_cost() function and stores it in a<br>variable and compare it with handle pay and the process is repeated with<br>other orders and compare the machine.total_burger==3 and BurgerMachine().total_burgers==0.</div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/10">https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/10</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>writing exceptions were easy, faced some issues while writing code for testcases, but<br>issues were resolved.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/226545470-caf5d5dc-79d9-420a-add7-691d9014ad17.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>2 burger selections<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-2-burgers/grade/sk3395" target="_blank">Grading</a></td></tr></table>