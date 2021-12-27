# my_first_Django_website

from django.http import HttpResponse

def bookmark(request):
    a = '''<h2>Navigation Bar<h2> 
    <a href="https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">
    Django Playlist CodeWithHarry</a><br>
    <hr/>
    <a href="https://www.pankajshuklaonline.com/s/mycourses"> Yoga</a><br>
    <hr/>
    <a href = "https://www.w3schools.com/python/python_iterators.asp">Learn Python</a><br>
    <hr/>
    <a href = "https://courses.conduiraonline.com/courses/course-overview/65163/65164">Conduira</a><br>
    <hr/>
    <a href = "https://www.youtube.com/playlist?list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME">Python Playlist CodeWithHarry</a>'''
    return HttpResponse(a)
