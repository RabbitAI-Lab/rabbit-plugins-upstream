## Description:

Enables an agent to inspect urlscan.io action schemas, retrieve and search scan data, and submit URLs for scanning through an OOMOL-connected oo CLI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security analysts use this skill to query urlscan.io scan results and search scan records. They can also submit URLs for scanning after confirming the exact payload and effect.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes one-line remote installer commands for the oo CLI.

Mitigation: Review and verify OOMOL installation instructions before running installer commands, and prefer version-pinned or otherwise verified installation steps.

Risk: The submit_scan action can create a new urlscan.io scan.

Mitigation: Confirm the exact URL submission payload and expected effect with the user before running the write action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-urlscan)
- [urlscan.io homepage](https://urlscan.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and execution metadata when actions are run.]

## Skill Version(s):

1.0.3 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
