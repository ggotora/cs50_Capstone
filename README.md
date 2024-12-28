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

- **Main:Profile:** A new profile is automatically created for all new user. Users can sign in or sign up using third party Google authentication 
- **Main:incomplete_profile** all new users are asked to complete their profile giving their company details. 
- **Main:update_profile** Existing profile can update personal information - organisation, phone number, image 
- **New Load:** Users who are signed in should be able to post a new load 
- **Edit load:** Only the user that created the load is able to edit the load 
- **Book load:** Users either than owner can book a load for shipping 
- **Cancel booking:** Users can cancel booking within 24hrs 
- **Mark load delivered:** Users can mark load as delivered once shipment is done 

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