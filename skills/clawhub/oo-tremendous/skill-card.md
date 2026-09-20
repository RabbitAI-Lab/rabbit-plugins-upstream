## Description:

Tremendous (tremendous.com). Use this skill for ANY Tremendous request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Tremendous through an OOMOL-connected account, including retrieving campaigns, funding sources, orders, products, rewards, and organizations. It also supports creating reward orders and generating reward redemption links after user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: State-changing Tremendous actions can create reward orders or generate reward redemption links.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

Risk: Installing the oo CLI through remote install scripts can execute unreviewed installer code.

Mitigation: Use a verified oo CLI installation path and avoid blindly executing remote install scripts.

## Reference(s):

- [Tremendous homepage](https://www.tremendous.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands target the OOMOL oo CLI and may return connector JSON with data and execution metadata.]

## Skill Version(s):

1.0.3 (source: evidence.release.version and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
