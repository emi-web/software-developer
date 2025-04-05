# keyword arguments
# when we put ** we need put the name of the parametre
# this wil print('id':'id') and this is call an dictionary(first is the parametre and second is the argument)
# how to access these values in  the function(["name"])


def get_product(**data):
    print(data["name"],
          data["desc"])

get_product(id="id", 
            name="iphone",
            desc="this is a phone"
            )


