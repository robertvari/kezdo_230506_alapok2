movie_list = {
    1: {"title": "The Princess", "rating": 26},
    2: {"title": "Spider-Man: No Way Home", "rating": 81},
    3: {"title": "Morbius", "rating": 64},
    4: {"title": "The Northman", "rating": 72},
    5: {"title": "Troll", "rating": 67},
    6: {"title": "Avatar", "rating": 76},
    7: {"title": "The Woman King", "rating": 79}
}

sorted_by_rating = sorted(movie_list, key=lambda movie_id: movie_list[movie_id]["rating"], reverse=True)
for movie_id in sorted_by_rating:
    print(movie_list[movie_id])