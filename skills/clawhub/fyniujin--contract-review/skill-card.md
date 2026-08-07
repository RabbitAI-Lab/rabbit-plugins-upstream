## Description:

Reviews Chinese contracts for clause risks, key information, and compliance issues, then generates review reports with legal citation traceability, negotiation support, and Chinese-English comparison.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Business, legal, procurement, HR, founders, and contract reviewers use this skill to inspect Chinese-language contracts, compare bilingual versions, prepare negotiation notes, and produce structured risk reports. It is intended to support review workflows and does not replace professional legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Contract text may be sent to the selected external LLM backend.

Mitigation: Use --no-llm or a local Ollama backend for confidential contracts, and review OPENAI_API_BASE before running.

Risk: Review summaries and risk snippets may be stored locally under ~/.contract-review/history.

Mitigation: Treat the local history directory as sensitive data and clear or protect it according to the user's retention policy.

Risk: The skill performs update checks without a strong per-run consent gate.

Mitigation: Run update checks only in environments where outbound version-check traffic is acceptable.

## Reference(s):

- [README](README.md)
- [Report Template](assets/report_template.md)
- [Legal Basis](references/legal_basis.md)
- [Compliance Checklist](references/compliance_checklist.md)
- [Contract Types](references/contract_types.yaml)
- [Risk Rules](references/risk_rules.yaml)
- [Clause Library Index](references/clause_library/clause_index.yaml)
- [Bilingual Glossary](references/bilingual_glossary.yaml)
- [Negotiation Strategies](references/negotiation_strategies.yaml)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Files, Code, Shell commands, Guidance]

**Output Format:** [Markdown, JSON, and generated document files with risk summaries, clause findings, legal bases, revision suggestions, bilingual comparison notes, and negotiation briefs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate local review history and optional Word reports; LLM-backed review is optional and can be disabled.]

## Skill Version(s):

5.0.0 (source: frontmatter, pyproject.toml, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
