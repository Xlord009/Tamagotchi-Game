BASIC GIT WORKFLOW

# check current branch
git branch

# create and switch to a new branch
git checkout -b branch_name

# switch to an existing branch
git checkout branch_name

# stage changes
git add file_name   # or git add . for all changes

# commit staged changes
git commit -m "descriptive message"

# push branch to remote (GitHub)
git push -u origin branch_name



BRANCHING AND MERGING

# merge a branch into current branch
git merge other_branch_name

# delete a local branch
git branch -d branch_name       # safe delete
git branch -D branch_name       # force delete

# delete a remote branch
git push origin --delete branch_name


INSPECTING HISTORY

# see commit history in one line
git log --oneline

# see graph with all branches and commits
git log --oneline --graph --all --decorate

# compare two branches
git diff branch1 branch2



MERGE CONFLICT HANDLING

# after merge conflict, edit file to resolve
# then
git add file_name
git commit -m "resolved merge conflict"
