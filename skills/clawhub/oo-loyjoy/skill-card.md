## Description:

LoyJoy lets agents operate LoyJoy through an OOMOL-connected account for reading, creating, and updating LoyJoy data via the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers with an OOMOL-connected LoyJoy account use this skill to inspect published LoyJoy processes and views, search tenant knowledge, and run LoyJoy process actions through the oo CLI. State-changing actions require confirmation of the exact payload and expected effect before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands for the oo CLI.

Mitigation: Prefer the official install guide, verify installer or package provenance where possible, and do not allow automatic execution of curl|bash or irm|iex.

Risk: Actions tagged as write can change LoyJoy state.

Mitigation: Confirm the exact payload and expected effect with the user before running create_completion or start_process.

Risk: The skill operates through OOMOL as an intermediary for LoyJoy account access.

Mitigation: Install and use it only when the user intends to use OOMOL for LoyJoy connectivity.

## Reference(s):

- [ClawHub LoyJoy skill page](https://clawhub.ai/oomol/skills/oo-loyjoy)
- [LoyJoy homepage](https://www.loyjoy.com/en/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect schemas and run LoyJoy connector actions; write actions require user confirmation before execution.]

## Skill Version(s):

1.0.2 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
