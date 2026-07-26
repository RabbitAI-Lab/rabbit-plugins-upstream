## Description: <br>
Perform unit conversions and calculations using GNU Units. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[asleep123](https://clawhub.ai/user/asleep123) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to answer unit-conversion questions by invoking GNU Units from the command line. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The GNU units utility may be unavailable in the user's environment. <br>
Mitigation: Confirm the utility is installed before relying on this skill for conversions. <br>
Risk: Unquoted unit expressions can be interpreted by the shell before reaching GNU Units. <br>
Mitigation: Quote unit expressions when invoking units commands. <br>
Risk: Currency conversions may rely on static definitions and become outdated. <br>
Mitigation: Use a current financial source for exchange-rate-sensitive work. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/asleep123/skills/units) <br>
- [Publisher profile](https://clawhub.ai/user/asleep123) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and conversion results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the GNU units command-line utility.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
