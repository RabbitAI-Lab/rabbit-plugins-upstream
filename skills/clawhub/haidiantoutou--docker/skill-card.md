## Description:

Provides Docker guidance for containers, images, Compose stacks, networking, volumes, debugging, production hardening, and common commands used to keep environments stable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haidiantoutou](https://clawhub.ai/user/haidiantoutou)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill for practical Docker and Docker Compose guidance, including build reliability, runtime behavior, logs, ports, volumes, networking, and production security posture.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Docker commands can change running containers, published ports, images, volumes, and host disk state if copied without review.

Mitigation: Review each suggested Docker command before execution, especially image pulls, port publishing, cleanup, prune, and volume commands.

Risk: Container exposure or supply-chain drift can occur when services bind publicly or images are not pinned.

Mitigation: For production, bind local-only services to 127.0.0.1 when appropriate and pin images by version or digest.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/haidiantoutou/skills/docker)
- [Skill Homepage](https://clawic.com/skills/docker)
- [Essential Commands](artifact/commands.md)
- [Image Building Traps](artifact/images.md)
- [Compose Traps](artifact/compose.md)
- [Infrastructure Traps](artifact/infrastructure.md)
- [Security Traps](artifact/security.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Docker command examples and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Docker CLI availability when suggested commands are executed]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter and _meta.json report 1.0.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
