## Description:

Mixpanel lets an agent operate Mixpanel through an OOMOL-connected account using the oo CLI instead of calling the Mixpanel API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to query Mixpanel analytics, reports, funnels, cohorts, profiles, retention, and event activity through a connected OOMOL account. It also guides agents to inspect each action schema before constructing connector payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes a remote installer command for the oo CLI, and the security summary flags that installer path for review.

Mitigation: Review installation steps before use, prefer a verified or pinned package-managed installation route, and require explicit approval before an agent runs any remote installer command.

Risk: The skill can access Mixpanel project analytics through the user's connected OOMOL account.

Mitigation: Confirm the connected account, project scope, and requested action before running connector commands, especially actions marked write or destructive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mixpanel)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Mixpanel homepage](https://mixpanel.com)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects with data and meta.executionId fields.]

## Skill Version(s):

1.0.4 (source: server evidence release and metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
