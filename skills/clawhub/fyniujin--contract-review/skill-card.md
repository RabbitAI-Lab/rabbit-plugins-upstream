## Description:

Reviews Chinese-language contracts to identify clause risks, extract key terms, cite legal bases, and generate structured review reports with suggested revisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Legal, procurement, HR, sales, and business users use this skill to review Chinese contracts before signing or negotiation. It supports risk triage, key-term extraction, legal-basis lookup, version comparison, and report generation, but its output should be reviewed by qualified counsel for important matters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive contract-derived data may be saved under ~/.contract-review.

Mitigation: Use the skill only on systems where local retention is acceptable, protect that directory, and remove retained review history when it is no longer needed.

Risk: Confidential contract content may be transmitted through optional external LLM review or webhook reminders.

Mitigation: Disable LLM review with --no-llm for confidential documents or use a trusted local backend, and configure webhook reminders only to destinations you control.

Risk: Auxiliary negotiation or alignment file ingestion may not have consistent security checks across all paths.

Mitigation: Avoid using those auxiliary ingestion paths with untrusted files until their checks are consistent with the main file validation flow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/contract-review)
- [Skill definition](artifact/SKILL.md)
- [Legal basis reference](artifact/references/legal_basis.md)
- [Compliance checklist](artifact/references/compliance_checklist.md)
- [Contract type definitions](artifact/references/contract_types.yaml)
- [Clause library index](artifact/references/clause_library/clause_index.yaml)
- [Guiding cases index](artifact/references/guiding_cases/index.json)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Files, Guidance]

**Output Format:** [Markdown, JSON, or DOCX reports with structured risk findings, legal references, scores, and suggested revisions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May retain local review history and may use optional LLM or webhook integrations depending on user configuration.]

## Skill Version(s):

5.2.1 (source: server release evidence, frontmatter, pyproject.toml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
