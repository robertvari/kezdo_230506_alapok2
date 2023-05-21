def call_myself(n):
    print(f"I called myself {n} times.")
    if n == 10:
        return
    
    call_myself(n+1)


call_myself(1)