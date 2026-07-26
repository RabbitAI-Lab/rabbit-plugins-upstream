## Description: <br>
Control Midea ACs, including turning units on or off, setting temperature, setting fan speed, switching modes, and checking status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iamanorange](https://clawhub.ai/user/iamanorange) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and home-automation operators use this skill to let an agent translate AC control requests into local-network Midea air conditioner commands. It is intended for configured rooms and devices whose IP addresses are known. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Vague requests such as warmer, cooler, or full speed could change a real air conditioner in an unintended way. <br>
Mitigation: Require clarification or confirmation before acting on vague comfort requests, and report the resulting action to the user. <br>
Risk: Incorrect room names or IP addresses could target the wrong local device or fail unexpectedly. <br>
Mitigation: Verify configured room names and AC_IPS entries before use. <br>
Risk: The skill depends on the msmart-ng package and local-network access to Midea AC units. <br>
Mitigation: Install msmart-ng from a trusted source and use the skill only on networks where controlling those devices is intended. <br>


## Reference(s): <br>
- [Midea Air Conditioners ClawHub skill page](https://clawhub.ai/iamanorange/skills/midea-ac) <br>
- [Inspired by hqman's Mijia skill](https://clawhub.ai/hqman/mijia) <br>
- [msmart-ng Python package](https://pypi.org/project/msmart-ng) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and plain-text command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May execute local-network device control commands when the agent is authorized to act.] <br>

## Skill Version(s): <br>
0.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
