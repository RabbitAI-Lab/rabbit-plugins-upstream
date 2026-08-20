## Description:

Reviews Chinese contracts for clause risks, key terms, legal references, amount consistency, multilingual alignment, and structured report generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Business users, legal operations teams, procurement teams, HR staff, founders, and developers use this skill to review Chinese-language contracts, compare versions, identify legal and commercial risks, and generate review reports or suggested revisions. It supports common contract categories including procurement, labor, technology, leasing, financing, equity transfer, NDA, construction, and cross-border trade agreements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Contract text or derived review data may be sent to cloud LLM APIs when optional LLM review is enabled.

Mitigation: Use local-only mode or run with --no-llm for sensitive contracts, and confirm confidentiality rules before enabling external API review.

Risk: Review reports and history can persist sensitive contract-derived information under the user's local profile.

Mitigation: Review retention expectations before use and periodically delete stored history or report files when they are no longer needed.

Risk: The skill includes automatic GitHub update checks and hardware profiling behavior.

Mitigation: Run in an environment where outbound update checks and local hardware inspection are permitted, or disable/check these behaviors before deployment.

Risk: Installer examples include pipe-to-shell commands for third-party tooling.

Mitigation: Install dependencies from verified sources and avoid running pipe-to-shell installer commands without independent review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/contract-review)
- [Skill definition](artifact/SKILL.md)
- [README](artifact/README.md)
- [Legal basis](artifact/references/legal_basis.md)
- [Risk rules](artifact/references/risk_rules.yaml)
- [Contract types](artifact/references/contract_types.yaml)
- [Compliance checklist](artifact/references/compliance_checklist.md)
- [Guiding cases index](artifact/references/guiding_cases/index.json)
- [Clause library index](artifact/references/clause_library/clause_index.yaml)
- [Bilingual glossary](artifact/references/bilingual_glossary.yaml)
- [Ollama download](https://ollama.ai/download)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON, and DOCX reports with risk levels, legal basis, suggested clause revisions, and optional command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local review reports and history records; optional LLM mode can call local Ollama or OpenAI-compatible APIs.]

## Skill Version(s):

5.1.0 (source: frontmatter, pyproject.toml, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
