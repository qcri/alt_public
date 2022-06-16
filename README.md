# alt_public [![Build Status](https://travis-ci.com/qcri/alt_public.svg?branch=master)](https://travis-ci.com/qcri/alt_public)

# The ALT references project.

Bib entries in this project are relfected in live websites. Therefore, proper care has to be taken to keep the references up to data and free of conflict. 

## Files and websites

Currently there are two bib files:
- tanbih.bib is used for tanbih.qcri.org
- alt.bib is used for alt.qcri.org

## Steps to add new references
The process to add new references is as follows:
1. Clone repo
2. Create a branch `git checkout -b branch_name`
3. Add the references
4. Commit and perform a a pull request. 

You should not merge the pull request until it passes the build. If any error shows, you have to resolve it in your local branch and then push your changes to the pull request and check the build again.  

If no errors are observed in the pull request, it will be accepted.

## Constraints

You are requested to add your new entry following an alphabetical order. The order is based on last name of 1st author, 2nd author... n-th author, title, venue, and date. Please get sure to stick to this order to make the life of the verifier easy. 

More important: do it to keep  the quality of our publications website!

## Verifications

Both automatic and manual verifications are triggered by the pull request:

### Automatic verification

A script is triggered that checks that the format of the bib file is correct and has no duplicates. The pull request will not be sent to the verifier if these checks are not passed.

### Manual verification 

A manual inspection is necessary to guarantee that the entry is acceptable and is not duplicated.


