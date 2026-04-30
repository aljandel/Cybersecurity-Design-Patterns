request_data={"name":"Ali", "has_token":True, "is_admin":False}

def withdraw_money(request):
    if not request.get("has_token"):
        print("you have not token")
        return
    else:
        print("The AuthMiddleware layer has been successfully bypassed")
    if not request.get("is_admin"):
        print("you have not permission")
        return
    else:
        print("The IsAdminMiddleware layer has been successfully bypassed")
    print(f"The money has been withdrawn by {request.get('name')}")

withdraw_money(request_data)
