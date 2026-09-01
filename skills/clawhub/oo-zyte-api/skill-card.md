## Description:

Zyte API helps agents inspect Zyte connector schemas and run read-oriented public URL extraction actions through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to extract article data, generic page content, product data, or browser-rendered HTML from public URLs through a connected Zyte API account while checking each action schema before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes Zyte API work through OOMOL's oo connector and may use the user's connected Zyte API account for public URL extraction.

Mitigation: Install the oo CLI and connect Zyte only when intending to use that service, and review JSON payloads before running connector actions.

Risk: Future connector actions could change or delete service state if write or destructive actions are added.

Mitigation: Confirm the exact payload and effect with the user before running any action tagged write, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-zyte-api)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Zyte API Homepage](https://www.zyte.com/zyte-api/)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects with data and meta.executionId fields.]

## Skill Version(s):

1.0.1 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
