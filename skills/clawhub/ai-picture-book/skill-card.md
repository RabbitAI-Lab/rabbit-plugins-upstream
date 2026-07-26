## Description: <br>
Baidu Wenku AI picture book helps agents submit story text to Baidu's AI picture-book service, create static or dynamic picture-book video tasks, poll task status, and return generated video URLs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ide-rea](https://clawhub.ai/user/ide-rea) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, content creators, educators, and developers use this skill to turn story prompts or descriptions into static or dynamic AI picture-book videos through Baidu Wenku/Qianfan APIs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Story prompts, task IDs, and generated content are sent to Baidu's external service. <br>
Mitigation: Use the skill only when Baidu processing is allowed for the data, and avoid submitting secrets, sensitive personal data, proprietary drafts, or regulated material unless policy permits it. <br>
Risk: The skill requires BAIDU_API_KEY for authenticated API calls. <br>
Mitigation: Store the API key in approved environment or secret storage and avoid exposing it in prompts, logs, or shared command transcripts. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ide-rea/skills/ai-picture-book) <br>
- [Baidu Qianfan API Base Endpoint](https://qianfan.baidubce.com/v2) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, JSON] <br>
**Output Format:** [Markdown guidance with shell commands and JSON task results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires BAIDU_API_KEY and returns task IDs, task status, and generated video URL fields when available.] <br>

## Skill Version(s): <br>
1.1.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
