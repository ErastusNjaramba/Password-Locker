import pyperclip
class credentials:
  """
  a class that creates new credentials for credentials
  """
  credentials_list =[]

  def __init__(self, credential_name, password,number):
    self.credential_name = credential_name
    self.password = password
    self.number = number
