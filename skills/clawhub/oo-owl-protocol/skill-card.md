## Description:

Owl Protocol helps agents read project summaries and token metadata, and update token metadata through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to access Owl Protocol data through an OOMOL-connected account, inspect action schemas, run read actions, and patch token metadata after explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags the first-time setup instructions because they tell users to execute unverified remote installer scripts.

Mitigation: Review the installer delivery path before installing the oo CLI, and prefer a versioned, signed, or checksum-verified installation method.

Risk: The skill can patch Owl Protocol token metadata, which changes connected project state.

Mitigation: Require explicit user confirmation of the exact payload and expected effect before running write actions.

## Reference(s):

- [Owl Protocol ClawHub page](https://clawhub.ai/oomol/skills/oo-owl-protocol)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Owl Protocol homepage](https://owlprotocol.xyz)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return JSON responses from Owl Protocol connector actions.]

## Skill Version(s):

1.0.3 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
