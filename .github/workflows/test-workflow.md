---
on:
  workflow_dispatch: {}
  issues:
    types: [assigned]

permissions:
  contents: read
  issues: read
  pull-requests: read

network: defaults

safe-outputs:
  add-comment:
---

# Auto-acknowledge issues assigned to sasinomalabs (manual = pick latest)

## Determine the target issue number

### If triggered by `issues.assigned`
- The target is the issue from the event payload.
- When calling `add_comment`, OMIT `item_number` so it auto-targets the triggering issue.

### If triggered by `workflow_dispatch` (manual run, no inputs)
You MUST determine the target issue as follows:
1. Query this repository for OPEN issues assigned to `sasinomalabs`.
2. Sort by **most recently updated** (descending).
3. Select the single most recently updated issue.
4. Record its issue number as `TARGET_ISSUE_NUMBER`.

If no open issues are assigned to `sasinomalabs`, do not comment; use `noop` with message:
"No open issues assigned to sasinomalabs were found."

## Guardrails (skip rules)
Do NOT comment if:
- The selected issue is closed, OR
- `sasinomalabs` is not an assignee.

Also, avoid duplicate acknowledgements:
- If any existing comment contains the exact phrase:
  "Thanks for the report — we're going to check this and get back to you."
  then do not comment; use `noop`.

## Comment task
Read:
- Issue title/body
- All existing comments

Then post EXACTLY ONE comment.

### Comment content requirements
Your comment must include:
1) Acknowledgement:
"Thanks for the report — we're going to check this and get back to you."

2) Answers:
If the issue body/comments contain direct questions, answer them briefly and clearly.

3) Clarifications:
If key information is missing, ask up to 3 specific clarifying questions (bulleted).

## How to post the comment (important)
- For `issues.assigned` runs: call `add_comment` with only `{ body: ... }`.
- For manual `workflow_dispatch` runs: call `add_comment` with:
  - `item_number: TARGET_ISSUE_NUMBER`
  - `body: ...`

Do not change labels/assignees/milestones and do not close the issue.
---