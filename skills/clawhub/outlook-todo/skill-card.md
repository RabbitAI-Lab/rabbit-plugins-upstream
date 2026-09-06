## Description:

Read Microsoft To Do task lists and tasks via shared Outlook Graph auth.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guoxh](https://clawhub.ai/user/guoxh)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to inspect Microsoft To Do lists and tasks for the signed-in Outlook account. With explicit confirmation, it can also help create, update, complete, or delete tasks through Microsoft Graph.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses shared Microsoft Graph OAuth credentials with Tasks.ReadWrite and inherited calendar write authority, which can permit task changes beyond read-only To Do viewing.

Mitigation: Install only where the shared OAuth boundary is acceptable, review requested scopes during device-code consent, and limit use to the intended Outlook account.

Risk: Agents can create, update, complete, or delete tasks when todo-write.sh is invoked with --apply, and --yes can bypass the delete prompt.

Mitigation: Keep write operations as dry-runs until the exact change is reviewed; do not allow --apply --yes unless the deletion has been separately approved.

Risk: The skill reads shared local Outlook Graph config and token files under ~/.outlook-graph/.

Mitigation: Protect those files as credentials and avoid exposing token or config contents in prompts, logs, or generated output.

## Reference(s):

- [Microsoft Graph To Do Notes](artifact/references/graph-todo.md)
- [Microsoft Graph API](https://graph.microsoft.com)
- [Microsoft identity platform sign-in](https://login.microsoftonline.com)
- [ClawHub skill page](https://clawhub.ai/guoxh/skills/outlook-todo)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and task data in summary, ids, raw, or JSON formats]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires bash, jq, curl, python3, and shared Outlook Graph auth; writes are dry-run by default and require explicit apply confirmation.]

## Skill Version(s):

1.0.1 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
