
from graphene import (
    Schema,
    ObjectType,
    Field,
    Mutation,
    String,
    List,
    Int
)

class UserType(ObjectType):
    id = Int()
    name = String()
    age = Int()

class CreateUser(Mutation):

    # Arguments needed to create a use
    class Arguments:
        name = String()
        age = Int()

    # Output type of the CreateUser class
    user = Field(UserType)

    # Function to handle mutation. It returns the class to close the loop
    @staticmethod
    def mutate(root, info, name, age):
        user = { "id" : len(Query.users) + 1, "name" : name, "age" : age}
        Query.users.append(user)
        return CreateUser(user=user)
    
class UpdateUser(Mutation):

    # Arguments needed to create a use
    class Arguments:
        user_id = Int(required=True)
        name = String()
        age = Int()

    # Output type of the CreateUser class
    user = Field(UserType)

    # Function to handle mutation. It returns the class to close the loop
    @staticmethod
    def mutate(root, info, user_id, name = None, age = None):
        matched_user = None
        for user in Query.users:
            if user["id"] == user_id:
                matched_user = user
                break
        
        if matched_user is None:
            return None

        if name is not None:
            matched_user["name"] = name

        if age is not None:
            matched_user["age"] = age
        
        return UpdateUser(user=matched_user)


class Query(ObjectType):

    user = Field(UserType, user_id=Int())
    users_by_min_age = List(UserType, min_age = Int())

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
    
    @staticmethod
    def resolve_users_by_min_age(root, info, min_age):
        matched_users = [user for user in Query.users if user["age"] >= min_age]
        return matched_users
    
class Mutation(ObjectType):

    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()

schema = Schema(query=Query, mutation=Mutation)

query_user_gql = """
query {
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


create_user_gql = """
mutation {
    createUser(
        name : "New User"
        age : 45
    )
    {
        user {
            id
            name
            age
        }
    }
}
"""

update_user_gql = """
mutation {
    updateUser(
        userId : 4
        name : "Updated User"
        age : 101
    )
    {
        user {
            id
            name
            age
        }
    }
}
"""

if __name__=="__main__":

    result = schema.execute(query_user_gql)
    print(result)
    result = schema.execute(update_user_gql)
    print(result)
    result = schema.execute(query_user_gql)
    print(result)

