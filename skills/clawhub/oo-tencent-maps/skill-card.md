## Description:

Use this skill for Tencent Maps (lbs.qq.com) requests involving searching and reading map, place, route, location, district, and weather data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to access Tencent Maps through an OOMOL-connected account for geocoding, reverse geocoding, IP location, weather, administrative district lookup, place search, place details, nearby or polygon searches, and route planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes unverified remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Use a reviewed, pinned, or checksum-verified oo CLI installation method before running Tencent Maps actions.

Risk: Tencent Maps requests are brokered through OOMOL-connected server-side credentials.

Mitigation: Only sign in and connect Tencent Maps when the user intentionally wants OOMOL to broker those requests.

## Reference(s):

- [Tencent Maps ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tencent-maps)
- [Tencent Maps homepage](https://lbs.qq.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas and returns connector responses as JSON with data and execution metadata.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
