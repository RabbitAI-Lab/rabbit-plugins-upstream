## Description:

Use this skill to operate Sauce Labs through an OOMOL-connected account for reading builds, jobs, job assets, and updating job metadata or status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and QA engineers use this skill to inspect Sauce Labs builds, jobs, and job assets, and to update job metadata or status after confirming the intended write payload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The write action can update Sauce Labs job name, tags, visibility, or pass status through the connected account.

Mitigation: Confirm the exact payload and intended effect with the user before running the write action.

Risk: One-time CLI setup and account connection establish access through OOMOL for this integration.

Mitigation: Perform setup only after an authentication or connection failure, and only when the user trusts OOMOL and needs the Sauce Labs integration.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-saucelabs)
- [Sauce Labs Homepage](https://saucelabs.com)
- [oo CLI Repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and execution metadata when actions are run.]

## Skill Version(s):

1.0.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
