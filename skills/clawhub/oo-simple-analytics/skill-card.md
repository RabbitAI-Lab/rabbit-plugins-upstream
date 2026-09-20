## Description:

Simple Analytics (simpleanalytics.com). Use this skill for ANY Simple Analytics request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with Simple Analytics through an OOMOL-connected account, including listing websites, retrieving aggregate statistics, exporting datapoints, and sending server-side events or pageviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup can direct an agent to install the oo CLI with remote shell commands.

Mitigation: Prefer manual installation from trusted OOMOL instructions, verify the installer where possible, and require confirmation before setup, login, connection, or write actions.

Risk: Write actions can send events or export datapoints through the connected Simple Analytics account.

Mitigation: Confirm the exact action, payload, and expected effect with the user before running any write-tagged action.

## Reference(s):

- [Simple Analytics homepage](https://simpleanalytics.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL Simple Analytics connection](https://console.oomol.com/app-connections?provider=simple_analytics)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before actions and requires confirmation before write or destructive operations.]

## Skill Version(s):

1.0.4 (source: evidence release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
