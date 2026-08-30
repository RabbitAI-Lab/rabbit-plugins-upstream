## Description:

A responsible web application security testing rule set and checklist for authorized testing, vulnerability scanning, security assessment, and penetration-test workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mowenqwq](https://clawhub.ai/user/mowenqwq)

### License/Terms of Use:

MIT

## Use Case:

Developers, security testers, and agent operators use this skill to keep authorized web security testing within explicit scope, with authorization checks, minimal impact, evidence logging, restoration, reporting, and review cadence guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent bypass switches can weaken authorization checks or external-site authorization handling.

Mitigation: Remove or disable the mowenfalse, mowenbrokentrue, and mowenwaitrue paths before deployment, and require human-reviewed authorization evidence for each target.

Risk: Contradictory destructive-operation guidance can lead to unsafe execution if backup and explicit authorization requirements are bypassed.

Mitigation: Resolve the Rule 22 backup contradiction before use, keep destructive actions disabled by default, and require explicit scope plus a verified recovery backup.

Risk: Security test reports may contain sensitive target details, credentials, or vulnerability proof.

Mitigation: Store reports only in private user-controlled locations and keep authorization evidence separate from public skill files.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/mowenqwq/skills/web-security-test-rules)
- [GitHub Repository](https://github.com/mowenQWQ/Web-Security-Test-Rules)
- [Authorization Template](references/authorization_template.json)
- [Authorization and Credential Notes](references/auth_notes.md)
- [Destructive Operation Backup Notes](references/backup_notes.md)
- [Security Test Report Template](references/report_template.md)
- [Trusted Public Keys Notes](references/authorized_pubkeys/README.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with checklists, JSON templates, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces process guidance and report structure; does not itself execute tests without an agent applying the rules.]

## Skill Version(s):

1.4.9 (source: SKILL.md frontmatter; ClawHub release version 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
