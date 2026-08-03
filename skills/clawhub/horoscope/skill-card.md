## Description: <br>
Provides zodiac horoscopes, personality analysis, compatibility checks, and Chinese traditional fate-reading workflows through taibu MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yuzhihui886](https://clawhub.ai/user/yuzhihui886) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent builders use this skill to answer Chinese-language horoscope requests, look up zodiac signs from dates, compare zodiac compatibility, and route traditional Chinese astrology questions to configured taibu MCP tools. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Daily horoscope queries send the normalized zodiac sign to ohmanda. <br>
Mitigation: Tell users when an external horoscope lookup is being used and avoid sending unnecessary personal data. <br>
Risk: Bazi, ziwei, and similar traditional astrology requests may send birth details to the configured taibu MCP service. <br>
Mitigation: Ask only for details needed to complete the request and remind users to avoid exact personal birth information unless they trust the configured service. <br>
Risk: Horoscope and astrology outputs may be mistaken for factual, professional, or deterministic advice. <br>
Mitigation: Present results as astrology-oriented guidance or entertainment, and avoid framing them as medical, legal, financial, or safety-critical advice. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yuzhihui886/skills/horoscope) <br>
- [Ohmanda horoscope API](https://ohmanda.com/api/horoscope/{sign}/) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Plain text or Markdown-style text with Unicode symbols and lists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call local JSON-backed scripts and, for daily horoscopes or taibu workflows, configured external services.] <br>

## Skill Version(s): <br>
1.0.1 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
