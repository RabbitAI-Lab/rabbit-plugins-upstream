## Description: <br>
All-in-one Chinese fortune-telling — BaZi (Four Pillars), ZiWei DouShu, QiMen DunJia, I Ching (Meihua + LiuYao), feng shui, marriage compatibility, plus daily horoscope push to Telegram/Feishu. Built on iztro + lunar-typescript, no external API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiajiaoy](https://clawhub.ai/user/jiajiaoy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use Yunshi to generate Chinese astrology and divination readings, including BaZi, ZiWei DouShu, QiMen DunJia, I Ching, feng shui, marriage compatibility, and daily fortune push content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles exact birth details and optional family-member details in local memory. <br>
Mitigation: Treat profiles as sensitive local data, avoid publishing populated profile content, and delete the yunshi MEMORY.md block when it is no longer needed. <br>
Risk: Daily push can retain horoscope delivery preferences and send recurring content. <br>
Mitigation: Run the push-off command when scheduled delivery is no longer wanted. <br>
Risk: Relationship, health, finance, and legal fortune interpretations can be mistaken for decision-making advice. <br>
Mitigation: Present outputs as entertainment or cultural interpretation, not as a basis for health, legal, financial, or relationship decisions. <br>


## Reference(s): <br>
- [Yunshi ClawHub Skill Page](https://clawhub.ai/jiajiaoy/skills/yunshi) <br>
- [OpenClaw](https://openclaw.ai) <br>
- [Registration Workflow](docs/注册流程.md) <br>
- [Lucky Today Related Skill](https://clawhub.ai/skills/lucky-today) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and local script output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include local MEMORY.md profile blocks, scheduled push directives, and culturally framed fortune interpretations.] <br>

## Skill Version(s): <br>
1.3.1 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
