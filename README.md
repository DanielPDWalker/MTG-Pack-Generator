# MTG-Pack-Generator
MTG Pack Generator Example :
[![https://gyazo.com/9d75a7a3de8349588eb208816fcfdfc6](https://i.gyazo.com/9d75a7a3de8349588eb208816fcfdfc6.gif)](https://gyazo.com/9d75a7a3de8349588eb208816fcfdfc6)

# Info  
* The script will generate a pack based on a set you pass it. 
* Capitilization does not matter. 
* There are a few sets that dont work, but most do.
* The packs are generated in the folder containing the script.
* The script checks how many of each packs are in the folder and increment the counter before the name by 1 automatically.
  
The script works by using the python mtgsdk to generate random cards from a set, then using their multiverse ID (unique identification number), it uses requests to download the image of the card from the gatherer website.

# Requirements  
You can either use the setup.py file that comes with this project by going to the directory on your computer in CMD or Terminal and typing:
``` 
python setup.py install
```    

Or you can manually install/check you have things you need installed.  
  
In CMD or Terminal, (in any directory, so long as pip is on your path), type each of these on separate lines -  
  
```
pip install requests
```  
```
pip install mtgsdk
```


