

def show_pics(html, nombre):
    with open (f'{nombre}.html' , 'w') as f:
        f.write(html)
  

if __name__ == '__main__':
    from apod import pull_fotos
    from html_module import create_html_pic
    dict = pull_fotos(2)
    html = create_html_pic(dict)
    show_pics(html, 'apod')
