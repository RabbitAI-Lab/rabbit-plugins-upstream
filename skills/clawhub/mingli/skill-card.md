## Description: <br>
Mingli (命理) provides multi-system daily horoscopes using Western astrology, Ba-Zi / Four Pillars, numerology, and I Ching, with optional AstronomyAPI transit data and Telegram delivery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lukebaze](https://clawhub.ai/user/lukebaze) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users use this skill to set up personalized horoscope profiles, generate on-demand horoscope readings, and schedule recurring Telegram horoscope delivery. Developers or operators can also use its scripts to calculate chart, Ba-Zi, numerology, I Ching, and planetary-position inputs for those readings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores exact birth details, location/timezone information, derived chart data, and a Telegram chat ID for recurring horoscope use. <br>
Mitigation: Install only when this local profile storage is acceptable, and use the remove command when the profile and daily job should be deleted. <br>
Risk: Recurring Telegram delivery can send personal horoscope content to the wrong destination if the chat ID or schedule is incorrect. <br>
Mitigation: Verify the Telegram destination and delivery schedule during setup before enabling recurring delivery. <br>
Risk: AstronomyAPI credentials are used for transit data. <br>
Mitigation: Use limited AstronomyAPI credentials and rotate or revoke them if the environment is shared or no longer trusted. <br>


## Reference(s): <br>
- [AstronomyAPI Reference](references/astronomyapi-reference.md) <br>
- [Horoscope Prompt Template](references/horoscope-prompt-template.md) <br>
- [I Ching 64 Hexagrams](references/i-ching-64-hexagrams.json) <br>
- [Zodiac Reference](references/zodiac-reference.md) <br>
- [AstronomyAPI](https://api.astronomyapi.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON script outputs and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include locally stored birth details, location and timezone data, derived chart data, Telegram chat IDs, and scheduled delivery configuration.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter says 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
