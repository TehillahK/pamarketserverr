# Pa Market Server
This the backend server for pamarket and rest api server .
## Architecture

1. ### Persistence layer
2. ### Business layer
3. ###  Data layer

## Routes

### Web page routes
1.  /
- loads index page

2. /farm?id=val
- loads page of a particular farm crops
3. /farms
- loads page of all farms
4. /login
- sign in page 


### API Routes
1. /api/farms
- This sends the json object of all farms in the server
 
2. /api/farm?id=val
- This sends a request farm in the database ,using farm ID

3. /api/crops?id=val
- gets all crops associated to a farm ,using the farm ID .
