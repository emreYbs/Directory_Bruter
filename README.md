# Directory_Bruter


![image](https://user-images.githubusercontent.com/59505246/137506689-0fa99554-4dd1-4466-9944-4cea00ca449f.png)


![image](https://user-images.githubusercontent.com/59505246/137520206-2573536e-d0b0-4bf4-8636-5a543b25875c.png)

**USAGE** : python3 directory_bruter.py
*Example* : You just give the URL in https://www.example.com, etc. The code will ask you to provide the URL as in the screenshot 

![image](https://user-images.githubusercontent.com/59505246/137521719-1eafb0df-6d6c-4fdc-9e6c-99141455c459.png)

**Important Note**:

- This code will run on Unix out of box, provided that you have installed the reguired libraries like pyfiglet, or you can edit the code and then no need to import pyfiglet, it is just for the banner, *not necessary for the code.* 

**For Windows**, you can change the / as \ and edit the wordlist path. So in a minute, you can use Directory_Bruter in Windows OS as well.If you need help, drop me a message via my e mail and I can help. OR I can also upload for Windows version.

*UPDATE*:   _I've added the version for Windows version in the same repo named as *Directory_Bruter_forWin.py._

- You should write the name of the target website like this 🔗: https://www.website.com  If you just provide it as "www.website.com", then you'll get an error.

- I used the Netsparker's wordlist(SVNDigger). You can use this wordlist or a related one. To download directly: https://www.netsparker.com/s/research/SVNDigger.zip

- You need to provide the downloaded wordlist path. In the code I wrote, I assumed the path "desktop". 🖥️

- You can get the connection errors as response code and the URL **(or if the connection is successful (status 200) )** ✅

- I've added some of my example screenshots and **blurred the target website addresses**. *You can view the screenshots before running the code to get an idea.*

- **There are not any special required libraries to import.** You may just need "pyfiglet and you can install it in the terminal:"pip3 install pyfiglet" and it is just needed for the banner. So it is nothing too important for the code to run.

- _You may use the code as you wish. I can just suggest to use it for good purposes such as finding some sensitive leftover devopment files in the remote server and take the necessary precautions._ **Otherwise, someone with malicous intentions can find some sensitive info in these leftovers.**

- Thanks to Tim for the support. 
