# Megan's Online Cookbook

The brief for this project is to make an online cookbook that users can easily store and access recipes. The logic must be written in Python, HTML, CSS and Javascript.
I decided to use the mLab database for this project as i am familiar with the database. I have also used Materialize, Bootsrap and Font Awesome for the design off the webpage.
I did a lot of research on online cookbooks and found a range of different themes and styles i could use which fit in with the theme i am trying to create. I eventually
decided to keep the cookbook simple and easy to navigate. I thought this was a good idea so the user doesn't get confused on how to navigate and then decide to leave the page. I decided 
to use a drop down on the nav bar so the user can navigate fromone section to the other easily. I also added a search bar so the user could search for a recipe by ingredients.
I thought it would be a good idea to use a colour scheme from the internet for this website. I decided on a pale background with bold colours in the foreground. I thought this 
would make it clear but also attract users to visit the site. I went for a straight forward name for the website so users would rememeber it or rememeber the logo. I created
the logo online on one of the online free logo makers. When i was first planning the website design, i decided it would be a good idea to use a standard footer and a navbar. 
I felt like this would make the navigation of the site easy and visually pleasing. The main thing that i wanted to include in the site are images for each recipe and for the
user to have the ability to add and change the images for each recipe. I have used several pages in this website such as the homepage, edit recipe, add recipe, show recipes and
sections. You can access all the pages from the homepage. I have used the same colours, font and buttons throughout the website. However the logo font is different as the website
did not support the font i decided on for the website. Overall i am happy with the layout and design off the website. I also think the documents i created in the database fit the
brief of the project and navigation of the page is easy to use. 

## UX

This website is for people who can't decide what to cook for tea, or someone who want's to try something new. My target audience would range from 18-70 years, all genders. I have
aimed the audience at adults as most of these recipes will need adult supervision if a child was cooking the recipe. I think some of the online cookbook's functions will be used
regulary. Such as the search bar as it only brings up recipes that include the ingredients the user has searched for. This is also quite a quick process, and the search will bring
the recipes up clearly with the option to edit the recipe. I also think the section pages on the navbar are going to be used a lot as they divide all recipes into their sections.
So you can search by section as well which makes navigation easy for the user. I realise some of the users will just want to browse the website for new recipes to try so i thought
having a button on the homepage which leads to a list of all recipes is quite handy for browsing users. I have created some user stories before hand to understand what some of the
actions are that users may want to take. 

*	As a user I want to be able to see only the salad recipes.
*	As a user I want to be able to search recipes by ingredients.
*	As a user I want to be able to see a list of all recipes.
*	As a user I want to be able to edit a recipe.
*	As a user I want to be able to add a recipe to the website.
*	As a user I want to see all ingredients for a recipe.
*	As a user I want to know the cooking time for each recipe.
*	As a user I want to be able to rate the recipe.
*	As a user I want to be able to check if the recipe has allergens.

With me creating the user stories, i was able to know quite quickly what i needed in the website and what users expected to see. Researchng other online cookbooks also helped me 
understand how to navigate the site. I knew i needed it to be simple and obvious how to navigate so i used buttons with text(e.g.'Home' and 'Show Recipes'). I also realised how
important it is to have details about allergies on each recipe, the recipe may not have any allergens but it is useful to have 'no allergies' stated if there is none. I also
created some wireframes for each page so i knew the content i needed on each page. This also helped me design each page and make them fit together. 

## Features

