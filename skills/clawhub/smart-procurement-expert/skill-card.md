## Description: <br>
投标人侧招投标与政府采购全周期合规导航助手，覆盖商机甄别、投标决策、任务分解、招标解析、章节初稿生成、文稿润色、图表占位、呈交终审、一致性审查、评标应对、质疑投诉救济与经验沉淀。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External procurement and bid teams use this skill to navigate Chinese tendering and government procurement workflows, prepare structured bid materials, model scoring logic, check substantive consistency, and plan compliant post-bid remedies. The skill supports drafting and analysis, while commercial decisions, legal conclusions, pricing, and final submission approvals remain with the user. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Bid and procurement files may contain sensitive commercial, pricing, or legal information. <br>
Mitigation: Use the skill only with files the user intentionally provides, and install it only where local processing of those files is acceptable. <br>
Risk: Generated bid drafts, compliance analysis, or remedy guidance may be incomplete or unsuitable for a specific procurement matter. <br>
Mitigation: Require human review of drafts, legal/commercial conclusions, and submission decisions before relying on the output. <br>
Risk: Price-score configs and calculated scores can be misread as pricing advice. <br>
Mitigation: Treat price scoring as formula execution against user-confirmed rules and require manual confirmation before any bidding decision. <br>
Risk: An unstructured DOCX parser edge case can fail or produce an incomplete structure. <br>
Mitigation: Review parser output and generated configuration before creating or submitting bid documents, and correct the structure manually when needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chesaram/skills/smart-procurement-expert) <br>
- [Publisher profile: chesaram](https://clawhub.ai/user/chesaram) <br>
- [Two-law domain routing](artifact/references/legal-domains.md) <br>
- [Scoring model methodology](artifact/references/scoring-model.md) <br>
- [DOCX generation methodology](artifact/references/docx-generation.md) <br>
- [Price rule extraction](artifact/references/price-rule-extraction.md) <br>
- [Consistency check methodology](artifact/references/consistency-check.md) <br>
- [Response autofill workflow](artifact/references/response-autofill.md) <br>
- [Knowledge base linkage](artifact/references/kb-linkage.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports, JSON configuration, shell command guidance, and generated DOCX-oriented configuration or files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include draft bid sections, review checklists, scoring tables, price configuration drafts, and explicit user-confirmation markers for legal, pricing, and submission decisions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
