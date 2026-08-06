## Description:

Chinese-language private-domain commerce operations skill for routing and producing WeChat Moments posts, group messages, welcome scripts, market research snapshots, diagnosis, reports, and customer archive workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maojiebc](https://clawhub.ai/user/maojiebc)

### License/Terms of Use:

MIT

## Use Case:

Operators, consultants, and small business teams use this skill to choose the next private-domain commerce action, draft compliant customer-facing copy, investigate market facts with evidence, and continue work from local customer archives.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can save and later reread customer consultation details from local plaintext archives under the user's home directory.

Mitigation: Review sensitive details before saving, prefer explicit archive commands such as /siyu-save and /siyu-restore, and remove or redact confidential information before creating archives or reports.

Risk: The update workflow can reinstall the publisher's package when the user asks to update the skill.

Mitigation: Run update commands only when the user explicitly requests an update, and review the publisher package before deploying updated behavior in sensitive environments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/maojiebc/skills/majia-siyu)
- [Project Homepage](https://github.com/maojiebc/majia-siyu-team)
- [GitHub Releases](https://github.com/maojiebc/majia-siyu-team/releases)
- [Beginner Tutorial](references/新手教程.md)
- [Full Setup Guide for Business Owners](references/整盘怎么搭-老板版.md)
- [WeChat Compliance Redlines](modules/wechat-compliance-redlines/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with optional shell commands, local file paths, and structured checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May route to packaged subskills; save and report workflows may create local plaintext Markdown archives under ~/.siyu when explicitly triggered.]

## Skill Version(s):

1.2.8 (source: frontmatter metadata, ClawHub release, README version history)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
