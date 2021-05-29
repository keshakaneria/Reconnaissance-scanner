from Wappalyzer import Wappalyzer, WebPage

import warnings
warnings.filterwarnings("ignore", message="""Caught 'unbalanced parenthesis at position 119' compiling regex""", category=UserWarning )

def Tech_used(host_name):
    output = "\n"
    try:
        webpage = WebPage.new_from_url(f'http://{host_name}')
        wappalyzer = Wappalyzer.latest()
        details=wappalyzer.analyze_with_categories(webpage)
        for d in details:
            for i in details[d]['categories']:
                output+=f"{i} : {d}\n"
    except Exception as e:
            output +="Sorry, The website SSL certificate could not be verified!\n"
    return output
#Have to install package python-Wappalyzer