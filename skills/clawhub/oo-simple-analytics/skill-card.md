## Description:

Enables agents to operate Simple Analytics through an OOMOL-connected account for reading, exporting, aggregating, and sending analytics data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Simple Analytics action schemas, list websites, retrieve aggregate stats, export datapoints, and send confirmed server-side events through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes direct execution of remote installer scripts.

Mitigation: Prefer verified oo CLI releases or package-manager installation, and review installer commands before running them.

Risk: Simple Analytics requests and responses are routed through OOMOL-connected infrastructure.

Mitigation: Confirm this routing is acceptable for the account's analytics data and organizational data-handling requirements before installation.

Risk: The send_event action can write pageviews or events to Simple Analytics.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/oomol/skills/oo-simple-analytics)
- [Simple Analytics Homepage](https://simpleanalytics.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Simple Analytics Connection](https://console.oomol.com/app-connections?provider=simple_analytics)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas and returns oo CLI JSON responses with execution metadata when actions run.]

## Skill Version(s):

1.0.3 (source: evidence release, skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
