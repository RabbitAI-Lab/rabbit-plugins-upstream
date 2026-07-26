## Description: <br>
Suki is a Chinese persona and style skill that guides an agent to roleplay an energetic soft-tsundere chat partner, avoid customer-service tone, and optionally coordinate meme or TTS habits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yyh-001](https://clawhub.ai/user/yyh-001) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use Suki to tune supported agents toward a casual Chinese chat persona with short, human-sounding replies instead of assistant or customer-service phrasing. It is also useful when configuring optional meme and TTS behavior through separate host tools. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing the skill intentionally biases the assistant toward a persistent Chinese Suki persona across resets. <br>
Mitigation: Install it only when that persona is desired, and disable or remove it when a neutral assistant style is required. <br>
Risk: Optional companion setup may include a separate agent-expression curl-to-shell install command. <br>
Mitigation: Review the companion installer before running it and install the companion only when meme or media behavior is needed. <br>
Risk: Optional media and TTS behavior can affect what the host agent sends or speaks if those tools are enabled. <br>
Mitigation: Enable companion media and TTS tools selectively, and review generated paths or spoken output during deployment testing. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/yyh-001/skills/suki) <br>
- [Suki Examples](references/examples.md) <br>
- [Suki Short Persona Core](SOUL.md) <br>
- [agent-expression Optional Companion](https://github.com/yyh-001/agent-expression) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Guidance, Configuration] <br>
**Output Format:** [Natural-language chat responses and Markdown guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May optionally guide local meme or TTS behavior only when companion host tools are installed.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and root SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
