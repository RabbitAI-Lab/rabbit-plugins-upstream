## Description:

Abyssale helps an agent read, create, and update Abyssale data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Abyssale through an OOMOL-connected account. The skill supports listing and retrieving Abyssale resources, creating projects, generating banners, and creating dynamic image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands for the oo CLI.

Mitigation: Review the oo CLI installation path before installing and prefer verified official installation guidance before running installer commands.

Risk: The skill can create projects, generate banners, and create dynamic image URLs, which can change Abyssale state.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions, and require explicit approval before any destructive action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-abyssale)
- [Abyssale homepage](https://www.abyssale.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute oo CLI connector calls that return JSON for requested Abyssale actions.]

## Skill Version(s):

1.0.5 (source: evidence.json release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
