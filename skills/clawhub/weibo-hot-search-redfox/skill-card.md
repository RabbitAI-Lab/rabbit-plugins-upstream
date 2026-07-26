## Description: <br>
Fetches current Weibo hot-search topics through RedFox, ranks them with heat scores and links, and helps the agent summarize content angles and risk notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content operators, creators, brand teams, and PR users can use this skill to check current Weibo trending topics, review ranks and heat scores, open related Weibo searches, and generate content-ideation summaries with caution notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a RedFox API key and makes calls to redfox.hk. <br>
Mitigation: Install only if you are comfortable providing a RedFox API key and allowing calls to redfox.hk; keep the key in environment configuration and do not hardcode or expose it. <br>
Risk: The optional daily push feature can create a recurring scheduled task. <br>
Mitigation: Confirm the schedule intentionally before enabling it and make sure you know how to disable the scheduled task in your OpenClaw environment. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/redfox-data/skills/weibo-hot-search-redfox) <br>
- [RedFox API key settings](https://redfox.hk/settings/api-keys?source=clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown response with a ranked table and analysis; the helper script returns JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REDFOX_API_KEY; optional daily push scheduling at a user-confirmed time.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
