## Description: <br>
YouTube SERP Scout for agents. Search top-ranking videos, channels, and trends for content research and competitor tracking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aisapay](https://clawhub.ai/user/aisapay) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, content teams, and autonomous agents use this skill to search YouTube results, discover top-ranking videos and channels, and support content research, competitor tracking, trend discovery, keyword research, and audience research. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: YouTube search terms and API-key-authenticated traffic are sent to AIsa's external API. <br>
Mitigation: Use only queries that are acceptable to share externally, and avoid sensitive personal data, secrets, or confidential business plans. <br>
Risk: The skill requires an AIsa API key for requests. <br>
Mitigation: Provide the key through AISA_API_KEY and avoid exposing it in prompts, logs, or shared command history. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aisapay/skills/aisa-youtube-search) <br>
- [OpenClaw homepage](https://openclaw.ai) <br>
- [AIsa API Reference](https://aisa.mintlify.app/api-reference/introduction) <br>
- [Skill documentation](artifact/SKILL.md) <br>
- [README](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON] <br>
**Output Format:** [Markdown guidance with shell commands, Python client examples, and JSON API responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires AISA_API_KEY and sends YouTube search terms through AIsa API requests.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
