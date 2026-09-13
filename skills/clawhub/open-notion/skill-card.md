## Description:

Open Notion in the user's Brave browser and take the user to their Notion workspace/dashboard when possible.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruchir17-cmd](https://clawhub.ai/user/ruchir17-cmd)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to open Notion in Brave, reuse an existing authenticated session when available, and reach a Notion workspace or dashboard without handling credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may open Notion using an existing signed-in Brave session.

Mitigation: Install only where this browser behavior is expected, and stop at login without requesting, entering, or storing credentials.

Risk: A browser automation agent could affect Notion content if asked to continue beyond opening the workspace.

Mitigation: Keep this skill limited to opening and verifying Notion unless the user explicitly asks for separate content changes.

## Reference(s):

- [Notion homepage](https://www.notion.com/)
- [ClawHub skill page](https://clawhub.ai/ruchir17-cmd/skills/open-notion)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Markdown or concise text status with browser automation actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May open or focus Brave, reuse an existing Notion tab, navigate to Notion, stop at login, and report whether the destination was verified.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
