<body>

<h1>Welcome to My Inventory Management System API!</h1>

<p>This is a simple API built using Django Rest Framework. It helps manage inventory items and includes user registration and login features. Below is a guide on how to set it up and use it.</p>

<h2>Setting Up the Project</h2>

<h3>What You Need:</h3>
<ul>
    <li>Python 3.8 or later</li>
    <li>MySQL database</li>
    <li>Redis for caching</li>
</ul>

<h3>Installation Steps:</h3>
<ol>
    <li><strong>Clone the Repository:</strong>
        <pre><code>https://github.com/Devesh-More/inventoty-management.git</code></pre>
    </li>
    <li><strong>Navigate into the Project Directory:</strong>
        <pre><code>cd inventory-management</code></pre>
    </li>
    <li><strong>Create a Virtual Environment:</strong>
        <pre><code>python -m venv venv</code></pre>
    </li>
    <li><strong>Activate the Virtual Environment:</strong></li>
    <ul>
        <li>On macOS/Linux:
            <pre><code>source venv/bin/activate</code></pre>
        </li>
        <li>On Windows:
            <pre><code>venv\Scripts\activate</code></pre>
        </li>
    </ul>
    <li><strong>Install the Required Packages:</strong>
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li><strong>Set Up Database:</strong></li>
    <ul>
        <li>Create a database in MySQL and note the credentials.</li>
        <li>Create a file named <code>.env</code> and add the following details:
            <pre><code>
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=3306
            </code></pre>
        </li>
    </ul>
    <li><strong>Run Migrations:</strong>
        <pre><code>python manage.py makemigrations</code></pre>
        <pre><code>python manage.py migrate</code></pre>
    </li>
    <li><strong>Start the Server:</strong>
        <pre><code>python manage.py runserver</code></pre>
    </li>
</ol>

<h2>Configuring Redis</h2>
<p>Make sure Redis is installed and running. You can install Redis using the following:</p>
<ul>
    <li>For macOS:
        <pre><code>brew install redis</code></pre>
    </li>
    <li>For Ubuntu:
        <pre><code>sudo apt-get install redis-server</code></pre>
    </li>
    <li>For Windows:
        Download from <a href="https://github.com/microsoftarchive/redis/releases">Redis for Windows</a>.</li>
</ul>
<p>To start Redis, just run:</p>
<pre><code>redis-server</code></pre>

<h2>User Authentication</h2>
<p>You need to register a user first to use the other features.</p>

<h3>Register a User</h3>
<p>Endpoint: <code>/inventory/register/</code></p>
<p>Method: <code>POST</code></p>
<p>Request Body:</p>
<pre><code>
{
    "username": "your_username",
    "password": "your_password"
}
</code></pre>
<p>Success Response:</p>
<pre><code>
{
    "status": true,
    "message": "User Registered Successfully."
}
</code></pre>

<h3>Login</h3>
<p>Endpoint: <code>/inventory/login/</code></p>
<p>Method: <code>POST</code></p>
<p>Request Body:</p>
<pre><code>
{
    "username": "your_username",
    "password": "your_password"
}
</code></pre>
<p>Success Response:</p>
<pre><code>
{
    "status": true,
    "refresh": "your_refresh_token",
    "access": "your_access_token",
    "message": "Login Successful"
}
</code></pre>
<p>Use the access token for subsequent requests:</p>
<pre><code>Authorization: Bearer your_access_token</code></pre>

<h2>CRUD Operations for Inventory Items</h2>

<h3>Create an Item</h3>
<p>Endpoint: <code>/inventory/items/</code></p>
<p>Method: <code>POST</code></p>
<p>Request Body:</p>
<pre><code>
{
    "name": "New Item",
    "description": "Description of the item"
}
</code></pre>
<p>Success Response:</p>
<pre><code>
{
    "status": true,
    "message": {
        "id": 1,
        "name": "New Item",
        "description": "Description of the item"
    }
}
</code></pre>

<h3>Get All Items</h3>
<p>Endpoint: <code>/inventory/items/</code></p>
<p>Method: <code>GET</code></p>
<p>Success Response:</p>
<pre><code>
{
    "status": true,
    "message": [
        {
            "id": 1,
            "name": "New Item",
            "description": "Description of the item"
        }
    ]
}
</code></pre>

<h3>Get Item by ID</h3>
<p>Endpoint: <code>/inventory/items_by_id/&lt;item_id&gt;/</code></p>
<p>Method: <code>GET</code></p>
<p>Success Response:</p>
<pre><code>
{
    "status": true,
    "message": {
        "id": 1,
        "name": "New Item",
        "description": "Description of the item"
    }
}
</code></pre>

<h3>Update an Item</h3>
<p>Endpoint: <code>/inventory/update_items/&lt;item_id&gt;/</code></p>
<p>Method: <code>PUT</code></p>
<p>Request Body:</p>
<pre><code>
{
    "name": "Updated Item",
    "description": "Updated description"
}
</code></pre>
<p>Success Response:</p>
<pre><code>
{
    "status": true,
    "message": {
        "id": 1,
        "name": "Updated Item",
        "description": "Updated description"
    }
}
</code></pre>

<h3>Delete an Item</h3>
<p>Endpoint: <code>/inventory/delete_items/&lt;item_id&gt;/</code></p>
<p>Method: <code>DELETE</code></p>
<p>Success Response:</p>
<pre><code>
{
    "status": true,
    "message": "Item deleted successfully"
}
</code></pre>

<h2>Conclusion</h2>
<p>That's it! You now have a fully functional Inventory Management System API. Feel free to modify and enhance it as you see fit. Happy coding!</p>

</body>
</html>
