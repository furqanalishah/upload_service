## Summary

The title and summary of a PR end up in the `git` history, where they'll help developers in the future (including
yourself) figure out why the code is the way it is.

Therefore, the title of each PR should:
- briefly summarize what you added/fixed/changed;
- not be longer than 72 characters, because:
  - Github truncates/wraps them at 72 characters;
  - having a consistent title length limit helps keep `git log --oneline` etc easy to read;
  - 72 characters should be enough for a short summary.

The summary (text below the title) should:
- describe what you added/fixed/changed (insofar as it's not already obvious from the commit title) and, if it's not
  obvious, why that's desirable;
- describe any trade-offs you made that are not apparent from the code itself.

---

Select the **nature** of change in this PR from below list 
- [x] `Feature`
- [ ] `Bug Fix`
- [ ] `Enhancement, Refactor or Reformating`
- [ ] `Cleaning`
- [ ] `Documentation`

---

**Trello card Link**: https://trello.com/c/example

---


**Sample Code/Traceback**: [Input/Output] Add inputs for parsing functions

---

