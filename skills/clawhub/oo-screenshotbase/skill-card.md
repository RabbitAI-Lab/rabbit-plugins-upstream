## Description:

This skill lets agents operate screenshotbase through an OOMOL-connected account to retrieve quota status and capture webpage screenshots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to call the screenshotbase connector through OOMOL for webpage screenshot capture and quota checks without handling raw API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Screenshot capture can expose private, authenticated, internal, or token-bearing URLs through a hosted screenshot result.

Mitigation: Confirm the target URL and intended capture with the user before running take_screenshot, and avoid sensitive URLs unless explicitly approved.

Risk: The connector contract can change over time, making stale payload assumptions unreliable.

Mitigation: Inspect the live action schema before constructing payloads for connector actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-screenshotbase)
- [screenshotbase homepage](https://screenshotbase.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Configuration guidance, Text]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector runs return JSON with data and meta.executionId when executed.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
