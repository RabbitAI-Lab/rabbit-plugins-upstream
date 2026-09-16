## Description:

Use this skill for Tapfiliate requests on tapfiliate.com, including reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Tapfiliate through an OOMOL-connected account, including reading affiliate, program, click, conversion, and commission data and creating supported Tapfiliate records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The oo CLI setup path includes remote installer commands that execute downloaded code directly in a shell.

Mitigation: Review the installation path before use and prefer an official package manager or a manually downloaded, version-pinned installer with checksum or signature verification.

Risk: Tapfiliate write actions can create or modify records such as affiliates, groups, clicks, and conversions.

Mitigation: Confirm the exact action payload and expected effect with the user before running any write action.

## Reference(s):

- [Tapfiliate skill on ClawHub](https://clawhub.ai/oomol/skills/oo-tapfiliate)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Tapfiliate homepage](https://tapfiliate.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides agents to inspect live connector schemas before sending JSON payloads through the oo CLI.]

## Skill Version(s):

1.0.3 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
