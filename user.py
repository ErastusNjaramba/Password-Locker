class User:
    """
    class that generates new instance of user
    """

    user_list =[] #Empty user list
     #Init method up here
    def save_user(self,user_name,user_password):
        '''
        save user method saves user object into user_list
        '''
        User.user_list.append(self)
    def delete_user(self,user_name,user_password):
        '''
        delete_user method deletes a saved user from the user_list
        '''
        User.user_list.remove(self)

    def __init__(self,user_name,user_password):

      # docstring removed for simplicity

        self.user_name=user_name
        self.user_password=user_password
  