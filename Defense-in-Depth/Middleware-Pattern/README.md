# Cybersecurity Design Patterns: Middleware Security
An implementation of the Chain of Responsibility pattern for scalable and decoupled security layers in Python.

#Concept & Objectives:

Most of the time, when we write certain functions, we need to protect the function. For example, if we have a function that withdraws money, 
but we want to protect this function so that not every request can execute it. We want it to check whether the request contains a token and also verify whether the token owner has admin responsibility.
 So now the function is conditional on two requirements:
 1. The requester must have a token.
 2. The requester must be an admin.


#The Monolithic Approach (Bad Practice):

After reading the objectives section, we might think about protecting the withdraw_money() function by placing conditional statements inside the function itself; business logic will not be achieved until the conditional statements are satisfied.
But is this method correct and professional? 
In fact, this method will show its flaws, including that a function in clean code should contain its own business logic, but in this way we have added verification and protection steps inside it. Also, these protection steps might be needed by another function, and here we would have to repeat the conditional statements(Code Redundancy) as they are in the other function. If we repeat these conditional statements in another function and later want to modify those protection layers, then we have to go into both functions and modify the conditional statements.
And this approach we will find embodied in the bad_practice.py file.


#The Middleware Approach (Best Practice):

In this approach, we will ensure that the core function remains clean by having it only contain its business logic. This is done by building two classes, each representing a layer of protection, instead of using a conditional statement as a protection layer. Then, the token verification layer (AuthMiddleware) will wrap the layer that checks whether the requester is an admin (IsAdminMiddleware), and the latter, in turn, wraps the withdraw_money() function. Here, to reach the withdraw_money() function, you must follow this path:

                                              AuthMiddleware -> IsAdminMiddleware -> withdraw_money()

You cannot access the IsAdminMiddleware layer except after passing the AuthMiddleware layer, and you cannot access the withdraw_money() function except after passing both layers AuthMiddleware and IsAdminMiddleware.
and this is similar to Onion Architecture.
and we embodied this approach in the code in the file secure_middleware.py.

