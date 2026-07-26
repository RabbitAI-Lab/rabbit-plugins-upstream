## Description: <br>
Creates personalized daily devotions with verse of the day, pastoral message, structured prayer, and time-aware greetings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[enjuguna](https://clawhub.ai/user/enjuguna) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users invoke this skill to receive a Christian daily devotion that combines a daily verse, pastoral reflection, structured prayer, and time-aware encouragement. It can incorporate prayer context supplied in the initial prompt. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill produces explicitly Christian devotional content that may not fit all users or settings. <br>
Mitigation: Use it only when Christian devotional output is intended and appropriate for the audience. <br>
Risk: Prayer personalization may use sensitive context supplied by the user or already available to the agent. <br>
Mitigation: Avoid including sensitive personal details unless they are needed for the devotion, and review generated prayers before sharing them. <br>
Risk: The skill may contact OurManna to fetch a daily verse. <br>
Mitigation: Allow network access only when the external verse lookup is acceptable, and use the documented fallback behavior if the API is unavailable. <br>
Risk: The optional npm/npx helper package executes code outside the prompt-only skill text. <br>
Mitigation: Review the npm package and execution environment before running helper commands. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/enjuguna/skills/daily-devotion) <br>
- [OurManna Daily Verse API](https://beta.ourmanna.com/api/v1/get?format=json&order=daily) <br>
- [OurManna](http://www.ourmanna.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown devotion with a verse, pastoral reflection, structured prayer, and time-aware greeting.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May personalize prayer content from prompt context, fetch a daily verse from OurManna, and optionally use an npm/npx helper.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
