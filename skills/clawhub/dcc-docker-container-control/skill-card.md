## Description:

Provides fast manual CI for Docker Compose apps by mapping DCC commands to a controller that fetches latest Git commits, builds, deploys, restarts containers, and verifies status on a known Docker server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drodecker](https://clawhub.ai/user/drodecker)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to run manual Docker Compose deployments on a known Docker server when a traditional CI pipeline is unavailable or too slow. It helps list, inspect, deploy, restart, or recreate Compose apps while reporting command output and final container status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run Docker Compose deployment commands with sudo on a server.

Mitigation: Install and use it only on intended Docker hosts, confirm the target host and app name before deploy, recreate, or restart actions, and review the bundled controller before first-time root installation.

Risk: A deployment command can rebuild or restart containers for the wrong app if the requested name is ambiguous.

Mitigation: Use exact deployment names and ask the user to choose when no deployment matches or more than one deployment matches.

## Reference(s):

- [DCC Docker Container Control Skill Homepage](https://github.com/localsplash/dcc-docker-container-control-skill)
- [ClawHub Skill Page](https://clawhub.ai/drodecker/skills/dcc-docker-container-control)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash code blocks and command output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports important command output and final Docker Compose status.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
