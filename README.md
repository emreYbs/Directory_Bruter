# Directory_Bruter

**The aim of this python script**, _@author Emre | github.com/emreYbs_, is **to get the leftover development files, debugging scripts and configutations files in the server**.

So maybe, we can get some sensitive information by hunting common filenames and directories. 
Therefore, we can get some precaution for the leftovers. Also, this script will be handy for some pentest related tasks.

**Important Note**:

- You should write the name of the target website like this: https://www.website.com  If you just provide it as "www.website.com", then you'll get an error.

- I used the Netsparker's wordlist(SVNDigger). You can use this wordlist or a related one. To download directly: https://www.netsparker.com/s/research/SVNDigger.zip

- You need to provide the downloaded wordlist path. In the code I wrote, I assumed the path "desktop".

- You can get the connection errors as response code and the URL **(or if the connection is successful (status 200) )** 

- I've added some of my example screenshots and **blurred the target website addresses**. *You can view the screenshots before running the code to get an idea.*

- **There are not any special required libraries to import.** You may just need "pyfiglet and you can install it in the terminal:"pip3 install pyfiglet" and it is just needed for the banner. So it is nothing too important for the code to run.

- _You may use the code as you wish. I can just suggest to use it for good purposes such as finding some sensitive leftover devopment files in the remote server and take the necessary precautions._ **Otherwise, someone with malicous intentions can find some sensitive info in these leftovers.**

- Thanks to Tim for the support. 