On the home page the user has the ability to search for a recipe by its ingredients. The user just needs to input the ingredient in to the search bar and press search. This will
then bring up all recipes that have that ingredient. I have a sections dropdown on the nav bar, which gives you a list of 6 pages, each page is a section. This way the user can easily
choose a recipe type and see what recipes are in that section. I have also used a knife and fork icon on the top right of the nav bar so the user can easily return to the homepage either
using the home button or the knife and fork icon. I have also added the page 'Add Recipe' to the nav bar so the user can easily add recipes themselves. The nav bar is always on each page
so you will be able to click on the add recipe page at any point during accessing the site. I added an image for each recipe as i thought the users would prefer to look at an image of the
meal instead of imagining it. The images also make the site more vibrant and modern. I decided to use an edit button when you actually click into the recipe so the user has the ability
to change the recipe or even add a different image for the recipe. One of the features i decided to use was the drop down select feature, i used this in the add recipe page and edit recipe 
page. On both these pages i have used it to choose a section. This way the user can easily pick between the 6 sections and not have any odd recipes not in a section. This is also there for
edit recipe however when you are on edit recipe, the section is already inputted from MLAB. This way the user doesn't have to enter a section, however the user can change the section name
by just changing the selected option in the dropdown. I used Django and materialize to make the forms, so i did not have to hard code everything. Django was used to get the documents printed
on the website. Every part of the recipe has an id in MLAB, so i was able to use Django to get all recipe names and ingredients etc on each part of the form. For example, writting {{recipe.sectionname}} 
in my code would show 'Salads' on the website instead off 'sectionname'. One of the features i added was a star rating to each recipe. This allowed to user to see how others have rated the
recipe, as well as having the option to change the rating or adding a rating when adding a new recipe. One of the final features i added to this project is the 'recipe of the week', i had a
lot of empty space on my homepage which was making the footer rise up. I did not liek the way the footer was not stuck to the bottom of the page so i decided to make a recipe of the week section where
me as the adminstartor would change the recipe of the week weekly. This is a just an extra design feature to attract more users top my website. I also thought it was a good idea to add icons
next to each input or checkbox fields to add a little more design to the pages as most of the website is data presented differently.




## Features Left to Implement

* I have thought about adding a log in option for the user so the user can create an account and save recipes etc...
* I have thought about making the search bar more in depth and to be able to search by cuisine, cooking time and star ratings.
* I could also add more sections which would mean more recipes to choose from.
* I could also add more details about each recipe such as cuisine, instructions on how to cook the recipe, nutrition and preparation time.


## Technologies Used

* HTML
* CSS - this is used for styling the website
* Django



* JavaScript



* Heroku

https://www.heroku.com/

* Materialize

https://materializecss.com/
    
    
* Font Awesome



* Bootsrap

https://getbootstrap.com/

* MLAB - this is used as the database in this project.

https://mlab.com/welcome/




## Testing



### Add a recipe

1.	When on the homepage, click the ‘Add Recipe’ button on the navbar.
2.	Once on the add recipe page, fill in the form and click the ‘Add Recipe’ Button at the bottom of the form.
3.	Now go to the home page, click ‘Show Recipes’ and look for the recipe that you just added in the all recipes list.
4.	Check all inputted information is shown including the image of the recipe.

1.	When on the homepage, click the ‘Add Recipe’ button on the navbar.
2.	Once on the add recipe page, do not fill in the form and click the ‘Add Recipe’ button at the bottom of the form.
3.	Verify the ‘required fields’ alert pops up. 
4.	Now enter all correct information but in the ingredients input, input an integer not a string and verify an ‘error’ message appears and does not let you submit the form.

1.	When on the ‘Add Recipe’ page, enter all inputs correctly but leave the ‘star rating’ input on ‘0’. 
2.	Press the ‘Save Changes’ button and verify the star ratings is what you entered. 
3.	Verify all fields have correct inputs.

1.	When on the ‘Add Recipe’ page, click on the ‘section name’ drop down and choose a section name.
2.	Enter all information in the form correctly and click the ‘Add Recipe’ button at the bottom of the form. 
3.	Verify the drop down has worked and the recipe is now showing the section name you choose. 

1.	When adding a recipe on the ‘Add Recipe’ page, click the tick box to say this recipe has allergies. 
2.	Once all information is entered correctly, click the ‘Add Recipe’ button.
3.	Verify this redirects you to add another recipe.
4.	Now go to the homepage and click the ‘Show Recipes’ button. 
5.	Verify this redirects you to the ‘All Recipes’ Page.
6.	Find the recipe you have just added and verify ‘the recipe has allergies’ is noted.

1.	When adding an image to the recipe you are adding on the ‘Add Recipe’ page, you need to copy the image’s URL from the internet and paste it into the ‘IMGURL’ section.
2.	Once all information is correct, press the ‘Add Recipe’ button. 
3.	Verify this has now redirected you to add another a recipe.
4.	Click on the homepage, then the ‘Show Recipes’ button.
5.	Verify the recipe you have just added is there, along with the image you attached to the recipe.

