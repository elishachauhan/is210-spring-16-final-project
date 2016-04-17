==============
PriceLife
==============

PriceLife is an program that seeks to match customer purchases to inventory 
that are in other stores. This is useful for retail stores in clothing, electronics, and 
other merchandise. 

Personas
========

Elene the Shopper
---------------------------------

Details
^^^^^^^

Elene the Shopper seeks to find the best deals on clothing items while shopping
in various areas of NYC. She is a 23-year old student that lives in Brooklyn. She is 
a new RN after taking her NCLEX exam.  She is an exuberant shopper that shops 
with friends and family every weekend in NYC. She browses many stores and gets 
confused on whether or not to buy certain items because the prices may drop at a 
later time.

Goals
^^^^^

Consumed by NYC life, Elene the Shopper wants to maximize her budget and be 
alerted when an item she bought went down in price or is found at a lower price 
elsewhere. Price is an important for Elene to strech her dollar to the fullest. Since
she is limited in time, she doesn't want to waste time researching items and 
finding which stores have the lower price.

Problem Scenarios
=================

Elene the Shopper's Dilemma
----------------------------------------------------

After a day of shopping one day, she realizes that she could have got an item
she bought at a cheaper price. Frustrated with her current lack of information,
she wants to know when an item's price drops or is found at a lower price 
elsewhere.

Current Alternatives
^^^^^^^^^^^^^^^^^^^^

Current alternatives include researching the items on Google, emails that
retailers send if they find similar items that you bought, etc. 

Value Proposition
^^^^^^^^^^^^^^^^^

An alert that detects items from purchase history from retailers and
relays price drop information in a instantaneous and cohesive manner.

User Stories
============

Elene the Shopper's Story
------------------------------------------------------------

As Elene the Shopper, I want to distribute customer information 
to other retailers so that I can alert customers on price drops and price
differences on items that they have purchased.

Acceptance Stories
^^^^^^^^^^^^^^^^^^

Database and Price Drop 
`````````````````````````````

::

    Scenario 01: Giving Information to Customers
    Given that a database is created with name of product, prices, and
    description,
        And the products are keyed and indexed in a dictionary,
	And the customer information is also keyed and indexed to 
	products bought,
    When I update this database on a frequent basis
    Then I can establish a reputable source for customers and retailers
        And give customers accurate data on products from specific retailers.
    
    Scenario 02: Alerting Customers on Price Drops
    Given that I selected products that are easily accessible through a search
    aggregation,
        And the products have data such as price, price drop, retailer, and 
	availabiliy,
	And I can sort, store, and pull up this information from a database,
    When I compare prices between retailers
    Then I can provide information to customers that want to save money on
    on a specific item, product, or service
        And alert customers when the price is lower than the price at the time of
	sale.