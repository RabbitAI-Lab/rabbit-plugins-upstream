## Description: <br>
AI Insurance Advisor helps mainland China users with insurance planning, product comparisons, premium estimates, coverage gap analysis, compliance-aware underwriting guidance, claims questions, sales copy, and agent training scripts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mnetfairy](https://clawhub.ai/user/mnetfairy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users in mainland China use the skill to analyze personal or family insurance needs, compare insurance products, estimate premiums, design coverage plans, and draft insurance-related education or sales materials. Insurance agents may also use it for training scripts and compliance-aware customer conversations. <br>

### Deployment Geography for Use: <br>
Mainland China <br>

## Known Risks and Mitigations: <br>
Risk: Insurance recommendations and premium estimates may be stale or incomplete because the skill relies on static bundled product data. <br>
Mitigation: Verify current prices, availability, terms, exclusions, and suitability with the insurer or a licensed insurance professional before buying. <br>
Risk: The skill may suggest an insurance sales contact if the user asks for contact details. <br>
Mitigation: Treat any contact suggestion as optional and verify advice independently before sharing personal information or purchasing coverage. <br>
Risk: Insurance planning output may not account for all user-specific health, financial, legal, or regional factors. <br>
Mitigation: Use the output as preliminary guidance and review final coverage decisions against current policy documents and professional advice. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Insurance knowledge reference](artifact/references/insurance-knowledge.md) <br>
- [Compliance reference](artifact/references/compliance.md) <br>
- [Insurance product data](artifact/references/products.json) <br>
- [Product data validation report](artifact/references/validation_report_20260524_090219.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Chinese Markdown responses, with JSON produced by bundled local helper scripts for needs analysis, premium calculation, and plan design.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses static bundled product data and should be treated as preliminary insurance guidance rather than a binding quote or professional suitability determination.] <br>

## Skill Version(s): <br>
1.8.420 (source: server release evidence; artifact frontmatter lists 1.8.351) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
