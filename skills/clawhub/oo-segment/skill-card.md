## Description:

Segment (segment.com). Use this skill for ANY Segment request: reading, creating, and updating data through the OOMOL Segment connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and analytics teams use this skill to send Segment identify, track, page, screen, group, alias, and batch calls from an agent through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send write calls that alter Segment analytics data.

Mitigation: Confirm the exact action, payload, and expected effect before running any Segment write action.

Risk: Payloads may be invalid or mismatched if built from stale assumptions.

Mitigation: Fetch the live action schema with `oo connector schema` before constructing payloads.

Risk: The first-time setup path references remote CLI installers.

Mitigation: Use a trusted install path or inspect the installer before running it.

## Reference(s):

- [ClawHub Segment skill listing](https://clawhub.ai/oomol/skills/oo-segment)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Segment homepage](https://segment.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live action schema lookup before constructing Segment payloads.]

## Skill Version(s):

1.0.4 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
