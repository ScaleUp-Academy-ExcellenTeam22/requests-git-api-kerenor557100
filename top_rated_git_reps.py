#Submitted by: Keren Or Hadad 208025205
from github import Github

#I created a git access token in order to be able to request queries from Git
ACCESS_TOKEN = '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'

g = Github(ACCESS_TOKEN)

"""
num repos: number of repositories to return (default is 5)
language: qualifier of the query- return repositories writen in "language" programing language (default is python)

this function defines a query that request all the repositories which are written in a specific (given as a parameter) 
programming language, sort the result by stars in descending order.
(The query returns only 1000 results by definition of Github API so I sorted from the returned results).
"""
def search_github(num_repos=5, language="python"):
    query = "repositories language:" + language
    result = g.search_repositories(query, 'stars',  'desc')

    for repo in result[:num_repos]:
        print(f'{repo.name} is a Python repo with {repo.stargazers_count} stars')


if __name__ == '__main__':
    language = input('Enter programming language: ')
    num_repos = input('Enter number of repositories: ')
    search_github(int(num_repos),language)

"""
output: 

Enter number of repositories: 6
NLP-progress is a Python repo with 20194 stars
ipython is a Python repo with 15329 stars
salt is a Python repo with 12292 stars
calibre is a Python repo with 12107 stars
stanford-tensorflow-tutorials is a Python repo with 10157 stars
scipy is a Python repo with 9527 stars

"""