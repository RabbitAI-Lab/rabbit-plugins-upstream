## Description:

deja-vu memory — search the user's past AI coding sessions with the deja CLI. Holds what they already settled and never wrote into the repo (naming rules, banned or already-tried tools, required checks before merge, preferred values, who owns what). Use before your first edit in a task, before any plan, review, or blank-slate task, before you call a change done or ready to merge, before you recommend a tool, library, design or reviewer, before re-debugging an error, when concrete names (repo, service, file, error, flag) surface mid-task by batching recall with reads, when they say 'didn't we fix this before', 'what did we decide about X' or 'I already have that', and before telling them something on this machine does not exist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vshulcz](https://clawhub.ai/user/vshulcz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use deja-search to retrieve decisions and context from prior AI coding sessions while planning, editing, debugging, reviewing, and recommending tools for a project.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The automatic fallback may download and run an unpinned package without confirmation.

Mitigation: Review the fallback behavior and package source, and use an explicitly selected, trusted version before installing.

Risk: Memory or global-rule changes can affect later agent behavior.

Mitigation: Review the proposed changes and confirm their scope before applying them.

## Reference(s):

- [Memory for OpenClaw](https://vshulcz.github.io/deja-vu/guide/memory-for-openclaw.html)
- [deja-search on ClawHub](https://clawhub.ai/vshulcz/skills/deja-search)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Recall queries and concise session summaries in plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Past-session content is reference material; project-specific user statements require confirmation before changing work.]

## Skill Version(s):

0.24.3 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
