## Testing Checkout
***
### Adding items to the bag
1. Click 'shop now' or through the drop menu on Products.
2. Click 'view details' from desired product.
3. Use input bar or icons to add or decrease quanity and when ready click 'add to bag.'
4. An alert will pop up confirming items have been added.
5. Click on the basket at the top when ready to checkout.
6. Whilst on the basket page, users can increment or decrement using the icons, then clicking 'update' to update the total. Or users can click remove to remove the item from the basket. The subtotal will calculate automatically.
7. Delivery is calculated automatically.

    * RESULT: PASS

### Checking out (new user).
1. Click 'secure checkout.'
2. Fill out the delivery details.
3. Users have the option to login or register an account to save their personal details.
4. Use '4242 4242 4242 4242' as the card number, '04/24' as the expiry and '242' as the CVC and '42424' as the ZIP code. (Note these are test figures and the everything after the card number and expiry date can be any digits. Please ensure to use an expiry date from the past.)
5. If the user's card details are wrong - the input bar will flag red with a message of the card number invalid.
6. Once ready - click 'complete order' with a message just below confirming amount to be charged.

    * RESULT: PASS

### Checking out (registered user).
1. Login to the account thats already registered.
2. Add items to the bag and continue to checkout.
3. Upon reaching the checkout page - users will have theie details prefilled (if saved from a prior purchase) - except adding a name.
4. Card details are to be entered.

    * RESULT: PASS

### Background processes using webhooks
1. Using webhooks - payment intents, charges created and charges succeeding will occur in the Stripe account. These will work in co-ordination with the website to ensure an order is created either through the website or in case of any failure - through the webhook handler.

    * RESULT: PASS

### Checkout success
1. On successful checkout the user will have an order created in the admin panel aswell as a confirmation notice to the user both on the site interfact and through email.
2. Registered users will also have the addition of the order being added to their order history in their own profile.

    * RESULT: PASS