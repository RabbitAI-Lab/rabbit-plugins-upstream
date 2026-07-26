## Description: <br>
Decision Architect helps agents structure high-stakes choices with framework matching, cognitive-bias checks, risk-profile learning, and decision retrospectives. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, product managers, and decision owners use this skill to compare options, surface potential cognitive biases, record decision rationale, and run later retrospectives. It is intended for product, technical, business, personal, high-risk, irreversible, or audit-sensitive decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks agents to persist decision history and risk-profile memory while declaring only read access. <br>
Mitigation: Review and explicitly approve any local write behavior before installation or use; prefer a read-only configuration unless storage locations and retention are documented. <br>
Risk: The input schema mentions callback_url even though the skill claims no network use. <br>
Mitigation: Avoid callback_url unless network behavior, destination approval, and payload limits are documented and approved. <br>
Risk: Stored decision history and risk-profile files may contain sensitive personal, product, business, or technical context. <br>
Mitigation: Treat local memory files as sensitive data, avoid storing credentials or regulated data, and review retention and access controls before use. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/decision-architect) <br>
- [Skill Homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown guidance with structured decision analysis, bias findings, confidence labels, and retrospective notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May request or maintain local decision history, risk-profile, and retrospective files when the host agent permits file writes.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
