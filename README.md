# CS50_CAPSTONE
Design a site where truckers can get loads online and shippers can post their loads
![](posts.png)
### Distinctiveness and Complexity
 The LoadMaster WebApp is a online loadboard platform to
connect shippers, brokers, and carriers to find loads for transporting freight. Shippers and brokers can post available loads and carriers can view load listings, book a load, cancel booking within 24hrs, change status to delivered 
- the Project has two apps, main and loads
    1. the main app takes care of user profiles and home screen 
        - main app has User and Profile models
    2. The loads app is for location and load listings, details, updates and deletion
        - loads app has 3 models, Location, Load and LoadStatus

### Specification
<hr>
Using Python, JavaScript, HTML, and CSS, complete the implementation of a webapp that allows user to post available loads, book a load, cancel booking within 24hrs, change status to delivered

- **main:home:** A home screen with a welcome page. Unauthenticated users can see the latest 5 listings without rates and shipper contact information
- **main:login:** Existing users can login with username and password or third party Google credentials 
- **main:signup:** A new profile is automatically created for all newly signed user. Users can optionally sign up using third party Google authentication 
- **main:incomplete_profile** all new users are automatically directed to this page to complete their profile giving more company details.
- **main:profile:** Authenticated users can view their profile page with user details: organisation, phone number, email and image 
- **main:update_profile** SExisting profile can update personal information - organisation, phone number, image, email 
- **loads:loads:** Users who are signed in should be able to see all load listings with <span style="color:green;">"Available"</span> status
- **loads:new_load:** Signed in users can post new loads and add a <span style="color: green">new location</span> if the location they need is not listed in <span style="color:orange">origin</span> and <span style="color:orange">destination</span> fields
- **loads:load_detail:** 
    - Signed in users can view shipper information and load details
    - if loadStatus is <span style="color:green;">Available</span>, users other than owner that posted the load, can book the load for shipping, in which case the loadStatus is changed to <span style="color:green">"In Transit"</span>
    - Once loadStatus is <span style="color:green">"In Transit"</span> the user can ship the load and change loadStatus to <span style="color:green">"Delivered"</span> Delivered. 
    - NB: The user can only cancel <span style="color:green">"In Transit"</span> or booked loads within 24 hours while owner can unbook the load and change loadStatus to <span style="color:green">"Available"</span> at any time
    - Clicking on "more loads from shipper" button takes user to load listings from the shipper
- **loads:load_update:** Owner can update any load they posted 
- **loads:my_bookings** Users see all the loads that they booked and are "In <span style="color:green">Transit"</span> and <span style="color:green">"Delivered"</span>. Clicking any load listed will take then to load_details
- **loads:my_loads** Users can view all the loads they have posted. Clicking a specific load will take them to load_detail page. 
- **loads:shipper_details**  

- **All Posts:** The “All Posts” link in the navigation bar should take the user to a page where they can see all posts from all users, with the most recent posts first.
    - Each post should include the username of the poster, the post content itself, the date and time at which the post was made, and the number of “likes” the post has (this will be 0 for all posts until you implement the ability to “like” a post later).
    
- **Profile Page** Clicking on a username should load that user’s profile page. This page should:
    - Display the number of followers the user has, as well as the number of people that the user follows.
    - Display all of the posts for that user, in reverse chronological order.
    - For any other user who is signed in, this page should also display a “Follow” or “Unfollow” button that will let the current user toggle whether or not they are following this user’s posts. Note that this only applies to any “other” user: a user should not be able to follow themselves.

- **Following** The “Following” link in the navigation bar should take the user to a page where they see all posts made by users that the current user follows.
    - This page should behave just as the “All Posts” page does, just with a more limited set of posts.
    - This page should only be available to users who are signed in.

-**Pagination:** On any page that displays posts, posts should only be displayed 10 on a page. If there are more than ten posts, a “Next” button should appear to take the user to the next page of posts (which should be older than the current page of posts). If not on the first page, a “Previous” button should appear to take the user to the previous page of posts as well.

-**Edit Post:** Users should be able to click an “Edit” button or link on any of their own posts to edit that post.
   - when a user clicks “Edit” for one of their own posts, the content of their post should be replaced with a textarea where the user can edit the content of their post.
   - The user should then be able to “Save” the edited post. Using JavaScript, you should be able to achieve this without requiring a reload of the entire page.
   - For security, ensure that your application is designed such that it is not possible for a user, via any route, to edit another user’s posts.

-**"Like" and "Unlike":** Users should be able to click a button or link on any post to toggle whether or not they “like” that post.
- Using JavaScript, you should asynchronously let the server know to update the like count (as via a call to fetch) and then update the post’s like count displayed on the page, without requiring a reload of the entire page.


## Built With

- Django, Python, Javascript
- Bootstrap 
- HTML 5
- CSS3
## YouTube Demo

[Video_Link](https://www.youtube.com/watch?v=K4dIeBbyRIc)

## Author

👤 **Author**

[https://github.com/ggotora](https://github.com/ggotora)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

Feel free to check the [issues page](https://github.com/ggotora/CS50-Project4/issues/1).

## Show your support

Give a ⭐️ if you like this project!

# 📝 License

This project is [MIT](LICENSE) licensed.