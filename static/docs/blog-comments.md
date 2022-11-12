## Testing Checkout
***
### Adding a blogpost (admin functionality only)
1. Log in as a superuser
2. Click on the blog page.
3. Click the 'create post' button (only visible to superusers)
4. Fill in the form and click add post. (Note the content box isn't configured for any styling - content will be a paragraph without any spacing. This feature will be added in the future.)
5. Once added, the user will be routed back to the main blog page.
6. Note the name of the superusers username and the date will automatically be added by virtue of being logged in as one.

    * RESULT: PASS

### Editing a blogpost (admin functionality only).
1. Click on the intended blogpost using the 'read more' button.
2. The superuser will be guided to an editing page.
3. The form is pre-filled to be replaced with the new input.
4. Click 'update post' when ready.
5. Users will be routed back to the said blogpost.
6. A success message alert will pop up.
7. Note upon editing - the current functionality does not allow for the date to be altered, nor can it differentiate who it is edited by in the event of more than one superuser (this is a known limitation and is to be added in the future).

    * RESULT: PASS

### Deleting a blogpost (admin functionality only).
1. 
2. 

    * RESULT: PASS

### Adding a comment (all registered users)
1. Log in to a registered account.
2. Click on the intended blogpost using the 'read more' button.
3. Click on the 'add comment' button (only visible for users logged in otherwise will prompt them to login to add a comment)
4. Fill in the comment section.
5. The comment will automatically attach to - and route the user back to - the originating post.

    * RESULT: PASS

### Editing a comment (only available to the original comment author)
1. Log in to a registered account.
2. Click on the intended blogpost using the 'read more' button.
3. Click on the 'edit comment' button (only visible for the original comment author).
4. Fill in the prefilled comment section and click 'update.'
5. The comment will automatically attach to the originating post however will route the user back to main blog as opposed to the post. This is a known bug and will be handled in the future.

    * RESULT: PASS

### Deleting a comment (only available to the original comment author and admin).
1. 
2. 

    * RESULT: PASS

#### Defence testing scenarios.
1. Logged out user types in the adding, updating or deleting urls.
    * RESULT: 