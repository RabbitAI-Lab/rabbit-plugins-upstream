## Description:

Provides local CPU, memory, disk, load, and bounded process diagnostics to help agents assess capacity and troubleshoot resource contention.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iyeque](https://clawhub.ai/user/iyeque)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can ask an agent to check local resources before demanding tasks or investigate CPU, memory, disk, and process usage during troubleshooting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Process diagnostics may reveal process names and usernames.

Mitigation: Request process listings only when needed for troubleshooting and share them only with the intended recipient.

## Reference(s):

- [Local System Info on ClawHub](https://clawhub.ai/iyeque/skills/iyeque-local-system-info)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown with JSON diagnostic results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only, point-in-time results; process listings are limited to 1–100 entries.]

## Skill Version(s):

1.2.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
