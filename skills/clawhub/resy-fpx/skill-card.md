## Description:

Query and act on Resy reservations from a shell with curl, including venue search, slot availability, booking or cancellation, favorites, and Priority Notify management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to produce ready-to-run shell workflows for Resy account actions without running the resy-mcp server. It supports token setup, reservation lookup, booking, cancellation, favorites, and notify management for a user's own Resy account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables live Resy account automation, including booking, cancellation, favorites, and Priority Notify changes.

Mitigation: Require explicit user confirmation before executing write actions, and verify state with list or profile calls before and after changes.

Risk: The workflows handle Resy credentials and auth tokens in shell commands.

Mitigation: Avoid saving credentials or tokens in shell history, use environment variables carefully, and consider an isolated browser profile for fpx pairing.

## Reference(s):

- [Resy API ready-to-run requests](artifact/references/resy-api.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may make live changes to the user's Resy account when executed.]

## Skill Version(s):

1.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
