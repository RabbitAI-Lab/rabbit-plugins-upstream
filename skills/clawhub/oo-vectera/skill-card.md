## Description:

Use Vectera (go.vectera.com) for reading, creating, and updating meeting room data through the Vectera connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Vectera meeting rooms through an OOMOL-connected account, including listing, retrieving, creating, and updating rooms, settings, permissions, and join URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions can run unverified installer scripts downloaded from the internet.

Mitigation: Review the installer path before installing; prefer a pinned or package-manager install with checksum or signature verification.

Risk: Creating or updating meeting rooms, settings, permissions, or join URLs can change Vectera state.

Mitigation: Confirm exact payloads and expected effects before allowing write actions.

Risk: The connected Vectera account may grant scopes the user does not intend to use.

Mitigation: Connect only the Vectera account scopes the user is comfortable granting.

## Reference(s):

- [Vectera homepage](https://go.vectera.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-vectera)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, API calls, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
