"""
py -m venv venv
pip install django
django-admin startproject core .
py manage.py startapp users
pip install graphene-django
pip install django-graphql-jwt
pip install django-graphql-auth

==================================

Get the user signed in
query{
  me{
    username
  }
}

===================================

register new user

mutation{
    register(email:"email@mail.com",
      	password1:"hunterDhunter",
      password2:"hunterDhunter",
      username:"oamahaikal1999"
    )
  {
        success,
        errors,
        token,
        refreshToken
  }   
}

===================================

get the token of existed user

mutation{
  tokenAuth(username:"<<your_username>>",password:"<your_password>"){
    token,
    refreshToken,
    errors,
    success
  }
}

====================================

verify:
mutation{
  resendActivationEmail(email:"<your_email>"){
   success
    errors
  }
}

mutation{
  verifyAccount(token:"<your_token>")
  {
    success
    errors
  }
}

<<<Note: token in verifyAccount not the jwt token; its token sent to the email (now its sent to the terminal)>>>


<<<password change needs the account to be already verified>>>>

mutation{
  passwordChange(oldPassword:"<your_old_password>",
    newPassword1:"your_new_password",
    newPassword2:"your_new_password"
  )
  {
    success,
    errors,
    token
  }
}

===========================================

mutation verifyToken {
  verifyToken(token: "<your_token>") {
    payload
  }
}

============================================

register:

mutation{
  register(email:"mail3@mail.com",username: "osamahaikal", 
    password1: "newpassword1!"
  , password2: "newpassword1!"
  
  ) {
    success,
    errors,
    token,
    refreshToken
    
	}
	
}


=======================================================================================

mutation{
  sendPasswordResetEmail(email:"ee.osamahaikal@gmail.com")
  {
    success
,
    errors
  }
}



mutation{
  passwordReset(token:"eyJ1c2VybmFtZSI6Im9zYW1haGFpa2FsIiwiYWN0aW9uIjoicGFzc3dvcmRfcmVzZXQifQ:1mu9L7:84UYOnOGY9cCy2kfBEfMc4Cym5mNl73rIMgJLR8XuTg"
  ,
    newPassword1:"hunterDhunter1!",
    newPassword2:"hunterDhunter1!",
  )
    {
      success,
      errors
    }
  
}

=======================================================
query{
	
  viewer(token:"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im9zYW1haGFpa2FsIiwiaWQiOiI1Iiwic3ViX25hbWUiOiIiLCJzdWJfZW1haWwiOiJlZS5vc2FtYWhhaWthbEBnbWFpbC5jb20iLCJleHAiOjE2Mzg3ODI5OTUsImh0dHBzOi8vaGFzdXJhLmlvL2p3dC9jbGFpbXMiOnsieC1oYXN1cmEtYWxsb3dlZC1yb2xlcyI6WyJtYW5hZ2VyIl0sIngtaGFzdXJhLWRlZmF1bHQtcm9sZSI6Im1hbmFnZXIiLCJ4LWhhc3VyYS11c2VyLWlkIjoiNSJ9fQ.b7QddXrlDbmPUp1JqqvXA17wvGR9oPbjm_kwx6KrAFA")
{
  username
  email
  id
  role
  isStaff
  isActive

}
}
query{
  users{
    edges{
      node{
        username
      }
    }
  }
  
}

"""