### Edit a recipe

1.	When on the homepage, click on the ‘Show Recipes’ button under the home image.
2.	Once the button has been clicked, you should be redirected to the ‘All Recipes’ page. 
3.	Verify there is a list of different recipes.
4.	Verify you can click on each recipe and see all the recipe details.
5.	Click on the ‘Edit Recipe’ button and verify you can now edit the recipe.
6.	Change one of the input fields and press the ‘Save Changes’ button.
7.	Verify the recipe has now been changed.

1.	When on the ‘All Recipes’ page, click on a recipe and click the ‘Edit Recipe’ button.
2.	On the ‘Section Name’ part of the edit recipe form, change the drop down to a different section name and press the ‘Save Changes’ button. 
3.	On the navbar, click on the ‘Sections’ drop down and click on the section name you just changed the recipe to.
4.	Verify this has redirected you to the specific section page.
5.	Now Verify the recipe you just edited is listed.

### Search by ingredients

1.	When on the homepage, enter an ingredient in to the search bar and press the search button. (e.g. ‘Meat’)
2.	Once pressed search, check you have a lists of results.
3.  Once the list of results are showing, check all recipes have the ingredient in them.
4.	Verify there is no recipes listed that do not include ‘Meat’.

1.	When on the homepage, enter an integer in to the search bar and click the search button.
2.	Once the search button has been clicked, verify an error message has now appeared.
3.	Verify no results of recipes are showing.

1.	When on the homepage, enter a string which is not an ingredient in to the search bar and then click the search button. (e.g. ‘Cat’)
2.	Once pressed the search button, verify an error message has now appeared.
3.	Verify no results of recipes are showing.

1.	When on the homepage, enter several ingredients into the search bar and press the search button. (e.g. ‘Meat Fish Pepper Onions’)
2.	Once pressed the search button, verify all recipes that include the searched ingredients are listed below.
3.	Verify no recipes are showing that do not include one of the ingredients searched.

### Navigating through the dropdown section on the navbar

1.	When on the homepage, click on the ‘Sections’ drop down and select one section.
2.	Verify this has redirected you to the specific section page. 
3.	Verify all recipes are ‘Meat and Poultry’ in the ‘Meat and Poultry’ section.
4.	Click on each section in the drop down and verify for each.
5.	Verify there are no recipes in the wrong sections.

### Buttons

1.	Click on the ‘Show Recipes’ button on the ‘Homepage’.
2.	Verify it redirects you to the ‘All Recipes’ page.

1.	Once entered all correct information click on the ‘Add Recipe’ button on the ‘Add Recipes’ page.
2.	Verify it adds the recipe to the website.

1.	Input an ingredient into the search bar and click on the search button on the ‘Homepage’.
2.	Verify it searches the website for the recipes including the ingredient you searched for and displays the recipes in another screen.

1.	Once entered all correct information, click on the ‘Edit Recipe’ button on the ‘Edit Recipe’ page.
2.	Verify the recipe has been updated with the new information.

1.	On the right side of the navbar, there is the home button which is the knife and fork icon. When on a different page, click on the homepage button.
2.	Verify this redirects you to the homepage.

### Responsiveness

#### Bugs/Errors

One of the main issues i am having at the minute is not being able to add CSS to some of the materialize forms. There is a default colour on materialize and it comes up when you hover over parts of the
form. I want to sort this out so the hover colours are not the default colours. The colours should be one of the colours from the colour scheme i choose for the website. I also want to change the font of
some of the text on the form as some of it i have designed with CSS but again i am struggling to change it due to the materialize defaults.

One of the other design issues i am having is the margins of the forms on the 'all recipes' page. I had all the text in the center, on one line but for some reason they have moved to the side slightly. 
This is something i will be fixing before submitting.

On the 'Edit Recipe' and 'Add Recipe' pages, i use a dropdown in the form for the section name. On the 'Edit Recipe' page, when clicking on the dropdown it does not work, also there is no text in the text box
of the dropdown. This needs fixing before submitting so the user has the option to keep the section name for the recipe or choose a different section from the dropdown.

At the moment the search button does not work. The search bar does not redirect you to a results page.


## Deployment

## Credits

* Images and URL's came from Google Images
* 