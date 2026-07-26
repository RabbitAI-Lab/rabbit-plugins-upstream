## Description: <br>
Provides an insurance claims workflow reference framework covering case intake, document handling, medical review, liability assessment, settlement checks, fraud screening, adjudication, and closure communication. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gechengling](https://clawhub.ai/user/gechengling) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Insurance claims professionals use this skill as a structured reference for claims intake, material analysis, medical review, liability assessment, settlement review, fraud risk checks, adjudication support, and customer communications. Outputs require human review before any real-world claims decision or operational action. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may involve broad access to customer, medical, claims-system, credential, notification, closure, archival, and logging workflows. <br>
Mitigation: Use only in a controlled insurance-operations environment with approved tools, secure secret management, intentionally granted and monitored permissions, and a documented logging and retention policy. <br>
Risk: Case registration, notification, closure, and archival actions can affect real claims workflows. <br>
Mitigation: Require explicit human approval before those actions and review outputs before relying on them for operational decisions. <br>
Risk: Live API keys or other secrets could be exposed if pasted into chat. <br>
Mitigation: Do not paste live API keys into chat; use managed secret storage and scoped credentials. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gechengling/skills/claim-expert-digital-employee) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance, structured report templates, JSON examples, and inline shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires human review; some workflows assume approved insurance operations tools and controlled access to claims, policy, notification, calculation, and archival systems.] <br>

## Skill Version(s): <br>
2.1.1 (source: target metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
