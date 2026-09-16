## Description:

APIVerve lets agents search and read APIVerve utility, language, location, and travel data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run APIVerve read-oriented utility, language, location, and travel actions from an OOMOL-connected account. The skill guides agents to inspect each action schema before constructing a JSON payload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can lead agents to execute remote installer scripts directly.

Mitigation: Prefer an official, version-pinned installer or a download-and-verify flow before installing the oo CLI.

Risk: APIVerve calls can fail or use incorrect inputs if payloads are constructed without the current action contract.

Mitigation: Inspect the live connector schema before building each action payload.

## Reference(s):

- [APIVerve homepage](https://apiverve.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub APIVerve skill page](https://clawhub.ai/oomol/skills/oo-apiverve)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId when actions run with --json.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
