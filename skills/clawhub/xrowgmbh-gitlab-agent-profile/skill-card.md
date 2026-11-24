## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GitLab profile owners use the skill to refresh monthly contribution charts and public proof records for an agent profile.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The WebP fallback may download and run an unpinned npm package without approval; the security scan was partial.

Mitigation: Use ImageMagick or an already installed sharp-cli, and review the package before allowing any download or execution.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance and shell commands; generated SVG, WebP, and JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Monthly statistics for completed calendar months, with public records and anonymized private totals.]

## Skill Version(s):

1.152.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
