import wikipediaapi
import time

user_agent="wikipedia_game (ian.alexander.ng@gmail.com)"
wiki = wikipediaapi.Wikipedia(user_agent, "en")

#function to return list of links
def fetch_links(page):
    links_list= []
    links = page.links

    for title in links.keys():
        links_list.append(title)
    return links_list

def wikipedia_game_solver(start_page, target_page):
    links = fetch_links(start_page)
    for link in links:
        if link==target_page.title:
            return(True)
    return(False)


start_page = wiki.page("Ring (mathematics)")
target_page = wiki.page("Field (mathematics)")

print(start_page.links)

print(fetch_links(start_page))
print(wikipedia_game_solver(start_page,target_page))