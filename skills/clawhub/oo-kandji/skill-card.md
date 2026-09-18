## Description:

Iru (Kandji) helps an agent search and read Kandji blueprint and directory user data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

IT, security, and device-management teams use this skill to let an agent retrieve Kandji blueprints and directory users, including filtered and paginated list operations. The skill is intended for read-only operational lookup through an already connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup instructions include remote installer commands that can execute local code.

Mitigation: Use a trusted, pinned, and verified oo CLI installation method before running connector actions.

Risk: The skill depends on an OOMOL-connected Kandji account and may fail when authentication, connection scope, billing, or app readiness is missing.

Mitigation: Run ordinary read actions only after the account is signed in and connected; address auth, scope, connection, or billing errors through the documented setup paths.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-kandji)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Iru homepage](https://www.iru.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return JSON responses from the OOMOL connector when run with --json.]

## Skill Version(s):

1.0.2 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
