# from dataclasses import make_dataclass
# import json

# from schema import And, Schema, Use


# def command(name, **fields):
#     schema = Schema(And(Use(json.loads), fields), ignore_extra_keys=True)
#     cls = make_dataclass(name, fields.keys())
#     cls.from_json = lambda s: cls(**schema.validate(s))


# def greater_than_zero(x):
#     return x > 0


# quantity = And(Use(int), greater_than_zero)

# Allocate = command(
#     orderid=int,
#     sku=str,
#     qty=quantity
# )

# AddStock = command(
#     sku=str,
#     qty=quantity
