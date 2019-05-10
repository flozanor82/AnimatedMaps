# AnimatedMaps - GIF CREATION- Readme
Stata Code that Generates Maps and Python code that animates them


•	Include the Chrome Driver location in your PATH environment variable

   - If you don’t know where the PATH is you can search for it in Windows at:
       - Control Panel\System and Security\System ->Advance system setting ->Advanced -> Environmental Variables -> Path(Set the path of the driver in this location) 

       
![alt text](Images/Path.png)


•	Potential Bug
   -	Your chrome driver is not up to date. Error
SessionNotCreatedException: session not created: Chrome version must be between 70 and 73
(Driver info: chromedriver=2.45.615291 (ec3682e3c9061c10f26ea9e5cdcf3c53f3f74387),platform=Windows NT 10.0.17134 x86_64)
   -	Go to chrome to download a compatible driver. As per May 8, 2019 Chrome Driver 2.46 solved the issue. 
