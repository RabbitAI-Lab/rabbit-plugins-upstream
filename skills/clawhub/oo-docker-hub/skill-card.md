## Description:

Docker Hub lets an agent read repository, tag, image, organization, team, token, and membership data and perform confirmed write or destructive Docker Hub actions through the OOMOL-connected docker_hub connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to manage Docker Hub repositories and organization administration from an agent, including repository creation, metadata lookup, member and team management, and guarded destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the oo CLI through a remote shell or PowerShell installer could execute unverified code.

Mitigation: Use a pinned, verified oo CLI installation method when available, and review the installer source or checksum before installation.

Risk: Organization access-token inventory can expose sensitive administrative information even when retrieved by a read action.

Mitigation: Run token-listing actions only with explicit user intent and limit storage or sharing of returned token metadata.

Risk: Docker Hub write and destructive actions can alter repositories, teams, organization membership, or access.

Mitigation: Confirm the exact action, target namespace, team, user, and payload before execution.

## Reference(s):

- [Docker Hub homepage](https://hub.docker.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-docker-hub)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects returned by the oo CLI.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
