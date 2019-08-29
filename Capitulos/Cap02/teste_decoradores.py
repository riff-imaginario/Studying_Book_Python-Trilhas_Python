def dec_text_to_html(func):
    def in_func(*args, **kwargs):
        func_to_return = func(*args, **kwargs)
        return f'<p>{func_to_return}</p>'
    
    return in_func


user_text = input('text: ')

@dec_text_to_html
def print_text(s_text):
    return user_text


print(print_text(user_text))