## Description: <br>
Search YouTube videos, channels, and playlists through the AIsa YouTube relay with one API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bibaofeng](https://clawhub.ai/user/bibaofeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and agents use this skill to search YouTube videos, channels, and playlists through the AIsa relay without managing Google credentials. It supports discovery workflows that need query expansion, locale filters, or pagination through a single API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: YouTube search queries are sent to api.aisa.one for processing. <br>
Mitigation: Use the skill only for searches that are acceptable to process through the AIsa relay, and avoid private or sensitive queries. <br>
Risk: The skill requires an AISA_API_KEY in the environment. <br>
Mitigation: Store the API key in the agent runtime's secret or environment management system and avoid exposing it in prompts, logs, or shared command output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bibaofeng/skills/aisa-youtube-search) <br>
- [Publisher profile](https://clawhub.ai/user/bibaofeng) <br>
- [AIsa homepage](https://aisa.one) <br>
- [AIsa YouTube search endpoint](https://api.aisa.one/apis/v1/youtube/search) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text] <br>
**Output Format:** [Markdown with inline bash commands and API request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires AISA_API_KEY and sends search queries to api.aisa.one.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
