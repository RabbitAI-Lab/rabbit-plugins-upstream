## Description:

Gov Report Writing helps agents draft, format, and review Chinese public-sector and state-enterprise official documents using GB/T 9704-2012 formatting, report templates, formal vocabulary guidance, and confidentiality checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mogician11111](https://clawhub.ai/user/mogician11111)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, document authors, and agent users working with Chinese public-sector or state-enterprise materials use this skill to draft annual summaries, duty reports, party-building reports, research reports, work plans, meeting minutes, notices, approvals, briefings, and related official-style documents. The skill also guides formatting, terminology review, policy-reference checks, redaction, placeholder use, and final safety reminders.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Users may provide classified, confidential, or internal-only source text.

Mitigation: Avoid submitting sensitive source material; use placeholders or redacted text and stop processing when classified or confidential signals appear.

Risk: Generated policy references, names, dates, or figures may be inaccurate or incomplete.

Mitigation: Review all policy citations, people, departments, dates, and numerical claims before relying on the output.

Risk: Official-document formatting may depend on local fonts and Word-processing behavior.

Mitigation: Run the included DOCX format checker and confirm required fonts and GB/T 9704-2012 layout settings before submission.

## Reference(s):

- [GB/T 9704 Formatting Reference](artifact/references/gb-t9704-format.md)
- [Report Templates](artifact/references/report-templates.md)
- [Vocabulary Guide](artifact/references/vocabulary-guide.md)
- [AI Trace Review Rules](artifact/references/ai-traces.md)
- [Policy Reference Database](artifact/references/policy-database.md)
- [ClawHub Skill Page](https://clawhub.ai/mogician11111/skills/gov-report-writing)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Guidance]

**Output Format:** [Chinese official-document drafts, Word document output guidance, Markdown or HTML alternatives when requested, safety reminders, and DOCX format-check reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses placeholders such as XX for missing or sensitive details and instructs users to review data, dates, names, policy references, and confidentiality before use.]

## Skill Version(s):

1.3.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
