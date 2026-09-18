## Description:

WakaTime lets agents retrieve WakaTime coding activity, project, user, daily summary, status bar, and all-time logged time data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to answer WakaTime questions about coding activity, project time, current user details, daily summaries, status bar data, and all-time logged time.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup fallback can direct an agent to run remote installer scripts when the required CLI is missing.

Mitigation: Review setup before installation; prefer a verifiable package or inspect the installer before running it.

Risk: WakaTime account queries are routed through OOMOL-connected credentials.

Mitigation: Connect WakaTime only when that account-routing model is acceptable for the deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-wakatime)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [WakaTime homepage](https://wakatime.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-focused connector actions; action schemas are inspected before constructing payloads.]

## Skill Version(s):

1.0.3 (source: metadata.version and release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
