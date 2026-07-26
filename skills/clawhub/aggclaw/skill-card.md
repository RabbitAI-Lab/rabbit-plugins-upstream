## Description: <br>
aggclaw helps agents analyze global ad creatives with AppGrowing Global, select game, non-game, or Inspire modes, and optionally download creative materials from completed sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[youcloud](https://clawhub.ai/user/youcloud) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External marketers, creative strategists, app teams, and game teams use this skill to request global ad creative analysis, compare creative strategies, generate ideation prompts, and retrieve creative materials after an analysis session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Creative-analysis prompts and related session context are sent to AppGrowing/YouCloud using the user's API key. <br>
Mitigation: Avoid confidential campaign plans, client secrets, personal data, and other sensitive material in prompts or follow-up context. <br>
Risk: The skill can download creative assets returned by the AppGrowing/YouCloud service. <br>
Mitigation: Review downloaded files and their usage rights before reuse or redistribution. <br>
Risk: Direct creative download links may contain embedded authorization data and can expire. <br>
Mitigation: Do not share raw download URLs; re-fetch materials through the authenticated materials endpoint when a link expires. <br>


## Reference(s): <br>
- [Usage Examples](references/example.md) <br>
- [AppGrowing Global](https://appgrowing.net/) <br>
- [ClawHub skill page](https://clawhub.ai/youcloud/skills/aggclaw) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown analysis responses with optional local creative asset files and PowerShell examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires YOUCLOUD_API_KEY; analysis requests may wait up to 600 seconds, and materials requests may wait 120 seconds or more.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
