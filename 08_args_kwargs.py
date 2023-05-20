def args_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

args_kwargs(
    1,
    2,
    3,
    name="Csaba",
    address="Pécs",
    email="csaba@gmail.com"
)