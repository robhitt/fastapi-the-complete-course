# INSTALL SQLITE
## Install [Homebrew](https://brew.sh) if not already installed
* you probably already have it installed, open terminal `$ brew update`
* `$ brew list` to see if it's enabled
* Otherwise `$ brew install sqlite`

## RUN SQLITE
`$ sqlite3` - confirm sqlite3 is installed  
`$ sqlite3 todos.db` - ex to enter a specific database while in the directory of the db.  
`sqlite> .schema` - shows schema in the db  
`sqlite> INSERT INTO todos (title, completed) VALUES ('create alerts', False)`
`sqlite> .mode column` or `sqlite> .mode markdown` or `sqlite> .mode box` or `sqlite> .mode table`  
`sqlite> SELECT * FROM todos`  
`.quit`  



