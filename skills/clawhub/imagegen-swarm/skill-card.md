## Description:

Generate or edit images and videos through supported image engines, including an optional pay-per-image API fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ekko237](https://clawhub.ai/user/ekko237)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate or edit images and short videos through supported engines, manage batches and reference images, and configure an optional paid API fallback. It also provides setup guidance for connecting selected engine accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags unverified remote installer guidance and cautions about access to an authenticated Muse session or sandbox escalation.

Mitigation: Review installer commands before running them, grant only the engine access needed, and require explicit approval before sandbox escalation.

Risk: Some executable files were only partially analyzed, so the scan did not assess every executable file fully.

Mitigation: Review the supplied scripts and dependencies before installation or before granting them credentials.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/ekko237/skills/imagegen-swarm)
- [Lovart integration setup repository](https://github.com/lovartai/lovart-skill.git)

## Skill Output:

**Output Type(s):** [Files, JSON, Shell commands, Configuration instructions, Guidance]

**Output Format:** [PNG images, MP4 videos, JSON job and result files, and setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Jobs can select an engine, aspect ratio, reference images, or video mode; output files are written to the chosen directory.]

## Skill Version(s):

1.2.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
