## Description:

Honeybadger helps an agent operate Honeybadger through an OOMOL-connected account to report check-ins, deployments, Insights events, and exception notices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and site reliability teams use this skill to send Honeybadger monitoring reports from an agent through an OOMOL-connected account. It is most relevant when reporting check-ins, deployments, Insights events, or exception notices after confirming the intended payload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send check-ins, deployments, events, and exception notices that change Honeybadger monitoring data.

Mitigation: Confirm the user's intent and exact payload before sending reports, and inspect the live action schema before constructing each request.

Risk: Payloads may include sensitive logs, stack traces, environment data, tokens, or customer data.

Mitigation: Review payload contents before execution and remove secrets or unnecessary sensitive data.

Risk: The skill includes CLI installation commands that download and execute remote scripts.

Mitigation: Install the oo CLI through a verified method or official install guide instead of piping a downloaded script directly into a shell.

## Reference(s):

- [ClawHub Honeybadger skill page](https://clawhub.ai/oomol/skills/oo-honeybadger)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Honeybadger homepage](https://www.honeybadger.io)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before constructing connector requests.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
