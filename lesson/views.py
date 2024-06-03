from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    contents = [
        {
            "title": "Learning Content",
            "href": "/learning_content",
            "thumbnail": "welcome-box-1.jpg",
            "description": "The specialised section containing content which accommodates knowledge base for all activities.",
        },
        {
            "title": "Program Implementation",
            "href": "/implementation",
            "thumbnail": "welcome-box-2.jpg",
            "description": "Source code for Digital Image Processing and Tic-tac-toe program is visually demonstrated.",
        },
        {
            "title": "PDF Viewer",
            "href": "/pdf_viewer",
            "thumbnail": "welcome-box-3.jpg",
            "description": "A portable feature that provide assistance to users through displaying lesson representation.",
        },
    ]
    return render(request, "index.html", {"contents": contents})


def learning_content(request):
    contents = [
        {
            "h2": "Digital Image Processing (DIP)",
            "h3": [
                {
                    "title": "Overview",
                    "paragraphs": [
                        "Digital image is a presentation of a common image that is stored and processed by a digital machine through an algorithm. By default, every digital image is combined from a number of indivisible elements. These elements are called pixels. In other words, a pixel is a smallest unit that establishes a digital image.",
                        "In programming, a digital image is stored as a two-dimensional array arranged in rows and columns. Every pixel in a digital image has its own (x, y) coordinate. These coordinates describe the intensity at the location that each pixel resides in.",
                    ],
                    "media": {
                        "file_name": "grayscale-image-example.png",
                        "description": "How the digital image is converted into a two-dimensional array",
                    },
                },
                {
                    "title": "Types of digital images",
                    "paragraphs": [
                        "Typically, there are three types of digital images which are binary image, grayscale image and RGB image. In common grayscale images, each pixel expresses its gray level in a total of 256 different levels of gray levels. The accepted values of gray level vary from 0 to 255. At the top and bottom boundaries, a pixel intensity of 0 represents the black color and pixel intensity of 255 describes the white color. Other between values demonstrates how the light intensity fluctuates linearly."
                    ],
                    "media": {
                        "file_name": "dip.png",
                        "description": "Convert digital image into two-dimensional array by using Python",
                    },
                },
                {
                    "title": "Digital images in Python",
                    "paragraphs": [
                        "By using Python, programmers could easily extract a specific digital image into a two-dimensional array. Additionally, there are some built-in features that Python helps developers to show the image as per demand."
                    ],
                },
            ],
            "description": "The specialised section containing content which accommodates knowledge base for all activities.",
        },
        {
            "h2": "Tic-tac-toe",
            "h3": [
                {
                    "title": "Specifications",
                    "paragraphs": [
                        "In this program, two people act as two users participating in a debate. One user plays “X” and another user plays “Y”. They mark their respective symbols in turn on a grid of three-by-three cells. In every turn, users enter their row and column location in order to mark their own choice.",
                        "The program terminates whenever 9 turns are passed. The board is displayed after every turn. Every user needs to make sure that their selection satisfies two requirements:",
                        "1) Their row and column index are an integer less than or equal to 2.",
                        "2) The selected location is not marked beforehand by any users.",
                    ],
                },
                {
                    "title": "Flowchart",
                    "paragraphs": [],
                    "media": {
                        "file_name": "tic-tac-toe-flowchart.png",
                        "description": "Flowchart for tic-tac-toe program",
                    },
                },
                {
                    "title": "Implementation",
                    "paragraphs": [],
                    "media": {
                        "file_name": "tic-tac-toe-code.png",
                        "description": "Tic-tac-toe program implementation",
                    },
                },
            ],
            "description": "The specialised section containing content which accommodates knowledge base for all activities.",
        },
        {
            "h2": "Number of Islands",
            "h3": [
                {
                    "title": "Specifications",
                    "paragraphs": [
                        "Given a two-dimensional array which was filled by two specified values: 0 and 1. Value 0 represents water and value 1 describes land. An island is defined by the maximum numbers of connected cells with value 1. All islands are surrounded by water (which is value 0)."
                    ],
                },
                {
                    "title": "Flowchart",
                    "paragraphs": [],
                    "media": {
                        "file_name": "number-of-islands.png",
                        "description": "Flowchart for tic-tac-toe program",
                    },
                },
            ],
            "description": "The specialised section containing content which accommodates knowledge base for all activities.",
        },
    ]
    return render(request, "learning_content.html", {"contents": contents})


def implementation(request):
    template = loader.get_template("implementation.html")
    return HttpResponse(template.render())


def pdf_viewer(request):
    template = loader.get_template("pdf_viewer.html")
    return HttpResponse(template.render())
