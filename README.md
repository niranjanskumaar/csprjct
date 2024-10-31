# Canteen Management App - Computer Science Boards Project

### Submitted by Gautham Krishna, Vivek Purushothaman and Niranjan S K

This is a menu-driven canteen management app. 

Database is handled using the `pickle` module. The data files can be found in the [`./data`]("https://github.com/niranjanskumaar/csprjct/tree/main/data") directory.

\
There are 3 different permission levels:

- Student
- Staff
- Administrator


### Student

Upon logging in, you are able to see the **booking status** as well as the **account balance**

A "Student" user has 3 available functions.

- **Book Coupon:** Books a coupon if not booked already. Also reduces ₹45 from account balance. *(Balance must be atleast ₹45 or above)*

- **Add funds:** Adds specified amount of funds to the account.
- **Logout:** Logs out of the account.

### Administrator

> [!TIP] 
> Username: admin

> Password: admin


