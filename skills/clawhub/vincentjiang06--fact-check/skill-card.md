## Description: <br>
Fact Check gives a fast, source-backed answer to a factual question or claim within a bounded time budget. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vincentjiang06](https://clawhub.ai/user/vincentjiang06) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to quickly verify factual questions or claims with bounded web search and return a concise cited answer. It is intended for bottom-line fact checks, not exhaustive research reports or subjective recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Fast web-search answers can be incorrect or stale if source quality is weak. <br>
Mitigation: Use the skill's source bars, freshness checks, citations, confidence labels, and uncertain path instead of guessing. <br>
Risk: The release does not include server-resolved GitHub import provenance. <br>
Mitigation: When publisher provenance matters, review the ClawHub publisher profile and the external source named in the security guidance before deployment. <br>
Risk: Citation structure can be incomplete even when the answer prose looks plausible. <br>
Mitigation: Run scripts/check_answer.mjs on saved answers when practical to confirm the required answer structure and resolving citations. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/vincentjiang06/skills/fact-check) <br>
- [SKILL.md](SKILL.md) <br>
- [Triage rules](rules/triage.md) <br>
- [Search protocol](rules/search-protocol.md) <br>
- [Output contract](rules/output-contract.md) <br>
- [Source reliability and freshness](references/source-reliability.md) <br>
- [Metrics](references/metrics.md) <br>
- [Answer template](assets/answer-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, shell commands] <br>
**Output Format:** [Markdown with a bottom-line answer, confidence label, tier, cited evidence bullets, numbered sources, and optional caveats.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses simple and complex time budgets; optional structural validation is available through scripts/check_answer.mjs.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
