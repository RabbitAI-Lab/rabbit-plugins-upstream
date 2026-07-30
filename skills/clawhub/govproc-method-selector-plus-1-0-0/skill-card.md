## Description: <br>
A government procurement compliance assistant that helps select or validate lawful procurement methods under China's government procurement framework, including statutory method checks, threshold-sensitive analysis, procedural warnings, and structured reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Procurement, legal, audit, and compliance users use this skill to determine which government procurement method fits a project or to check whether a proposed method is compliant. It supports forward recommendation and reverse validation while reminding users that final approval remains with the appropriate procurement and finance authorities. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Procurement method guidance may be mistaken for legal approval or a final administrative decision. <br>
Mitigation: Treat outputs as compliance analysis only; confirm final procurement method decisions with the purchasing entity, finance authority, procurement/legal team, or other competent reviewer. <br>
Risk: Thresholds and legal requirements are year-sensitive and may change after the skill's embedded knowledge or referenced sources were prepared. <br>
Mitigation: Verify current legal texts, local procurement thresholds, and official catalog standards before relying on a determination. <br>
Risk: Incomplete project facts can lead to an overconfident method recommendation. <br>
Mitigation: Provide required inputs such as procurement object type, budget, location, year, proposed method when relevant, market competition, technical complexity, and urgency; keep determinations conditional when facts are missing. <br>
Risk: Users may ask for help evading procurement rules through bid splitting, fabricated urgency, or unsupported single-source claims. <br>
Mitigation: Follow the skill's stated boundary to refuse unlawful workarounds and provide only lawful compliance explanations and risk warnings. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chesaram/skills/govproc-method-selector-plus-1-0-0) <br>
- [Publisher profile](https://clawhub.ai/user/chesaram) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, guidance] <br>
**Output Format:** [Structured Markdown report with a JSON deliverable] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes procurement method recommendation or compliance verdict, legal basis, condition checks, procedural requirements, red/yellow/blue risk flags, threshold source notes, law-version notes, audit risk level, and a disclaimer.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
