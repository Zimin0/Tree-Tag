# Application "menu_app"  
The menu_app is made to show a "tree-like menu". Each level of the menu goes a bit to the right, like this:
```
Point0
----Point1.1
----Point1
--------Point2
```
To do this, we used nested </ul/> tags. So, we chose a recursive way to show the menu.

## Recursive Approach
We didn't use the ready unordered_list filter. We made our own way to match the project needs. We used two templates to show the menu in a recursive way.

## Testing with test_pages_app
We also made a test_pages_app to check how the menu looks. This helps to test one, many, and nested pages to make sure the menu shows right.

This way, the menu shows the hierarchy nicely and is easy to test in different situations.
