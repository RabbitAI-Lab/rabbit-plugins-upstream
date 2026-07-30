## Description: <br>
Classifies agent tasks into 4 risk tiers (GREEN/YELLOW/RED/CRITICAL) <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent orchestrators use this skill to classify code and configuration tasks by risk tier before assignment, verification, parallel execution, or approval decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can activate during broad discussions about risk, classification, safety, verification, or gates. <br>
Mitigation: Use it when classifying concrete code or configuration tasks, and ignore broad activations when no task execution or verification decision is being made. <br>
Risk: Incorrect task classification can lead to insufficient review for high-impact changes. <br>
Mitigation: Escalate uncertain, security-sensitive, data-affecting, irreversible, or production-impacting work to RED or CRITICAL and require the documented review or human approval gates. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-leyline-risk-classification) <br>
- [Clawdis Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline) <br>
- [Heuristic Classifier](modules/heuristic-classifier.md) <br>
- [Readiness Levels](modules/readiness-levels.md) <br>
- [Tier Definitions](modules/tier-definitions.md) <br>
- [Verification Gates](modules/verification-gates.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Configuration] <br>
**Output Format:** [Markdown guidance with risk tier labels, task metadata examples, verification gates, and orchestration patterns] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only skill; produces risk classifications and required controls rather than executing commands.] <br>

## Skill Version(s): <br>
1.9.17 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
