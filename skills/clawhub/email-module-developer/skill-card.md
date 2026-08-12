## Description:

Generates, rewrites, and polishes standardized Chinese campus emails and formal student documents for leave requests, advisor communication, graduation-project updates, internship applications, scholarship statements, class-schedule requests, and campus activity notices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[caroljiang150-ai](https://clawhub.ai/user/caroljiang150-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Students and campus staff use this skill to produce copy-ready Chinese emails, applications, statements, and notices with polite wording, clear structure, and explicit placeholders for missing information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Drafts may include personal academic details, contact information, health context, family information, or other user-provided sensitive content.

Mitigation: Provide only information intended for inclusion, keep optional sensitive details out unless needed, and review the final text before sending.

Risk: A generated draft may retain placeholders or ambiguous dates, recipients, attachments, or approval details.

Mitigation: Replace every `【待填写】` placeholder and verify dates, names, recipients, attachments, and requested actions before use.

Risk: Applications, reports, and internship messages could overstate achievements or imply unverified facts if the input is unclear.

Mitigation: Use only user-confirmed facts and check claims against the underlying school, scholarship, course, or recruiting requirements.

## Reference(s):

- [校园邮件与公文场景模板库](references/templates.md)
- [ClawHub skill page](https://clawhub.ai/caroljiang150-ai/skills/email-module-developer)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Plain text or Markdown Chinese document drafts with subject lines, structured sections, and placeholders]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the `【待填写：字段】` placeholder style for unknown required information and may include optional subject alternatives, attachment lists, or filling tips.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
