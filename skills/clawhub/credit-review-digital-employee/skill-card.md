## Description: <br>
Provides a credit review reference framework covering admission rule scans, risk planning, case intake review, collateral risk management, related-party transaction detection, pre-loan analysis, and review memoranda. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gechengling](https://clawhub.ai/user/gechengling) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Credit review employees and banking risk teams use this skill to structure admission checks, intake validation, pre-loan risk analysis, collateral and related-party review, visit memoranda, and risk-planning tasks for loan applications. Outputs are reference materials that require qualified human review before use in real credit decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may be used with sensitive customer, credit, banking, public-record, and collateral data in an operational credit-review workflow. <br>
Mitigation: Use it only where data access, retention, audit logging, and human approval controls are explicitly authorized. <br>
Risk: Server security review says the skill under-discloses sensitive API access, stored notes or audit logs, and workflow-gating behavior. <br>
Mitigation: Review deployment integrations before installation and require manual approval for external-system access, retained records, or gating decisions. <br>
Risk: Generated analyses could be mistaken for final credit decisions or regulated financial, legal, or compliance advice. <br>
Mitigation: Treat outputs as reference materials and require qualified credit, risk, and compliance reviewers before business action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gechengling/skills/credit-review-digital-employee) <br>
- [Publisher profile](https://clawhub.ai/user/gechengling) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Guidance] <br>
**Output Format:** [Markdown reports and structured JSON task plans] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reference-only credit review outputs, report sections, missing-data prompts, and audit-log structures; requires human review.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
