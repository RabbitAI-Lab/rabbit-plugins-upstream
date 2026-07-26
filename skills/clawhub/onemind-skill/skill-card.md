## Description: <br>
Join the OneMind chat to propose ideas, rate others' propositions on a grid, and collaboratively build consensus on collective decisions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[onemindlife](https://clawhub.ai/user/onemindlife) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to interact with OneMind chats: authenticate anonymously, join the official chat, submit propositions, read round status, and submit one-time batch ratings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create anonymous accounts and submit live OneMind propositions or ratings, which may write real participation data. <br>
Mitigation: Require review and approval of each request URL and payload before writes, and run tests only against authorized environments. <br>
Risk: ClawScan marked the release suspicious because signup, joining, proposing, and rating are live remote actions without enough consent or sandbox safeguards. <br>
Mitigation: Install only when this OneMind interaction is intentional, inspect commands before execution, and avoid production test scripts unless authorized. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/onemindlife/skills/onemind-skill) <br>
- [OneMind Website](https://onemind.life) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with JSON examples and curl command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include live API request examples that require review before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
