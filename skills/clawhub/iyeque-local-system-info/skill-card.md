## Description:

Provides local CPU, memory, disk, load, and bounded process diagnostics to help agents assess capacity and troubleshoot resource contention.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iyeque](https://clawhub.ai/user/iyeque)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use the skill to check local resource availability before demanding tasks and investigate process-level resource contention.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Process names and optional usernames can disclose local activity.

Mitigation: Inspect processes only for troubleshooting and use --include-owners only when username attribution is needed.

Risk: A single resource reading may not reflect sustained availability.

Mitigation: Treat results as point-in-time observations and recheck resources before consequential local work.

## Reference(s):

- [Local System Info release on ClawHub](https://clawhub.ai/iyeque/skills/iyeque-local-system-info)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Point-in-time local metrics; process results contain names and resource usage, with usernames included only on explicit request.]

## Skill Version(s):

1.2.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
