## Description:

Open Docker in the user's Brave browser and take the user to the Docker homepage. Reuse an existing Docker tab/session when possible. Use when the user asks to open, visit, or go to Open Docker.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruchir17-cmd](https://clawhub.ai/user/ruchir17-cmd)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to open Docker's public website in Brave, reusing an existing tab or session when available and stopping before credential handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can focus Brave and reuse an existing Docker browser session.

Mitigation: Confirm the loaded site is docker.com and stop at any login or credential prompt.

Risk: Browser automation could be mistaken for permission to perform account actions.

Mitigation: Keep use limited to opening and verifying the Docker website unless the user gives a separate explicit instruction.

## Reference(s):

- [Docker homepage](https://www.docker.com/)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Brave browser automation; does not handle credentials or modify account data.]

## Skill Version(s):

1.0.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
