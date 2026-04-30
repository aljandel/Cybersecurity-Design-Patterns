request_data={"name":"Ali", "has_token":True, "is_admin":True}

class AuthMiddleware:
    def __init__(self, next_layer):
        self.next_layer = next_layer
    def __call__(self, request):
        if not request.get("has_token"):
            print("you have not token")
        else:
            print("The AuthMiddleware layer has been successfully bypassed")
            return self.next_layer(request)

class IsAdminMiddleware:
    def __init__(self, next_layer):
        self.next_layer = next_layer
    def __call__(self, request):
        if not request.get("is_admin"):
            print("you have not permission")
        else:
            print("The IsAdminMiddleware layer has been successfully bypassed")
            return self.next_layer(request)

def withdraw_money(request):
    print(f"The money has been withdrawn by {request.get('name')}")

layer1= IsAdminMiddleware(withdraw_money)
layer2= AuthMiddleware(layer1)

layer2(request_data)

