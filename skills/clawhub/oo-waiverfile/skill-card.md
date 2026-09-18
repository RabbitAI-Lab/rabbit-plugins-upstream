## Description:

WaiverFile (waiverfile.com) supports searching and reading data from a connected WaiverFile account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators with an OOMOL-connected WaiverFile account use this skill to retrieve site details, list waiver forms and upcoming events, fetch signed waivers, and search waiver records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include direct execution of remote installer scripts for the oo CLI, which creates a supply-chain risk if the installer source is compromised or misresolved.

Mitigation: Review the oo CLI installation path before use, prefer a versioned vendor installer, and verify the installer signature or checksum before execution.

Risk: Waiver searches and retrievals may expose sensitive signed waiver records.

Mitigation: Limit requests to the user's authorized WaiverFile account and avoid retrieving or displaying waiver data beyond what the task requires.

## Reference(s):

- [WaiverFile skill page](https://clawhub.ai/oomol/skills/oo-waiverfile)
- [WaiverFile homepage](https://www.waiverfile.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; action results are returned as JSON by the oo CLI.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
