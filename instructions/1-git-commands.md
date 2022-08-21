# Git workflows

## Cloning a new project

```console
git clone https://github.com/OpenAvenues-PickleRobotCompany/manip-trajopt-control.git .
```

Cloning is the industry standard.

Alternatively:
It is also possible to [download a zip from the Github Project](https://github.com/OpenAvenues-PickleRobotCompany/manip-trajopt-control/archive/refs/heads/main.zip).
Then to extract it using 7-zip, unzip or any other free extractor tools.

## Pulling the latest change on the main branch

```console
git checkout main
git pull
```

*git checkout main* changes your current git branch to be the *main* one. git pull download changes from the remote (the GitHub repository in our case) and applies them to the current branch (*main* here since we checked out before)

## Creating a new branch from main

```console
git checkout main
git pull
git checkout -b my-branch-name
```

*git checkout -b my-branch-name* creates a new branch with name *my-branch-name* and checks it out.

## Staging and commiting your changes

Staging and commiting are local actions which only affect your local git repository.
Staging enables you to select which files/lines you want to commit/keep.
Committing enables to save the staged changes into your local git history.
[Ideally, you should stage and commit often.](https://softwareengineering.stackexchange.com/questions/74764/how-often-should-i-do-you-make-commits)

```console
git add my-files
git commit
```

*git add my-files* adds the chosen file to the staging area. *my-files* can be the path to a single file, paths to multiple files where each path
is separated by a blank space, *.*. *.* stages all changes of the current directory and its subdirectories. Use *.* when you are sure you want to stage
all the current changes. It is also possible to stage specific lines from a file using the command line but it is easier to do it using a visual
git tools such as the one integrated in VSCode or Magit.

*git commit* commits all the staged files. It opens an interface to write a commit message that should describe your changes.
[How to write a good commit message.](https://stackoverflow.com/questions/33097657/how-to-write-a-good-git-commit-message)

## Pushing your local change to the remote

NOTE: Only do this on feature branch, never push on the main branch.

```console
git pull --rebase
git push
```

*git push* pushes the local changes of the current local branch to the remote. *git pull --rebase* is optional and is only required if several members work on the same branch together.

## Merging your remote branch changes into the main branch

Go to [GitHub website Pull Request interface](https://github.com/OpenAvenues-PickleRobotCompany/manip-trajopt-control/pulls).
Click on *New Pull Request*.
Set *base* to *main*. Set *compare* to *my-branch-name*.
