## Description: <br>
Adaptive Reasoning helps an agent assess request complexity and adjust reasoning depth before answering. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[enzoricciulli](https://clawhub.ai/user/enzoricciulli) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to help an assistant decide when deeper reasoning is warranted for complex tasks and when fast responses are sufficient for simple requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automatic reasoning escalation can make responses slower and use more tokens. <br>
Mitigation: Install only when automatic deeper reasoning is desired; avoid it for workflows that require reasoning mode to change only by explicit user command. <br>
Risk: Reasoning indicators may be appended to some answers and could conflict with strict formatting expectations. <br>
Mitigation: Review output formatting requirements and remove or override markers where they are not appropriate. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/enzoricciulli/skills/adaptive-reasoning) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, text] <br>
**Output Format:** [Natural-language guidance with optional inline reasoning indicators] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May append reasoning icons for higher-complexity requests and may increase response latency or token use.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
