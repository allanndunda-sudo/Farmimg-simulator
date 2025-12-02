FARMING SIMULATOR

Date 2025/2/12

By Allan Muuo


Proposed Solution
The Farm Simulator CLI provides a simple command-line interface that allows farmers or users to:
Register animals with details such as name, gender, and category
Assign feeds and products to animals
Store all farm data in a database with proper relationships, including many-to-many relationships (e.g., an animal can eat multiple feeds and produce multiple products).
Interact with the system through commands, without needing a graphical interface.
Expected User Outcome
After using the Farm Simulator CLI, the user will be able to:
Quickly register and categorize animals on the farm.
Track what each animal eats and the products it produces.
Generate organized lists of animals, feeds, and products.
Maintain a digital farm record that is easy to update and query.




Animal Registration
Users can register a new animal by specifying:
Animal name
Category (e.g., Cow, Goat, Chicken, etc.)
Gender (Male / Female)
Feed type (e.g., Grass, Maize, Commercial Feed)
Products produced (e.g., Milk, Eggs, Wool)


Database-Backed
All data is stored in a relational database with:
Animals table
Categories table
Feed types table
Products table
Many-to-many tables where needed (e.g., animals ↔ products)
Tech Stack
SQL Lite with SQL Alchemy
Python
Click for CLI commands
Pipenv for environment variables
