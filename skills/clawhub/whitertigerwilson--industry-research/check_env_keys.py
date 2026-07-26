import os
keys = ['TAVILY_API_KEY','BOCHA_API_KEY','BRAVE_API_KEY','BING_API_KEY','SERPER_API_KEY','GOOGLE_API_KEY','JINA_API_KEY']
for k in keys:
    v = os.environ.get(k, '')
    status = '已配' if v else '未配'
    detail = (': ' + v[:8] + '***') if v else ''
    print(f'{k:<22} {status}{detail}')
