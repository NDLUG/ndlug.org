+++
title = "How to contribute"
draft = false
date = "2017-10-24T15:00:42-04:00"
+++

Motivation
==========

The NDLUG blog is a group effort, and so if you would like to contribute, we would like that to be as easy as possible.
Simply follow these steps, and you can help make the blog great again.

But How?
========

First Steps
-----------

First, the site is made using hugo, so it will probably be useful to have hugo installed. Follow [their guide](https://gohugo.io/getting-started/installing/) on installing hugo if
you do not already have it installed. It isn't strictly necessary to install hugo to contribute to the site, but it helps for previewing your changes.

Next, you have to fork the site repo. There are two repositories for the blog, [the source files](https://github.com/NDLUG/ndlug.org) which you will be editing, and the
[published page](https://github.com/NDLUG/NDLUG.github.io) which contributers will push the compiled site to. Create a fork of the source files repo, and clone your fork.

Now that you have your own fork of the site source, you are ready to start either editing posts or making new ones. Enter the project directory to get started.

Editing Existing Posts
-----------------

In order to edit a post, simply open up the corresponding file
in `./content/post/` with your favorite text editor. Posts are formatted with markdown, so you might want to read up on that.

Creating New Posts
------------------

To create a new post, you can either just copy another post from `./content/post/` and change all of the stuff at the top, or you can have hugo fill out some of it for you (like the date).
To do that, run `hugo new post/name-of-your-file-here.md`, except you should change name-of-your-file-here.md to something a little better. Next, edit the file with your favorite editor,
as if it were an existing post. The new post should have some content that will help you with writing your post.

The site repo should also include a handle `new.sh` script, which will create the file for you, change the title attribute, and open it in your favorite editor automatically. To use the
script, simply invoke `./new.sh Tile of your new post` where **Title of your new post** is the title of the post you want, including spaces and all that, no need for quotes. The script
will remove the spaces and replace them with dashes for the file name and it will keep the spaces in the post title. This will ensure that the post titles are consistent with their file names,
which will be good for organization.

Testing
-------

Simply run `hugo serve` to test the site. Then, in your favorite web browser, visit `localhost:1313` - the site should load. Please preview your changes before trying to merge them!

Making it Live
--------------

In order to have your changes made public, please push your changes to your github fork, and then create a pull request. Someone should merge it in a timely fashion, and it will be compiled
and pushed into the public site.
