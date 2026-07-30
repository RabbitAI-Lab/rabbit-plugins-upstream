## Description: <br>
Segments customers into tiers using business evidence such as transactions, orders, inquiries, effective communications, and recent timing, and explains the basis for each tier. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Business users and customer-management teams use this skill to classify customer lists into core, near-term, nurture, opportunity, paused, or undetermined tiers from supplied business records. It is intended to preserve uncertainty by asking for missing critical inputs and keeping unsupported or conflicting data marked for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Customer records supplied for segmentation may contain sensitive business or personal data. <br>
Mitigation: Use redacted or minimum necessary records and provide only the evidence needed for the requested segmentation. <br>
Risk: Incomplete, conflicting, or unverified evidence can lead to incorrect customer tiers. <br>
Mitigation: Require the parameter status table, keep missing or conflicting items visible, and treat uncertain entries as preliminary or undetermined until reviewed. <br>
Risk: Segmentation output could be mistaken for an automatic update to source records or existing manual classifications. <br>
Mitigation: Treat the output as an analysis or recommendation and do not overwrite manual tiers, responsible-owner assignments, or original records without human confirmation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-segment) <br>
- [Skill rules](artifact/SKILL.md) <br>
- [Examples](artifact/examples.md) <br>
- [Tests](artifact/tests.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Analysis, Guidance] <br>
**Output Format:** [Markdown analysis with a parameter status table, segmentation results, evidence basis, unresolved items, change conditions, and near-term action-pool suggestions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a customer list, customer evidence, and segmentation purpose before producing a formal analysis.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
