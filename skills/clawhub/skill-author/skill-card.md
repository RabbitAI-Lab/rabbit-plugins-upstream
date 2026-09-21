## Description:

Author, harden, and publish agent skills for ClawHub by writing skills that conform to ClawHub conventions, running pre-publish hardening, and remediating clawhub.ai security-audit findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sunshinejnjn](https://clawhub.ai/user/sunshinejnjn)

### License/Terms of Use:

BSD-3-Clause

## Use Case:

Developers and skill publishers use this skill to create, harden, remediate, publish, and verify ClawHub agent skills against ClawHub conventions and audit findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent through broad file edits and command execution while authoring, remediating, or publishing another skill.

Mitigation: Confirm the target skill directory, review proposed edits before applying them, and approve publishing commands explicitly.

Risk: Audit remediation may change code, configuration, or documentation in ways that affect published behavior.

Mitigation: Review the finding-to-fix mapping, run the skill's own checks, and scan the package before publishing.

Risk: Temporary-directory cleanup examples can remove files if adapted carelessly into automation.

Mitigation: Scope cleanup commands to a known skill-specific temporary path and inspect the path before deletion.

## Reference(s):

- [skill-author ClawHub page](https://clawhub.ai/sunshinejnjn/skills/skill-author)
- [ClawHub Skill Authoring Conventions](references/authoring-guide.md)
- [Publish Checklist](references/publish-checklist.md)
- [ClawHub Audit Pattern Fix Mapping](references/audit-patterns.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command examples and edit recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include file edits and ClawHub CLI commands when approved by the user.]

## Skill Version(s):

1.1.0 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
