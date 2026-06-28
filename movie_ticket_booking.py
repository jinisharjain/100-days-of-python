movies = {
    "Avengers": 50,
    "Interstellar": 30,
    "Inception": 40,
    "Jawan": 60
}
bookings = {}

def view_movies(movies):
    print(movies)

def book_tickets(movies):
    mov = input("Enter movie name : ")
    if mov in movies:
        num = int(input("Enter number of tickets : "))
        if num <= movies[mov]:
           movies[mov] = movies[mov] - num
           if mov in bookings:
              bookings[mov] += num
           else:
              bookings[mov] = num
        else:
            print("Not enough seats available!")
    else:
        print("Movie not found")
    return movies, bookings

def cancel_tickets(movies):
    mov = input("Enter movie name : ")
    if mov in movies:
        if mov in bookings:
            num = int(input("Enter number of tickets : "))
            bookings[mov] = bookings[mov] - num
            movies[mov] = movies[mov] + num
        else:
            print("No tickets booked before!")
    else:
        print("Movie not found")
    return movies, bookings

def view_bookings(bookings):
    print(bookings)

print("---Movie Ticket Booking System---")
print("1. View Tickets")
print("2. Book Tickets")
print("3. Cancel Tickets")
print("4. View Bookings")
print("5. Exit")

while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        view_movies(movies)
    elif choice == 2:
        movies, bookings = book_tickets(movies)
    elif choice == 3:
        movies, bookings = cancel_tickets(movies)
    elif choice == 4:
        view_bookings(bookings)
    elif choice == 5:
        print("Thank you for using this program")
        break
