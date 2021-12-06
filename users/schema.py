import graphene
from graphql_auth import mutations
from graphql_auth.schema import UserQuery, MeQuery
import graphql_jwt
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
from .models import ExtendUser
from graphql_jwt.decorators import login_required ,user_passes_test


class UserType(DjangoObjectType):
   class Meta:
      model = ExtendUser

class AuthMutation(graphene.ObjectType):
   register = mutations.Register.Field()
   token_auth = graphql_jwt.ObtainJSONWebToken.Field()
   verify_token = graphql_jwt.Verify.Field()
   refresh_token = graphql_jwt.Refresh.Field()
   update_account = mutations.UpdateAccount.Field()
   resend_activation_email = mutations.ResendActivationEmail.Field()
   send_password_reset_email = mutations.SendPasswordResetEmail.Field()
   password_set = mutations.PasswordSet.Field()
   password_reset = mutations.PasswordReset.Field()
   password_change = mutations.PasswordChange.Field()

class Query(graphene.ObjectType):

    users = graphene.List(UserType)
        
    def resolve_users(self, info):
        user = info.context.user
        print(user)
        # Check to ensure user is a 'manager' to see all users
        if user.is_anonymous:
            raise Exception('Authentication Failure: Your must be signed in')
        if user.role != 'manager':
            raise Exception('Authentication Failure: Must be Manager')
        return get_user_model().objects.all()

class Mutation(AuthMutation, graphene.ObjectType):
   pass

schema = graphene.Schema(query=Query, mutation=Mutation)