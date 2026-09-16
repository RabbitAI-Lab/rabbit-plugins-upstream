## Description:

L2S (l2s.is) helps an agent read, create, and update shortened URL data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users with an OOMOL-connected L2S account use this skill to inspect existing shortened URLs, create new shortened URLs with optional metadata, and update stored URL details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that could execute arbitrary code if the installer source is compromised or untrusted.

Mitigation: Review and verify OOMOL installer sources before running remote installer pipelines; prefer a safer package source when available.

Risk: The update_url_details action changes stored L2S data.

Mitigation: Confirm the exact payload and intended effect with the user before running write actions.

## Reference(s):

- [L2S homepage](https://www.l2s.is)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub L2S skill page](https://clawhub.ai/oomol/skills/oo-l2s)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
