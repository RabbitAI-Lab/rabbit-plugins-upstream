## Description:

Beamer lets agents read Beamer data and create changelog posts through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate a connected Beamer account from an agent, including reading unread counts, feed URLs, and existing posts, and creating changelog posts after confirming the payload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes a remote shell installer for the oo CLI.

Mitigation: Review the installation path first and prefer official, version-pinned, verifiable installation instructions where available.

Risk: The skill can create Beamer changelog posts through a connected account.

Mitigation: Confirm the exact post creation payload and intended effect with the user before running write actions.

Risk: Broad Beamer routing could cause the agent to operate a live connected account for unrelated or ambiguous requests.

Mitigation: Use the skill only when the user intends to operate Beamer, and inspect the live connector schema before constructing an action payload.

## Reference(s):

- [Beamer homepage](https://www.getbeamer.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; write actions require user confirmation.]

## Skill Version(s):

1.0.4 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
