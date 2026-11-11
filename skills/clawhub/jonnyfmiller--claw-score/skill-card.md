## Description:

Packages and sanitizes agent configuration files, submits them to Atlas for a Claw Score audit, and returns an emailed architecture report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jonnyfmiller](https://clawhub.ai/user/jonnyfmiller)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent builders use Claw Score to submit agent instruction and configuration Markdown, plus workspace structure, to Atlas for architecture scoring, recommendations, and quick wins delivered by email.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive agent configuration files and workspace structure are sent to Atlas for audit.

Mitigation: Install and run only if you are comfortable sharing those files; review and manually redact memory, user, security, identity, and tool configuration before submission.

Risk: The security review says the sanitization claims are overstated and the promised payload preview is not present.

Mitigation: Do not rely on automatic redaction alone; inspect the files selected for submission and remove secrets or personal data before running the workflow.

Risk: The install instructions mention an unpinned npx installer.

Mitigation: Avoid the unpinned installer unless the package source has been independently verified.

## Reference(s):

- [Claw Score on ClawHub](https://clawhub.ai/jonnyfmiller/skills/claw-score)
- [Atlas Audit Landing Page](https://atlasforge.me/audit)
- [AtlasForgeAI on X](https://x.com/AtlasForgeAI)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Terminal status text plus a Markdown-style email report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Email report is described as delivered within 24-48 hours after successful submission.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
