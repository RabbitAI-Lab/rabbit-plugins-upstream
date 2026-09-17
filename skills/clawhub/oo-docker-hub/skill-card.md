## Description:

Docker Hub operates Docker Hub through an OOMOL-connected account for reading repositories, creating repositories, and managing organization and team data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Docker Hub repository, tag, image, organization, team, member, invitation, and access-token metadata, and to perform confirmed repository and organization administration through an OOMOL-connected Docker Hub account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform Docker Hub write and destructive organization or repository actions.

Mitigation: Confirm the exact target, payload, and effect with the user before running actions marked [write] or [destructive].

Risk: The skill can list organization access tokens and other sensitive account metadata.

Mitigation: Use it only with Docker Hub accounts where the OOMOL connector should have the requested organization permissions, and avoid exposing token details unnecessarily.

Risk: First-time setup includes curl-to-bash and irm-to-iex installer commands.

Mitigation: Run installer commands only after independently trusting and verifying the OOMOL CLI installer source.

## Reference(s):

- [ClawHub Docker Hub Skill](https://clawhub.ai/oomol/skills/oo-docker-hub)
- [Docker Hub](https://hub.docker.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building action payloads; state-changing actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
