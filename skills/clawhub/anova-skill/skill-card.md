## Description: <br>
Control Anova Precision Ovens and Precision Cookers (sous vide) via WiFi WebSocket API. Start cooking modes (sous vide, roasting, steam), set temperatures, monitor status, and stop cooking remotely. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dodeja](https://clawhub.ai/user/dodeja) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent prepare Anova oven or sous-vide cooker commands, monitor device status, and stop active cooking sessions through the Anova cloud API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can remotely start or stop a real heating appliance and change cooking temperature. <br>
Mitigation: Require explicit user confirmation before any start, stop, or temperature-changing command. <br>
Risk: The skill may act on an unintended Anova device if device selection is not verified. <br>
Mitigation: Verify the exact target device before executing cooking or stop commands. <br>
Risk: Unbounded or casual prompts could request unsafe cooking settings. <br>
Mitigation: Apply reasonable temperature, duration, fan, and humidity bounds before execution. <br>
Risk: The websockets dependency is declared with a broad minimum version. <br>
Mitigation: Pin a reviewed websockets version before regular use. <br>


## Reference(s): <br>
- [Anova Developer Portal](https://developer.anovaculinary.com) <br>
- [Anova WiFi Device Controller Reference](https://github.com/anova-culinary/developer-project-wifi) <br>
- [Anova Skill Repository Listed in Metadata](https://github.com/dodeja/anova-skill) <br>
- [ClawHub Skill Page](https://clawhub.ai/dodeja/skills/anova-skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash commands and command-line arguments] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a local Python environment, the websockets package, internet access, and an Anova personal access token stored outside the skill.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release evidence; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
