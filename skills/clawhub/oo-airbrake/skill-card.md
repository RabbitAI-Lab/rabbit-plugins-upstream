## Description:

Enables agents to operate Airbrake through an OOMOL-connected account for retrieving projects, error groups, notices, deploys, and notice status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and support engineers use this skill to inspect Airbrake projects, deploys, error groups, notices, and notice processing status from an agent session. The skill also guides agents to fetch live connector schemas before constructing requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands could execute unreviewed code locally.

Mitigation: Install the oo CLI only through a trusted, reviewed method and do not let an agent automatically run pipe-to-shell install commands.

Risk: Airbrake API access could expose or modify sensitive project and error data if credentials are overprivileged.

Mitigation: Use a least-privilege Airbrake API key and review connector schemas and payloads before write-like actions.

Risk: The get_deploy action has an ambiguous safety tag in the artifact.

Mitigation: Treat get_deploy as requiring confirmation until the action tag is corrected or its effect is verified.

## Reference(s):

- [ClawHub Airbrake skill page](https://clawhub.ai/oomol/skills/oo-airbrake)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Airbrake](https://airbrake.io)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON connector payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before request construction; command responses include data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
