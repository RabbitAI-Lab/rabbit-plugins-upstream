## Description: <br>
Audit-ready decision artifacts for LLM outputs: assumptions, risks, recommendation, and review gating as schema-valid JSON. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sapenov](https://clawhub.ai/user/sapenov) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, teams, and decision makers use this skill to turn review-required prompts into auditable JSON decision records with assumptions, risks, recommendations, and consistency checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated decision records may contain secrets, personal data, or confidential incident details if those details are included in the prompt. <br>
Mitigation: Remove sensitive data before storing or sharing generated artifacts. <br>
Risk: Example outputs may not require review for every high-impact scenario. <br>
Mitigation: Require qualified human review for production rollbacks, access-control, financial, legal, medical, safety, or other high-impact decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/sapenov/skills/dgr) <br>
- [Publisher Profile](https://clawhub.ai/user/sapenov) <br>
- [DGR JSON Schema](artifact/schema.json) <br>
- [DGR Field Guide](artifact/field_guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, guidance] <br>
**Output Format:** [JSON object conforming to schema.json] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes decision metadata, assumptions, risks, recommendation, review gating, and consistency checks.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata and SKILL.md changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
