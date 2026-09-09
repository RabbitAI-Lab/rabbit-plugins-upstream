## Description:

Provides rules and checklists for authorized website and web application security testing, emphasizing authorization, least-impact methods, restoration, reporting, and strict scope control.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mowenqwq](https://clawhub.ai/user/mowenqwq)

### License/Terms of Use:

MIT

## Use Case:

Developers, security testers, and agents use this skill to conduct authorized web security assessments with documented scope, controlled testing methods, restoration steps, and structured findings reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local override switches can weaken authorization checks or destructive-action safeguards.

Mitigation: Enforce authorization outside the skill itself and do not treat mowenfalse, mowenbrokentrue, or mowenwaitrue as proof of permission.

Risk: Security reports and operation logs may contain sensitive target, account, request, or finding details.

Mitigation: Redact sensitive data before sharing or archiving reports and logs, and keep report storage under the authorizing party's control.

Risk: Authorized web security testing can affect systems outside the intended scope if targets or third-party integrations are not checked carefully.

Mitigation: Confirm the approved target list, accounts, methods, time window, and third-party authorization before testing, then stop and re-confirm when scope is ambiguous.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/mowenqwq/skills/web-security-test-rules)
- [README](README.md)
- [Authorization Notes](references/auth_notes.md)
- [Authorization Template](references/authorization_template.json)
- [Trusted Public Keys](references/authorized_pubkeys/README.md)
- [Backup Notes](references/backup_notes.md)
- [Security Report Template](references/report_template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with checklists, configuration examples, JSON authorization templates, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are intended for authorized security testing workflows and should be reviewed before execution.]

## Skill Version(s):

0.2.0 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
