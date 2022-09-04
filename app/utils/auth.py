from flask import session, redirect
from functools import wraps
# functools have several helpers available

def login_required(func):
  @wraps(func)
  #preserves the original name when creating the wrapped fxn, ie func(...arguments)
  def wrapped_function(*args, **kwargs):
    # captures all the keywords regardless of amount of arguments
    # if logged in, call original function with original arguments
    if session.get('loggedIn') == True:
      return func(*args, **kwargs)
    return redirect('/login')
  
  return wrapped_function