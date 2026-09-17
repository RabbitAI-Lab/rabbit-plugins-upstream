## Description:

Social Fetch helps an agent use an OOMOL-connected Social Fetch account to inspect action schemas and retrieve account, balance, profile, or channel data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to query Social Fetch through a connected OOMOL account, including account lookup, credit balance checks, and public profile or channel retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands can execute unverified code if an agent runs the documented setup path automatically.

Mitigation: Require explicit user approval before installer execution, review installer source first, and prefer a verified, version-pinned installation path.

Risk: The skill can access data available through the user's connected Social Fetch account.

Mitigation: Run only the read-oriented actions needed for the task and fetch the live connector schema before constructing each payload.

## Reference(s):

- [Social Fetch homepage](https://www.socialfetch.dev)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-social-fetch)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the live connector schema before request construction; responses include data and an execution id when actions run successfully.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
