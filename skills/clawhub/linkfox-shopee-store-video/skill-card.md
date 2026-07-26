## Description: <br>
Provides agent workflows and Python entry points for authorized Shopee store video publishing, editing, deletion, listing, and performance analytics through the LinkFox Shopee developer proxy. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External merchants, e-commerce operators, and developers use this skill to manage videos and analyze video performance for authorized Shopee shops after LinkFox and Shopee authorization are configured. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform high-impact Shopee store video actions, including publishing, editing, and deleting videos. <br>
Mitigation: Use only with authorized shops and confirm destructive operations, especially delete_video, before running commands. <br>
Risk: Complete API responses are saved locally and may include store, video, or analytics data. <br>
Mitigation: Run the skill in an appropriate workspace, restrict access to saved linkfox data, and clear saved response files when they are no longer needed. <br>
Risk: The skill requires LinkFox API credentials and a separate Shopee store authorization skill. <br>
Mitigation: Verify LINKFOX_AGENT_API_KEY or LINKFOXAGENT_API_KEY and the linkfox-shopee-store-auth dependency before use, and avoid exposing credentials in prompts or logs. <br>
Risk: Security evidence flags the release as suspicious because high-impact actions and local response persistence do not have enough guardrails. <br>
Mitigation: Review commands and parameters before execution and avoid automatic retries or exploratory calls that could consume credits or change store state. <br>


## Reference(s): <br>
- [Skill API reference](references/api.md) <br>
- [Shopee Open Platform video module index](https://open.shopee.com/documents/v2/v2.video.get_cover_list?module=129&type=1) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-video) <br>
- [Publisher profile](https://clawhub.ai/user/linkfox-ai) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, json, files, guidance] <br>
**Output Format:** [Markdown guidance with Python or curl commands, JSON API responses, and local JSON response files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Small responses print in full; larger responses print summaries while complete responses are saved under linkfox/<date>/<session>/data.] <br>

## Skill Version(s): <br>
1.0.3 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
