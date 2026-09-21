## Description:

Airbrake (airbrake.io). Use this skill for ANY Airbrake request — searching and reading data. Whenever a task involves Airbrake, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to inspect Airbrake projects, deploys, error groups, notices, and notice processing status through an OOMOL-connected Airbrake account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The broad activation language may cause an agent to fetch live Airbrake data whenever Airbrake is mentioned.

Mitigation: Review the skill before installation and constrain use to contexts where live Airbrake access is intended.

Risk: The first-time setup fallback can run a remote oo CLI installer.

Mitigation: Do not allow the agent to run the remote installer unless the OOMOL installer source is trusted and unverified script execution is acceptable.

Risk: Future write or destructive connector actions could change or remove Airbrake data.

Mitigation: Require explicit user confirmation for the exact payload and target before any action tagged write or destructive is run.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-airbrake)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Airbrake](https://airbrake.io)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects with data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: server evidence release.version and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
