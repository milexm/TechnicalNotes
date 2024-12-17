# GitHub notes <!-- omit from toc -->


## 1. Git

- [1. Git](#1-git)
- [Git](#git)
  - [Git Getting Started](#git-getting-started)
    - [1.1.2. Publish Local Git Repository to GitHub](#112-publish-local-git-repository-to-github)
    - [1.1.3. Add information to README.md](#113-add-information-to-readmemd)
- [2. GitHub](#2-github)
  - [3.2. Create a branch](#32-create-a-branch)
- [4. Glossary](#4-glossary)
- [5. Custom Styles](#5-custom-styles)
- [6. Appendix](#6-appendix)
  - [6.1. Appendix A - TBD](#61-appendix-a---tbd)
- [7. - 1. Git](#7---1-git)
- [8. References](#8-references)

## Git

**Git** is a revision control system, a <b>tool</b> to manage your source code history

### Git Getting Started





#### 1.1.2. Publish Local Git Repository to GitHub


#### 1.1.3. Add information to README.md

~~ 1. In your favorite markdown editor, edit the **README.md** file and add meaningful information about the project. I use [MacDown](https://macdown.uranusjr.com/) as the markdown editor on a Mac laptop. ~~
~~2. In your Git client you will see in green the content added to the file. Verify that everything is correct.~~
~~3. In the left pane, add a comment about the changes you made.~~
~~4. Click the **Commit to master** button.~~
~~5. In the right pane, click the **Push origin** button. This publishes the file to your GitHub repository. ~~ 


## 2. GitHub




### 3.2. Create a branch



## 4. Glossary

- **Repository**. It is a collection of commits, each of which is an archive of what the project’s working tree looked like at a past date, whether on your machine or someone else’s. It also defines **HEAD** which identifies the branch or commit the current working tree stemmed from. Lastly, it contains a set of branches and tags, to identify certain commits by name.
- **Commit**. A commit is a snapshot of your working tree at some point in time. The state of HEAD at the time your commit is made becomes that commit’s parent. This is what creates the notion of a **revision history**.
- **Index**. Git does not commit changes directly from the working tree into the repository. Instead, it registers them in the **index**. It is a way of “confirming” your changes, one by one, before doing a commit, which records all your approved changes at once. Some call it the **staging area**, instead.
- **Working tree**. A working tree is any directory on your filesystem which has a repository associated with it, typically indicated by the presence of a sub-directory within it named **.git.**. It includes all the files and sub-directories in that directory.
- **Branch**. A branch is just a name for a commit. It is also called a reference. It is the parentage of a commit which defines its history, and thus the typical notion of a “branch of development”.
- **Tag**. A tag is also a name for a commit, similar to a branch, but it always refers to the same commit. It can have its own description text.
- **Master** The mainline of development in most repositories is done on a branch called “**master**”. Although this is a typical default, there is nothing special about this branch.
- **HEAD** It is used by the repository to define what is currently checked out, specifically:
  - If you checkout a branch, HEAD symbolically refers to that branch, indicating that the branch name should be updated after the next commit operation.
  - If you checkout a specific commit, HEAD refers to that commit only. This is referred to as a detached HEAD, and occurs, for example, if you check out a tag name.

## 5. Custom Styles

The technique shown in [Custom Styles](#custom_styles) section work on your local machine, 'cause the style *custom.css* file is local, in the case of Jupyter Notebooks. But it does not work if you publish the file on a public server such as Anaconda cloud. The ideal thing is to have the *custom.css* file available globally. The best solution, in the case of Jupyter Notebooks (and Anaconda cloud) is to <span class="m_warning">define the custom styles locally in your markdown file</span> as you can see next, if you display this cell in edit mode.

<style>
/* Custom Markdown styles */

/* Note Red */
.danger {
  background-color: #ffdddd;
  border-left: 6px solid #f44336;
}

/* Note Green */
.success {
  background-color: #ddffdd;
  border-left: 6px solid #4caf50;
}

/* Note Blue */
.info {
  background-color: #e7f3fe;
  border-left: 6px solid #2196f3;
}

/* Note Yellow */
.warning {
  background-color: #ffffcc;
  border-left: 6px solid #ffeb3b;
}

/* Note Gray */
.other {
  background-color: #e7e7e7;
  border-left: 6px solid #696965;
}

/* Marker Yellow */
.m_warning {
  background-color: yellow;
}

/* Marker Gray */
.m_other {
  background-color: lightgray;
}

/* Marker Blue */
.m_info {
  background-color: lightblue;
}

/* Marker Orange */
.m_danger {
  background-color: #ffdddd;
}
</style>

<code language="xml">

 <div style="background-color: #ffffcc;
 border-left: 6px solid #ffeb3b;">Yellow</div>

 <div style="  background-color: #ffdddd;
 border-left: 6px solid #f44336;">Red</div>
  
 <div style="background-color: #ddffdd;
 border-left: 6px solid #4caf50;">Green</div>

 <div style="background-color: #e7f3fe;
 border-left: 6px solid #2196f3;">Blu</div>
</code>  

## 6. Appendix

### 6.1. Appendix A - TBD

## 7. - [1. Git](#1-git)

## 8. References

- [GitHub desktop documentation](https://docs.github.com/en/desktop/)
- [GitHub Docs](http://guides.github.com/) - GitHub documentation hub.
