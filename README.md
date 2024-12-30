# CS50_CAPSTONE
Design a site where carriers can get loads online and shippers/brokers can post their loads
![](home.png)
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
Using Python, JavaScript, HTML, and CSS, a webapp that allows user to post available loads, book a load, cancel booking within 24hrs, change status to delivered

- **main:home:** A home screen with a welcome page. Unauthenticated users can see the latest 5 listings without rates and shipper contact information
- **main:login:** Existing users can login with username and password or third party Google credentials 
- **main:signup:** A new profile is automatically created for all newly signed user. Users can optionally sign up using third party Google authentication 
- **main:incomplete_profile** all new users are automatically directed to this page to complete their profile giving more company details.
- **main:profile:** Authenticated users can view their profile page with user details: organisation, phone number, email and image 
- **main:update_profile** SExisting profile can update personal information - organisation, phone number, image, email 
- **loads:loads:** Users who are signed in should be able to see all load listings with <span style="color:green;">"Available"</span> status
    - users can see filtered results for load of type <spam style="color:orange"> "All", "Flatbed", "Reefer", "Van" or "Other" </span>
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
- **loads:shipper_details** User can see a list of loads posted by a specific shipper/broker  
<hr>

## Installation 

Run the following commands 

```bash
$  git clone git@github.com:ggotora/cs50_Capstone.git
$ cd cs50_Capstone  
$  pip install -r requirements.txt
$ python manage.py runserver
```
<hr>
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

Feel free to check the [issues page]
(https://github.com/ggotora/cs50_Capstone/issues/1)


## Show your support

Give a ⭐️ if you like this project!

# 📝 License

This project is [MIT](LICENSE) licensed.