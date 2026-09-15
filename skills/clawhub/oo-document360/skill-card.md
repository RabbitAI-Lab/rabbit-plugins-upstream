## Description:

Use this skill for Document360 requests that search and read workspace data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent search and read Document360 workspaces, articles, and category hierarchies through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags setup instructions that tell an agent to run unverified internet installer scripts.

Mitigation: Do not let an agent run the installer commands automatically; install the oo CLI through a verified, versioned, signed, or checksum-checked method before using the skill.

Risk: Use depends on OOMOL as the connector provider with credentials injected server-side.

Mitigation: Install only if the deployment is comfortable with OOMOL as a connector provider, and prefer read-only Document360 actions unless a user explicitly approves broader actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-document360)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Document360 homepage](https://document360.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON data, Guidance]

**Output Format:** [Markdown instructions with shell command snippets and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; available documented actions are read-oriented list, get, and search operations.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
