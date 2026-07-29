## Description: <br>
Provides horoscope lookup, zodiac personality analysis, compatibility reports, and Chinese astrology and divination support through taibu MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yuzhihui886](https://clawhub.ai/user/yuzhihui886) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users ask an agent for daily western horoscope text, zodiac sign details from birth dates, sign compatibility analysis, or supported Chinese astrology and divination readings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Astrology and divination requests may process dates or birth details. <br>
Mitigation: Ask users to provide only the details needed for the requested reading and avoid submitting sensitive personal data. <br>
Risk: Daily horoscope lookup contacts ohmanda.com and can fail or depend on that external service's availability. <br>
Mitigation: Disclose the external lookup, handle failures clearly, and label any fallback horoscope as AI-generated rather than real-time data. <br>


## Reference(s): <br>
- [ohmanda horoscope API](https://ohmanda.com/api/horoscope/{normalized}/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown-style conversational text with optional shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include horoscope, personality, compatibility, or divination guidance; daily horoscope lookup depends on ohmanda.com availability.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
