## Description:

Search arXiv and, when needed, verify external academic sources to update field beliefs and one primary decision through testable propositions, capability frontiers, explicitly labeled mechanism models, technical options, transition theses, five-dimensional maturity, leading indicators, and a restrained bilingual standalone HTML report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yofine](https://clawhub.ai/user/yofine)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, technical strategists, product leaders, and due-diligence teams use this skill to turn arXiv-centered literature into evidence-bounded field beliefs and one primary research, architecture, product, or investment decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow performs network research and paper retrieval through an arXiv dependency.

Mitigation: Confirm the research scope before use, follow sequential arXiv request limits, and preserve raw responses for auditability.

Risk: The skill saves raw public research responses and local JSON/HTML report files.

Mitigation: Review generated files before sharing, respect each paper's license terms, and avoid including sensitive local notes in report inputs.

Risk: The default report posture is Chinese-first, which may not match every deployment audience.

Mitigation: Request English or another target language before running the workflow when the default language is unsuitable.

Risk: Abstract-only or incomplete corpora can lead to overconfident field conclusions if evidence ceilings are ignored.

Mitigation: Require the schema validation, evidence ledger, explicit coverage gaps, and HTML verification checks before relying on a decision report.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yofine/skills/arxiv-paper-report)
- [Report JSON Schema](artifact/references/report.schema.json)
- [Analysis Rubric](artifact/references/analysis-rubric.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Validated JSON research record and deterministic standalone HTML report, with concise text or Markdown handoff notes when appropriate.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default report language is zh-CN with original English titles preserved; generated reports should include exact arXiv URLs and pass schema, render, and HTML verification checks.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
