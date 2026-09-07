## Description:

Write formal Chinese government and state-owned enterprise documents including annual reports, work summaries, party-building reports, meeting minutes, and official correspondence following GB/T 9704-2012 standards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mogician11111](https://clawhub.ai/user/mogician11111)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external users drafting Chinese official documents use this skill to generate, polish, format, and check government, state-owned enterprise, and public-sector reports against GB/T 9704-2012 style expectations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may provide classified, confidential, or sensitive internal materials while asking for official-document drafting.

Mitigation: Avoid classified or confidential inputs, desensitize internal materials before use, and stop processing when sensitive signals are detected.

Risk: Broad natural-language triggers may activate the skill for requests that only loosely resemble official-document writing.

Mitigation: Prefer explicit invocation for this skill and confirm the document type when the request is ambiguous.

Risk: Generated drafts may contain placeholders, unsupported policy references, or facts that require organizational verification.

Mitigation: Review all names, dates, data, policy citations, and XX placeholders before submission; use the bundled quality and format checks where appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mogician11111/skills/gov-report-writing)
- [Project homepage](https://github.com/Mogician11111/gov-report-writing)
- [GB/T 9704 format reference](references/gb-t9704-format.md)
- [Report templates](references/report-templates.md)
- [Vocabulary guide](references/vocabulary-guide.md)
- [Expression library](references/expression-library.md)
- [Case examples](references/case-examples.md)
- [AI trace review rules](references/ai-traces.md)
- [Policy database](references/policy-database.md)
- [Polishing guide](references/polishing-guide.md)
- [Capability matrix](references/capability-matrix.md)
- [Quality scoring standard](references/quality-scoring.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Guidance]

**Output Format:** [Chinese official-document drafts, Markdown or DOCX-ready content, and optional quality or format-check command output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses XX placeholders for missing or sensitive fields and includes safety reminders for document review.]

## Skill Version(s):

1.6.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
