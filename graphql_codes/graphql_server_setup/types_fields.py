
from graphene import (
    Schema,
    ObjectType,
    Field,
    String,
    Int
)

class UserType(ObjectType):
    id = Int()
    name = String()
    age = Int()


class Query(ObjectType):

    user = Field(UserType, user_id=Int())

    # dummy data source
    users = [
        {"id" : 1, "name" : "Andy Doe", "age" : 30},
        {"id" : 2, "name" : "John Doe", "age" : 21},
        {"id" : 3, "name" : "Sandra Smith", "age" : 56},
        {"id" : 4, "name" : "Oliver", "age" : 46}
    ]

    @staticmethod
    def resolve_user(root, info, user_id):
        print(root)
        matched_users = [user for user in Query.users if user["id"]==user_id]
        return matched_users[0] if matched_users else None
    
schema = Schema(query=Query)

gql = """
{
    user(
        userId : 4
    )
    {
        id
        name
        age
    }
}
"""

if __name__=="__main__":

    result = schema.execute(gql, root_value="Some other data source")
    print(result)

