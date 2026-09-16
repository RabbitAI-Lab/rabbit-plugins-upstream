## Description:

Use this Ayrshare (ayrshare.com) skill for reading, creating, updating, and deleting Ayrshare data through the OOMOL oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Ayrshare through an OOMOL-connected account, including inspecting live action schemas, publishing or scheduling social posts, managing post lifecycle actions, and retrieving profile, history, detail, and analytics data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may execute mutable remote installer scripts on the user's machine.

Mitigation: Review the install path and run remote installer commands only after trusting OOMOL's installer source and accepting local code execution risk.

Risk: Publishing, updating, retrying, or deleting posts can change or remove Ayrshare data.

Mitigation: Require the exact payload, target, and expected effect to be confirmed before any write or destructive action.

Risk: Connector actions depend on the live Ayrshare action schema and connected OOMOL account state.

Mitigation: Inspect the live action schema before constructing payloads and use setup or connection steps only when a command fails with the matching auth, scope, credential, app, or billing error.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ayrshare)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Ayrshare homepage](https://www.ayrshare.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke OOMOL oo CLI commands that return JSON connector responses.]

## Skill Version(s):

1.0.5 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
