## Description:

A Chinese official-document drafting skill for government, state-owned enterprise, public institution, and enterprise report workflows, including formal report templates, GB/T 9704-2012 formatting guidance, terminology checks, polishing guidance, and confidentiality reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mogician11111](https://clawhub.ai/user/mogician11111)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external users use this skill to draft, polish, format, and review Chinese official documents such as annual summaries, duty reports, Party-building reports, research reports, work plans, meeting minutes, notices, requests, replies, and briefing materials. It is intended for non-classified materials and uses placeholders plus review reminders for missing, sensitive, or unverifiable facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Classified or sensitive internal material could be exposed if users paste original source text into an agent conversation.

Mitigation: Use redacted, non-classified inputs only; the skill should refuse classified source material and ask for sanitized content.

Risk: Generated policy wording, names, dates, and numerical claims may be incorrect or unsupported.

Mitigation: Review all generated facts against authoritative source documents before submission or distribution.

Risk: Official-document formatting may not match local filing requirements if required Chinese fonts or Word settings are unavailable.

Mitigation: Verify output with the included format-check guidance and install or configure required fonts before final use.

## Reference(s):

- [README](README.md)
- [GB/T 9704-2012 Formatting Reference](references/gb-t9704-format.md)
- [Report Templates](references/report-templates.md)
- [Vocabulary and Terminology Guide](references/vocabulary-guide.md)
- [Policy Citation Reference](references/policy-database.md)
- [Polishing Guide](references/polishing-guide.md)
- [AI Trace Review Guide](references/ai-traces.md)
- [Format Check Script](scripts/format_check.py)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or structured Chinese document text with optional DOCX formatting guidance and format-check commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses XX placeholders for missing or sensitive details and includes safety, factual review, and font/format reminders.]

## Skill Version(s):

1.4.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
