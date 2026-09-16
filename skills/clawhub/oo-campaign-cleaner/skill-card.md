## Description:

Campaign Cleaner lets agents operate Campaign Cleaner through the OOMOL-connected oo CLI to read, submit, analyze, report on, and delete email campaign data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to inspect Campaign Cleaner action schemas, submit email campaign HTML for analysis, retrieve campaign status and reports, check credits, and delete saved campaigns with explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that download and execute scripts.

Mitigation: Do not let an agent run those installers automatically; install the oo CLI only through a trusted, user-verified method.

Risk: The send_campaign action changes Campaign Cleaner state by submitting campaign HTML for analysis.

Mitigation: Confirm the exact payload and intended effect with the user before running write actions.

Risk: The delete_campaign action removes a saved campaign.

Mitigation: Confirm the target campaign ID and obtain explicit approval before running destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-campaign-cleaner)
- [Campaign Cleaner homepage](https://campaigncleaner.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON command results, and transit file references for PDF reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include a data object and meta.executionId when actions run successfully.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
