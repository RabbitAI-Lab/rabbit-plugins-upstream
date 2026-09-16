## Description:

WaiverFile helps an agent search and retrieve site details, waiver forms, signed waivers, upcoming events, and waivers by reference for a connected WaiverFile account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to let an agent read and search WaiverFile account data through the OOMOL connector. It is suited for retrieving waiver records, event lists, form lists, site details, and waivers tied to external reference identifiers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote shell and PowerShell installers.

Mitigation: Install only from a reviewed or verified path, and do not let an agent automatically run curl-to-bash or PowerShell iex installer commands.

Risk: Successful use accesses data from the connected WaiverFile account through OOMOL.

Mitigation: Install only if you trust OOMOL and the WaiverFile connector, and scope agent tasks to the WaiverFile data the user intends to retrieve.

## Reference(s):

- [ClawHub WaiverFile skill page](https://clawhub.ai/oomol/skills/oo-waiverfile)
- [WaiverFile homepage](https://www.waiverfile.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; responses are expected as JSON from the oo CLI.]

## Skill Version(s):

1.0.2 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
