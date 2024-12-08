# Git commands <!-- omit from toc -->

This topic contains a description of essential Git commands.

- [1. Squash and merge](#1-squash-and-merge)
  - [1.1. How it works](#11-how-it-works)
  - [1.2. Advantages of squash and merge](#12-advantages-of-squash-and-merge)
  - [1.3. When to use squash and merge](#13-when-to-use-squash-and-merge)
  - [1.4. Git commands for squashing and merge](#14-git-commands-for-squashing-and-merge)
- [2. Pull origin](#2-pull-origin)
  - [2.1. Command details](#21-command-details)
  - [2.2. Equivalent detailed commands](#22-equivalent-detailed-commands)
  - [2.3. Default behavior](#23-default-behavior)
  - [2.4. Common scenarios for `git pull origin`](#24-common-scenarios-for-git-pull-origin)
  - [2.5. Potential pitfalls](#25-potential-pitfalls)
- [3. Rebase](#3-rebase)
  - [3.1. Key differences between rebase and merge](#31-key-differences-between-rebase-and-merge)
  - [3.2. Benefits of rebase](#32-benefits-of-rebase)
  - [3.3. When to use rebase](#33-when-to-use-rebase)
    - [3.3.1. Steps to use rebase](#331-steps-to-use-rebase)
    - [3.3.2. Rebase vs. Pull with rebase](#332-rebase-vs-pull-with-rebase)
  - [3.4. Common workflows with rebase](#34-common-workflows-with-rebase)
- [4. Essential Git commands](#4-essential-git-commands)
  - [4.1. Setup and configuration](#41-setup-and-configuration)
  - [4.2. Working with changes](#42-working-with-changes)
  - [4.3. Viewing history](#43-viewing-history)


## 1. Squash and merge

*Squash and merge* is a technique in Git **used during pull requests to
combine multiple commits into a single, cleaner commit before merging
into the main branch**. This method is often used to maintain a tidy
commit history while preserving all the changes made in a feature
branch.

### 1.1. How it works

1. Multiple Commits in a Branch

    Suppose you have a feature branch with several commits (e.g., bug
    fixes, work-in-progress changes) that aren't meaningful on their
    own.

    Example of commits

    - Add feature implementation
    - Fix bug in feature
    - Update tests for feature

1. Squash

    **Before merging, these commits are squashed into a single commit**.
    All the changes are combined, and a new commit message is written to
    summarize the overall changes.

1. Merge

    The squashed commit is merged into the target branch (e.g., main or develop).

### 1.2. Advantages of squash and merge

- **Clean Commit History**. Eliminates unnecessary intermediate commits,
  making the history easier to read and understand.
- **Focused Commit Messages**. Encourages writing a single, descriptive
  commit message summarizing the feature or fix.
- **Reduced Noise in Logs**. Helps avoid clutter in the commit log
  caused by temporary or work-in-progress commits.

### 1.3. When to use squash and merge

- When a feature branch has multiple messy or intermediate commits.
- When the main branch should only contain meaningful, logical commits.
- When changes in a feature branch are small enough to be summarized in
  one commit.

### 1.4. Git commands for squashing and merge

To squash manually, you can use an interactive rebase as follows:

    > git rebase -i <base-branch>

- Mark all but the first commit as squash (s).
- Edit the commit message to summarize all the changes.

After squashing, merge the branch into the target branch using the following command:

    > git merge <branch>

> [!NOTE] Alternatively, many platforms (e.g., GitHub, GitLab) provide a
> "Squash and Merge" option in pull requests.


## 2. Pull origin

The command `git pull origin` is a shortcut in Git to **fetch** and
**merge** changes from a remote repository named origin. Here's what
happens step-by-step. 

### 2.1. Command details 

1. Remote repository (origin)

    *origin* is the **default name** for the **remote repository**
    **when you clone a repo**. You can check it with the following
    command:

        >git remote -v

1. Fetch changes

    `git pull origin` f**etches updates from the origin remote repository**.
    By default, it fetches the branch you're currently working on.

1. Merge changes

    After fetching, **Git merges the changes from the remote branch into
    your local branch**. If there are conflicts, you'll need to resolve
    them manually.

### 2.2. Equivalent detailed commands

Running `git pull origin` is equivalent to the following commands:

    >git fetch origin
    >git merge origin/<branch>

- `fetch` downloads updates from the remote branch.
- `merge` combines the fetched changes with your local branch.

### 2.3. Default behavior

If you run just `git pull origin`, Git **pulls updates from the default
branch of the origin remote**(e.g., **main** or **master**). You can
specify a branch explicitly as follows:

    >git pull origin <branch-name>

### 2.4. Common scenarios for `git pull origin`

- To synchronize your local branch with the latest changes from the
  remote repository.
- To bring in updates from teammates working on the same branch.

### 2.5. Potential pitfalls

- **Merge conflicts**. If your local changes conflict with the remote
  updates, you'll need to resolve these conflicts before completing the
  merge.
- **Overwriting changes**. If not careful, using pull can inadvertently
  merge in unwanted updates. **Use fetch first to preview changes**.

## 3. Rebase

In Git, `rebase` is an **alternative workflow to merge** that is often
used to maintain a **cleaner**, **more linear project history**. Here’s
an explanation of what it is, how it works, and when to use it.

Rebasing **reapplies your commits from one branch onto another, creating
a new base for your work**. It essentially **moves your changes to the
tip of the target branch as if you had branched off from the most recent
commit**.

Let's assume for example the following scenario:

- Suppose the main branch has commits A → B → C.
- Your feature branch has commits D → E based on B.

When you run the following command: 

    >git rebase main

- The commits D and E are re-applied on top of the latest commit in main
  (C).
- The new commit history becomes: A → B → C → D → E.

**This process avoids a merge commit, keeping the history linear**.

### 3.1. Key differences between rebase and merge

| Feature         | Merge                                                      | Rebase                                         |
| ----------------| ---------------------------------------------------------- | -----------------------------------------------|
| Commit History  | Retains the original branch structure, adds a merge commit.| Creates a linear history by rewriting commits. |
| Use Case        | Useful when preserving branch context.                     | Ideal for keeping a clean commit history.      |
| Complexity      | Easier for beginners, as history isn’t rewritten.          | More complex, requires resolving during rebase.|
| Collaboration   | Shared history remains intact.                             | Can rewrite history, watch shared branches.    |

### 3.2. Benefits of rebase

- **Clean history**. Produces a simple, linear commit history without
  merge commits.
- **Easier review**. Makes it easier to see the sequence of changes when
  reviewing history.
- **Resolving conflicts once**. You address conflicts only during the
  rebase, instead of resolving them during multiple merges.

### 3.3. When to use rebase

- **Before merging a feature branch**. Rebase your feature branch onto
  main to ensure it has the latest updates.
- **Tidying history**. When preparing a branch for merging or sharing,
  rebase can consolidate messy commits into a clean sequence.

#### 3.3.1. Steps to use rebase

1. Rebase a branch onto another.

        >git checkout feature
        >git rebase main

1. Handling conflicts during rebase.
If a conflict occurs, Git pauses the rebase. 

        > git status  # Shows files with conflicts

        # Resolve conflicts manually, then:
        > git add <file>
        > git rebase --continue

1. Aborting a rebase. To undo a rebase and restore the original branch. 

        >git rebase --abort

> [!WARNING]
> **Never rebase shared branches**.
> Rebasing rewrites commit history, so if someone else is using the same branch, it will cause inconsistencies and potential conflicts.

#### 3.3.2. Rebase vs. Pull with rebase

To fetch updates from a remote branch and rebase instead of merging.

    >git pull --rebase

### 3.4. Common workflows with rebase

1. Interactive rebase.  Allows you to edit, squash, or reorder commits.

        >git rebase -i HEAD~3

    Use this to combine multiple commits or improve commit messages.

1. Rebase onto another branch. Rebases your branch onto a different branch.

        >git rebase main feature

## 4. Essential Git commands

Here’s a list of essential Git commands grouped by their functionality.

### 4.1. Setup and configuration

- `git init`. Initialize a new Git repository in the current directory.
- `git clone <repo-url>`. Clone an existing repository from a remote
  location.
- `git config --global user.name "<name>"`. Set your name for all
  repositories.
- `git config --global user.email "<email>"`. Set your email for all
  repositories.

### 4.2. Working with changes

- `git status`. Show the status of the working directory and staging
  area.
- `git add <file>`. Stage changes for a specific file.
- git `add .`. Stage changes for all modified and new files.
- `git commit -m "<message>"`. Commit staged changes with a descriptive
  message.

### 4.3. Viewing history