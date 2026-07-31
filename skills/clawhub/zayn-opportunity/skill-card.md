## Description: <br>
Assesses customer or project evidence to distinguish ordinary inquiries, test purchases, real projects, and long-term opportunities. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales, customer-management, and business-development users can use this skill to assess user-provided opportunity evidence, identify missing signals, separate facts from assumptions, and decide the next step before advancing a customer or project opportunity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Customer or project details may include sensitive business information. <br>
Mitigation: Use anonymized examples where possible and review business evidence before sharing it with the agent. <br>
Risk: Weak evidence, platform activity, or AI inference could be mistaken for confirmed buying intent. <br>
Mitigation: Require user-provided reliable evidence, preserve conflicts or unverified information, and avoid presenting assumptions as facts. <br>
Risk: Incomplete inputs can lead to premature opportunity conclusions. <br>
Mitigation: Check required parameters first and request missing customer, demand, evidence, or analysis-goal details before issuing a formal conclusion. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-opportunity) <br>
- [README](artifact/README.md) <br>
- [Examples](artifact/examples.md) <br>
- [Tests](artifact/tests.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown with structured findings and status tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should identify parameter completeness, opportunity type, available and missing signals, risks, current stage, and recommended next steps.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
