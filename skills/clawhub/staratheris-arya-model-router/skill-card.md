## Description: <br>
Routes agent requests across cheap, default, pro, and ultra model tiers, with manual overrides, optional briefing for large contexts, feedback-based threshold tuning, and response policy hints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[staratheris](https://clawhub.ai/user/staratheris) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to choose lower-cost model tiers for routine work and escalate heavier tasks to stronger models or sub-agents only when routing rules indicate it is needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Routing rules and thresholds may select a model tier that is too costly or too weak for a specific workflow. <br>
Mitigation: Review model names and thresholds in rules.json, use router auto off or explicit @cheap/@pro overrides when tighter control is needed, and monitor feedback adjustments. <br>
Risk: Brief generation can include sensitive context if the source text contains secrets, private data, or confidential task details. <br>
Mitigation: Review context before briefing and avoid sending sensitive material into generated briefs or sub-agents unless that disclosure is intentional. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Configuration, Guidance, Text] <br>
**Output Format:** [JSON routing decisions plus plain-text briefs and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Routing output includes selected level, model, score, reasons, actions, response policy, and helper script guidance.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
