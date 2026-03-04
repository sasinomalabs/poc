---
name: "Agentic: Issue to PR"
on:
  issues:
    types: [opened, labeled]
strict: true
---

# Agentic Issue → PR (strict mode)

## When to run
Run when:
- an issue is opened, OR
- an issue is labeled with `agentic-pr`

(If the event is `labeled`, only proceed when label name is exactly `agentic-pr`.)

## Inputs
Read from the event payload:
- issue.number
- issue.title
- issue.body

Write the issue body to `issue_body.md` (multiline-safe).

## Generate changes (no direct git push)
1. Check out the repository.
2. Run an “agent step” that modifies files in the working directory based on `issue_body.md`.
   - Placeholder output (until a real agent exists):
     - create `agentic-output/ISSUE-<issue_number>.md` containing issue title + body.
3. If there are no file changes, end successfully and (optionally) add a comment to the issue saying “No changes generated.”

## Create PR (safe output)
If changes exist, create a pull request using **safe outputs** (not by pushing a branch yourself):
- title: `Agentic: #<issue_number> - <issue_title>`
- body includes: `Closes #<issue_number>`
- base: default branch

Use:
- safe-outputs.create-pull-request

## Optional: status comment
After creating the PR, add a comment on the issue with the PR URL using:
- safe-outputs.add-comment