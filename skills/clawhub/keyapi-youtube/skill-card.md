## Description: <br>
Analyze YouTube videos and channels through the KeyAPI REST API using live official docs for video metadata, comments, replies, streams, related videos, Shorts and video search, trends, channel metadata, channel videos, ID and URL conversion, and search suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xyzzero](https://clawhub.ai/user/xyzzero) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and content research teams use this skill to turn natural-language YouTube questions into documentation-guided KeyAPI REST workflows. It supports live lookup, ranking, search, comparison, and reporting across videos, comments, Shorts, trends, channels, and related YouTube entities. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a KeyAPI bearer token and its setup helper can persist the token in shell startup files. <br>
Mitigation: Prefer a session-scoped KEYAPI_TOKEN or a secret manager; avoid persistent profile storage on shared machines and never paste, print, log, or commit the token. <br>
Risk: The live API helper can read query, body, and image files and can write full API responses to a chosen output path. <br>
Mitigation: Use only trusted, non-sensitive input files and write outputs only to a workspace or temporary path the user controls. <br>
Risk: Broad reports or repeated requests can make many live KeyAPI calls and may consume quota or expose more request context than intended. <br>
Mitigation: Resolve current docs first, scope pagination and fan-out before execution, and confirm broad multi-endpoint reports with the user. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xyzzero/skills/keyapi-youtube) <br>
- [KeyAPI documentation index](https://docs.keyapi.ai/llms.txt) <br>
- [KeyAPI YouTube documentation](https://docs.keyapi.ai/en/youtube/) <br>
- [KeyAPI authentication documentation](https://docs.keyapi.ai/overview/authentication#bearer-authentication) <br>
- [Scenario Cards](references/scenarios.md) <br>
- [Global Rules](references/global-rules.md) <br>
- [Setup And Auth](references/setup-and-auth.md) <br>
- [YouTube Rules](references/youtube-rules.md) <br>
- [YouTube Video Module Rules](references/youtube-video-rules.md) <br>
- [YouTube Channel Module Rules](references/youtube-channel-rules.md) <br>
- [YouTube Search And Trends Module Rules](references/youtube-search-trends-rules.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional JSON from helper scripts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May make live KeyAPI requests and write full JSON responses when an explicit output file is supplied.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
