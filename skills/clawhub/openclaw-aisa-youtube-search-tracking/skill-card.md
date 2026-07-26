## Description: <br>
YouTube SERP Scout for agents. Search top-ranking videos, channels, and trends for content research and competitor tracking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aisadocs](https://clawhub.ai/user/aisadocs) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, marketers, and content teams use this skill to query YouTube search results through AIsa for content research, competitor tracking, trend discovery, keyword research, and audience analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends YouTube search terms and request parameters to the external AIsa service. <br>
Mitigation: Install only when use of AIsa as the search provider is acceptable for the intended workflow. <br>
Risk: The skill requires AISA_API_KEY for authenticated API calls. <br>
Mitigation: Treat AISA_API_KEY as a secret and avoid exposing it in logs, transcripts, shared prompts, or checked-in configuration. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/aisadocs/skills/openclaw-aisa-youtube-search-tracking) <br>
- [OpenClaw Homepage](https://openclaw.ai) <br>
- [AIsa API Reference](https://aisa.mintlify.app/api-reference/introduction) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, code, shell commands, configuration, guidance] <br>
**Output Format:** [JSON API responses with Markdown documentation, curl examples, and Python command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl or python3 and the AISA_API_KEY environment variable.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
