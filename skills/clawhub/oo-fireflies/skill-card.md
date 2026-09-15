## Description:

Fireflies (fireflies.ai) skill for reading, creating, updating, and deleting Fireflies data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Fireflies meeting data through the OOMOL Fireflies connector. It supports transcript, bite, channel, user, user group, AI app output, and AskFred workflows, including selected write and delete actions with confirmation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes direct execution of remote installer scripts for the oo CLI.

Mitigation: Review the installer before use and prefer a verified, pinned, or signed installation method when available.

Risk: The skill can update Fireflies records, change user roles, and delete transcripts or AskFred threads.

Mitigation: Approve write, role-change, and delete actions only after checking the exact Fireflies target and payload.

## Reference(s):

- [Fireflies homepage](https://www.fireflies.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-fireflies)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Markdown, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return connector JSON responses with data and execution metadata.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
