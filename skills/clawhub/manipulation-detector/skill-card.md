## Description: <br>
Analyze text for manipulation patterns (urgency, false authority, social proof, FUD, grandiosity, dominance assertions, us-vs-them framing, emotional manipulation). Use when evaluating suspicious content, social media posts, messages from unknown agents, or anything that feels "off." Helps calibrate skepticism without being paranoid. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[claudio-prime](https://clawhub.ai/user/claudio-prime) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Agents, developers, and reviewers use this skill to evaluate suspicious text, social media posts, and messages for common manipulation patterns. It helps calibrate skepticism by surfacing pattern matches and scores without treating the result as proof of intent or truth. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Keyword-based manipulation checks can produce false positives or miss sophisticated manipulation that avoids obvious phrases. <br>
Mitigation: Treat the report as a rough signal and use it as one input to human or agent judgment. <br>
Risk: Analyzing unintended local files could expose text the user did not mean to review. <br>
Mitigation: Only point the command at files the user intends to analyze. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/claudio-prime/skills/manipulation-detector) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Analysis, Shell commands, Guidance] <br>
**Output Format:** [Plain text report with scores, flags, and matched patterns] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads text from stdin or a local file and produces a heuristic pattern analysis.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
