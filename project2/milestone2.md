<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Shop Project</td></tr>
<tr><td> <em>Student: </em> Somanadh Koneti (sk3395)</td></tr>
<tr><td> <em>Generated: </em> 4/26/2023 3:24:04 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone-2-shop-project/grade/sk3395" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Users with admin or shop owner will be able to add products </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of admin create item page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/234468798-6ed6bf63-bade-4a21-be23-91182836feb1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Users with admin or shop owner adding products<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of populated Products table clearly showing the columns</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/234469747-954ca5c3-066f-4e15-8226-860de1098a03.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of populated Products table<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly describe the code flow for creating a Product</td></tr>
<tr><td> <em>Response:</em> <p>By filling up the values in the add, values returns to shop.py function.<br>And checks id is passed or not and check if the action is<br>to edit or add. As no id is passed this is a create<br>action and insert statement is executed passing the values to Products table and<br>success flash is displayed.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/16">https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/16</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sk3395-prod.herokuapp.com/admin/item">https://is601-sk3395-prod.herokuapp.com/admin/item</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Any user can see visible products on the Shop Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Shop page showing 10 items without filters/sorting applied</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/234472565-1be236bd-74c6-40c9-ace6-d9333b183070.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Shop page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/234472720-0bd62df7-3444-40d2-a762-cb0ca5bb6454.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Shop page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Shop page showing both filters and a different sorting applied (should be more than 1 sample product)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/234473263-82193bb6-1d55-4476-938d-c2b78de8b584.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shop page showing both filter-Food applied and Price-Low to High sorting applied<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the filter/sort logic from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/234499715-382c32b2-187f-4d2e-80c4-54e046cb4dc2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the filter/sort logic<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Briefly explain how the results are shown and how the filters are applied</td></tr>
<tr><td> <em>Response:</em> <p>In shop page we get the items and details from Products table whose<br>visibility is 1.we can search in the page by name or select a<br>category or sort on price &quot;High to Low&quot; or &quot;Low to High&quot;.When we<br>search using one/all of the above option. we go to shop_list function in<br>shop.py and based on the input we add a where condition to the<br>query. and display the results again<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/16">https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/16</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sk3395-prod.herokuapp.com/shop">https://is601-sk3395-prod.herokuapp.com/shop</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Show Admin/Shop Owner Product List (this is not the Shop page and should show visibility status) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the Admin List page/results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/234477112-b15d3bdf-ee72-488b-bb5f-751933fd73cc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the Admin List page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the results are shown</td></tr>
<tr><td> <em>Response:</em> <p>Without any filter we select all fields from Products table and pass it<br>to html page. As no where condition is specified, every product will be<br>displayed irrespective of visibility status<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/16">https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/16</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sk3395-prod.herokuapp.com/admin/items">https://is601-sk3395-prod.herokuapp.com/admin/items</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin/Shop Owner Edit button </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the edit button visible to the Admin on the Shop page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/234472565-1be236bd-74c6-40c9-ace6-d9333b183070.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the edit button visible to the Admin on the Shop page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the edit button visible to the Admin on the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/234480873-a8ec9207-030d-4981-b265-05e7cf43d126.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>creenshot showing the edit button visible to the Admin on the Product Details<br>Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot showing the edit button visible to the Admin on the Admin Product List Page (The admin page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/234477112-b15d3bdf-ee72-488b-bb5f-751933fd73cc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the edit button visible to the Admin on the Admin Product<br>List Page <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after screenshot of Editing a Product via the Admin Edit Product Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/234479089-ab36f7ac-10b6-40ba-a434-42bf99878278.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>before screenshot of Editing a Product via the Admin Edit Product Page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/234479238-a6afbf6c-61bc-4005-86de-a794969954f3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After screenshot of Editing a Product via the Admin Edit Product Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p>In shop.html for each product we check if the user is logged in<br>and the user is admin, if both cases are true we display a<br>edit button which redirect to item page with the product details.And it works<br>same for item details page. The admin items page has edit button default<br>as the page is only accessed by admin.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/16">https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/16</a> </td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sk3395-prod.herokuapp.com/">https://is601-sk3395-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Product Details Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the button (clickable item) that directs the user to the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/234472565-1be236bd-74c6-40c9-ace6-d9333b183070.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the button that directs the user to the Product Details Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the result of the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/234481461-9ec331a9-c320-44a4-aa7d-bc3bfab07746.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the result of the Product Details Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p>The product name is clickable because i have used anchor tag, when clicked<br>will pass the product id to itemdetails function and get all details from<br>Products table passing the id and render them in the itemdetails page.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/16">https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/16</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file (can be any specific item)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sk3395-prod.herokuapp.com/itemdetails?id=2">https://is601-sk3395-prod.herokuapp.com/itemdetails?id=2</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add to Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the success message of adding to cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/234483913-d28e3ced-0f7b-4e65-bfcf-6967c95315c0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the success message of adding to cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the error message of adding to cart (i.e., when not logged in)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/234484103-934d61ba-0bb0-412f-8c1d-1650bebce2ff.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> screenshot of the error message of adding to cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Cart table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/234483710-6e51aaff-78db-4391-b527-e9756cc124ef.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Cart table with data in it<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Tell how your cart works (1 cart per user; multiple carts per user)</td></tr>
<tr><td> <em>Response:</em> <p>1 cart per user, having product_id &amp; user_id.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Explain the process of add to cart</td></tr>
<tr><td> <em>Response:</em> <p>Adding products by clicking the ADD button, the product id as hidden field,<br>quantity field gets submitted to cart function in shop.py,and as the product id<br>is passed and quantity is greater than 0, we insert the product id,<br>user id, desired quantity, and unit_price into S_cart table.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/16">https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/16</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> User will be able to see their Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart View</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/234486457-f524d4a2-df62-42a7-aa66-ba59e4151d83.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Cart View<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the cart is being shown from a code perspective along with the subtotal and total calculations</td></tr>
<tr><td> <em>Response:</em> <p>BY click the cart, the cart function checks if there is no product<br>id passed,If not it is not a add or update function and goes<br>to SELECT block getting, id, product id, name, desired quantity and calculates the<br>subtotal multiplying the desired quantity and unit_price in select statement only, pass user<br>id these values to cart.html. For the total calculation, we render each item<br>as a row in table in the HTML output and and for every<br>row we add the subtotal value and variable total and later display it<br>as total in the bottom.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/16">https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/16</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sk3395-prod.herokuapp.com/cart">https://is601-sk3395-prod.herokuapp.com/cart</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> User can update cart quantity </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a before and after screenshot of Cart Quantity update</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/234486457-f524d4a2-df62-42a7-aa66-ba59e4151d83.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>before screenshot of Cart Quantity update<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/234489285-5d60d9b6-00e2-4ab0-b08f-fcdd3508ffc4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> after screenshot of Cart Quantity update<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a before and after screenshot of setting Cart Quantity to 0</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/234489285-5d60d9b6-00e2-4ab0-b08f-fcdd3508ffc4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>before screenshot of setting Cart Quantity to 0<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/234489603-bef86216-c2db-4c9b-86d9-c42edfb630ca.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after screenshot of setting Cart Quantity to 0<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how a negative quantity is handled</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/234489840-127c5310-f850-43c9-8bbd-86ea6edef637.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>negative quantity is handled<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain the update process including how a value of 0 and negatives are handled</td></tr>
<tr><td> <em>Response:</em> <div>Here a hidden product id will be passed to the cart function when<br>we click the update button. And in the code if the quantity is<br>greater than 0, we get the price &amp; name from products table,and we<br>update the quantity &amp; price in cart table by passing product id &amp;<br>user id.When we give 0 in quantity field, the code goes to DELETE<br>block, we delete the product from cart table by sending product id &amp;<br>user id.</div><div>We set the min value as 0 for input field in HTML,for<br>handling the negative value in quantity field.</div><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/16">https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/16</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Cart Item Removal </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a before and after screenshot of deleting a single item from the Cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/234493017-faded056-ca35-4277-872a-ee24e84f7d60.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>before screenshot of deleting a single item from the Cart<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/234493439-b4918456-ce0f-4525-b6a6-559d17cb6592.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> after screenshot of deleting a single item from the Cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after screenshot of clearing the cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/234493017-faded056-ca35-4277-872a-ee24e84f7d60.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>before screenshot of clearing the cart<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/121911063/234493679-9746f01d-35dc-46cd-b627-7fdf28e6c78f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after screenshot of clearing the cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how each delete process works</td></tr>
<tr><td> <em>Response:</em> <p>To deleting a single item in cart, a hidden field quantity of -1<br>will be submitted and in the cart function when the quantity is less<br>than zero, it processes the Delete query passing product id. When clearing the<br>total cart,we pass a variable delete_all equal to 1, and in the cart<br>function, if the delete_all value is True we delete the records in Cart<br>table passing user_id.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/16">https://github.com/somnadh-koneti/IS-601-Spring-2023--006/pull/16</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <div>issue in displaying the shop public page when no user is logged in,<br>if condition for authentication was missing in edit button and got an error,<br>as without the user logged in the code is checking for admin role<br>in current user. And then added the is-authenticated condition in admin .</div><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sk3395-prod.herokuapp.com/">https://is601-sk3395-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone-2-shop-project/grade/sk3395" target="_blank">Grading</a></td></tr></table>