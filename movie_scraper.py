"""
Coded by Marcus Willock :)
"""

from BeautifulSoup import BeautifulSoup
import urllib2
import re 


def info(soup):
    
    """
    The soup is the HTML of the webpage.
    
    Theaters are divided into two categories (odd and even).
    
    Note: If you want to change the number of theaters that you are 
          looking at, then change the limits for theaters1 and theaters2.
    """
    
    theaters1 = soup.findAll("div", {"class": "list_item odd"}, limit = 1)
    theaters2 = soup.findAll("div", {"class": "list_item even"}, limit = 1)
    
    # Places all theaters into one list
    theaters = theaters1 + theaters2

    
    for theater in theaters:
        
        """
        Iterates through the list of Theaters and gathers the
        name and phone number of said theater
        """
        
        #Finds the name of Theater
        theater_html1 = theater.findAll("div", {"class" : "fav_box"})
        find_title = re.compile('itemprop="url">(.*)</a>')
        theater_title = re.findall(find_title, str(theater_html1))
        
        #prints name of movie theater
        print "\n\n\n\n\n","Theater: " ,str(theater_title)[2:-2], "\n"
        
        
        
        #Finds the phone number of Theater
        theater_html2 = theater.findAll("div", {"class": "address"})
        find_phone_number = re.compile('<span itemprop="telephone">(.*)</span>')
        phone_number = re.findall(find_phone_number, str(theater_html2))
        
        #prints phone number of movie theater
        print "phone number: ",str(phone_number)[2:-2], "\n\n", 
           
        
        """
        Finds the movie(s) information and puts them into a list
        """
        
        
        movie_html = theater.findAll("div", {"class": "list_item"})
        
        #A counter for the list of movie title created in the next loop.   
        movie_counter = 0
        
        
        for movie in movie_html:
            
            """
            Iterates over the list of the movie's (html info)
            """
                
            #Finds the movie titles and places them into a list called "movie_title"
            find_movie_title = re.compile('Poster" title="(.*)" src=')
            movie_title = re.findall(find_movie_title, str(movie_html))
            
            #prints a movie title to screen
            print "\n\n\t\t", movie_title[movie_counter], "\n"
            movie_counter +=1
            
            #The count is used to tell whether the showing is regular, 3D, or IMAX 3D
            count = 0
            
            """
            Finds the html for the movie showtimes
            """
            
            showtimes_list = movie.findAll("div" , {"class": "showtimes"})
            
            
            """
            Scraping the showtimes was annoying...
            
            Steps:
            
            1. Make the showing (html) into a string.
            2. Split the string by new line ("\n"), which places each line into a list
            3. iterate over this list (Note: the list is filled with strings)
            4. Create an if statement that finds the time by looking at the last letter
               in the string.
               
            """
            
            for showings in showtimes_list:
                count+=1
                
                if count ==1:
                    showings = str(showings).split("\n")
                    print "Regular"
                        
                    for times in showings:
                        if times.endswith("m") or times.endswith("0") or times.endswith("5"):
                                 
                            print "\t\t", times
                            
                elif count ==2:
                    showings = str(showings).split("\n")
                    print "3D" 
                        
                    for times in showings:
                        if times.endswith("m") or times.endswith("0") or times.endswith("5"):
                                
                            print "\t\t", times
                            
                elif count ==3:
                    showings = str(showings).split("\n")
                    print "IMAX 3D" 
                        
                    for times in showings:
                        if times.endswith("m") or times.endswith("0") or times.endswith("5"):
                                
                            print "\t\t", times
                            
                else:
                    print "Why are there 4 (or more) different type of movie showings?! Crazy, right?"
                    
    """
    The return statement does nothing. Delete it if you want.
    """
                    
    return "done!!!!"



def main():
    
    """
    Takes the URL and creates BeautifulSoup out of it.
    """
    
    URL = "http://www.imdb.com/showtimes/cinemas/"
    page = urllib2.urlopen("http://www.imdb.com/showtimes/cinemas/").read()
    soup = BeautifulSoup(page)
    
    info(soup)
    
    """
    The only fuction of the user input is to give you enough time to
    view the information on the screen.
    """
    end = raw_input("\n\nThis box will disappear as soon as you push enter...")
    
    print "Finished"
    
    
if __name__ == '__main__':
    main()
    
