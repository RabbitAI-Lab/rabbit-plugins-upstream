## Description: <br>
YouTube SERP Scout for agents. Search top-ranking videos, channels, and trends for content research and competitor tracking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[0xjordansg-yolo](https://clawhub.ai/user/0xjordansg-yolo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, agents, and content research teams use this skill to query YouTube search results through AIsa for content planning, competitor tracking, trend discovery, keyword research, audience research, and SEO analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to the third-party AIsa API. <br>
Mitigation: Avoid submitting secrets, personal data, or confidential business research terms. <br>
Risk: The skill uses an AISA_API_KEY and pay-as-you-go API credits. <br>
Mitigation: Use a dedicated, revocable API key and monitor usage or credit consumption. <br>
Risk: YouTube search results can vary by time, country, language, and API response format. <br>
Mitigation: Review returned results before using them for business decisions or automated reporting. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/0xjordansg-yolo/skills/openclaw-aisa-youtube-search-serp-video-channels-trends-content-tracking) <br>
- [OpenClaw](https://openclaw.ai) <br>
- [AIsa](https://aisa.one) <br>
- [AIsa API Reference](https://aisa.mintlify.app/api-reference/introduction) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown guidance with bash commands, Python client examples, and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, python3, and a user-provided AISA_API_KEY; API responses include YouTube search result data and usage cost fields.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
