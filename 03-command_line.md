# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

`pwd` show current working directory path  
`mkdir` (e.g. mkdir exampledir) creating a directory  
`rmdir` (e.g. rmdir exampledir) deleting a directory  
`touch` (e.g. touch example.txt) creating a file using `touch` command  
`rm` (e.g. rm example.txt) deleting a file  
`mv` (e.g. mv example.txt example2.txt) renaming a file  
`ls -a` listing hidden files  
`cp` (e.g. cp exampledir/example.txt exampledir2) copying a file from one directory to another  
`top` show running processes within environment  
`grep` search for pattern matches in files  
`man` read documentation about commands  
`chmod` modify rwx file permissioning   
`ssh` log into a remote host - for example, access an AWS instance

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls` list contents of the current working directory  
`ls -a` list contents including hidden files (which start with a '.')  
`ls -l` long format, i.e. showing rwx file permissions  
`ls -lh` long format with file sizes in an interpretable format  
`ls -lah` long format with interpretable file sizes, including hidden files  
`ls -t` sorted by date/time (most to least recent)   
`ls -Glp` colored format, long format with permissions, directories shown with /    
 
---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

* `ls -R` list contents including contents of subdirectories as well, recursively
* `ls -d` list directories only
* `ls -m` list contents as comma seperated list
* `ls -1` list contents on individual lines
* `ls -r` list contents with order reversed

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

>> `xargs` converts a standard input stream to arguments used by another command and executes the command with these arguments. It can be used as a workaround with commands that normally disregard STDIN and to pass an arbitrarily long list of parameters to a command (sometimes number of parameters is limited).

>> An example use would be executing a remove command on all .txt files in a directory -- first use a `find` command with a wildcard, and pipe the output to `xargs rm` as below:

`find . -name "*.txt" | xargs rm`
 

