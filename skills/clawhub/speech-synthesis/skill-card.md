## Description: <br>
一个集成了Microsoft Edge高质量语音合成能力的MCP服务器，支持多语言语音生成、音频合并和云端存储。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to generate Microsoft Edge TTS speech audio from text, including multi-segment conversations that can be merged into one MP3 or returned as separate outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill saves the XiaoBenYang API key in a local plaintext .env file. <br>
Mitigation: Use a low-privilege API key, restrict local file access, rotate the key if exposed, and remove the key from .env when the skill is no longer needed. <br>
Risk: Speech text is sent to the remote XiaoBenYang API. <br>
Mitigation: Avoid confidential, regulated, or high-value text unless the publisher clarifies endpoint handling, retention, and storage behavior. <br>
Risk: Server evidence reports unavailable provenance and documentation/provenance mismatches. <br>
Mitigation: Review the artifact contents, publisher profile, and security summary before deployment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/alinklab/skills/speech-synthesis) <br>
- [XiaoBenYang API Key Portal](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API Endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Files, Text] <br>
**Output Format:** [JSON API response describing generated speech audio, with MP3 outputs or cloud storage references when returned by the service.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires XBY_APIKEY; supports merged MP3 output or separate generated speech items.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
