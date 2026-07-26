## Description: <br>
Provides TikTok Shop creator profile, shop product, showcase product, shoppable video pre-check, posting, and status workflows through the LinkFox gateway using a creator access token. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External operators and developers use this skill to inspect TikTok creator data, retrieve creator-linked products, and run shoppable video publishing support workflows after obtaining a creator access token. It is intended for LinkFox-mediated TikTok Shop creator API calls, not creator authorization itself. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a LinkFox API key and TikTok creator access token, which can expose creator, shop, and video posting data if used in an untrusted workspace. <br>
Mitigation: Install only when LinkFox is trusted, keep tokens out of shared logs, restrict gateway environment variables, and display creator tokens only in masked form. <br>
Risk: Responses and cached results may persist locally and can include creator or shop data. <br>
Mitigation: Prefer --no-cache for sensitive sessions, review saved JSON files before sharing the workspace, and remove local LinkFox output directories when retention is not needed. <br>
Risk: The workflow can post shoppable videos or send feedback through network APIs. <br>
Mitigation: Require explicit user confirmation before posting videos or sending feedback, and verify TikTok business status codes before treating an operation as successful. <br>


## Reference(s): <br>
- [TikTok Creator API Reference](references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-tiktok-creator) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, JSON, files, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON response summaries; full API responses are written as JSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a 24-hour local cache by default, supports --no-cache, and should mask creator access tokens in displayed output.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
