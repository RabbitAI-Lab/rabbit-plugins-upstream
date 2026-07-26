## Description: <br>
Searches and reads X (Twitter) profiles, timelines, mentions, followers, tweet search, trends, lists, communities, and Spaces, and publishes posts after the user completes OAuth in the browser. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[0xjordansg-yolo](https://clawhub.ai/user/0xjordansg-yolo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to search and read Twitter/X data for social listening, profile and tweet analysis, trend monitoring, and competitor intelligence. With user OAuth authorization, it can also publish text, image, video, reply, quote, and threaded posts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The authoritative security evidence says the skill exposes the configured AIsa API key in normal command output. <br>
Mitigation: Install only in trusted environments, avoid sharing command output in logs or transcripts, and redact API keys from status, authorize, and post outputs until the key-output behavior is fixed. <br>
Risk: The authoritative security evidence says ambiguous posting instructions could affect public posts. <br>
Mitigation: Review each requested post, media attachment, reply, quote, and thread relationship before publishing, and do not claim success until the publish command returns a successful result. <br>
Risk: The authoritative security guidance notes that AIsa receives Twitter/X searches, uploaded media, OAuth posting requests, and the configured API key. <br>
Mitigation: Use this skill only when the operator trusts AIsa for those data flows and has permission to submit the requested content and credentials. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/0xjordansg-yolo/skills/openclaw-aisa-twitter-search-post) <br>
- [OpenClaw homepage](https://openclaw.ai) <br>
- [AIsa API reference](https://docs.aisa.one/reference/) <br>
- [Twitter OAuth posting workflow](references/post_twitter.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires AISA_API_KEY; posting requires user OAuth authorization and may return an authorization link before publishing.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
