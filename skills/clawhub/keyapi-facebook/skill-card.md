## Description: <br>
Explore and analyze public Facebook data through the KeyAPI REST API using live official docs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xyzzero](https://clawhub.ai/user/xyzzero) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to resolve public Facebook profile, page, and group identifiers, inspect public details, collect public posts, photos, Reels, and group events, and summarize the returned KeyAPI data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup flow can store a KeyAPI bearer token in a shell profile as plaintext. <br>
Mitigation: Prefer interactive local setup, avoid passing tokens on the command line, review the target shell profile after setup, and rotate any token exposed in shell history. <br>
Risk: Helper commands can send local files to KeyAPI or save full API responses to disk when file-related options are used. <br>
Mitigation: Use file upload and output-file options only when intentionally needed, choose temporary paths for internal analysis, and avoid treating temporary response files as public deliverables. <br>


## Reference(s): <br>
- [KeyAPI docs index](https://docs.keyapi.ai/llms.txt) <br>
- [KeyAPI authentication](https://docs.keyapi.ai/overview/authentication#bearer-authentication) <br>
- [Facebook Rules](references/facebook-rules.md) <br>
- [Global Rules](references/global-rules.md) <br>
- [Routing Policy](references/routing-policy.md) <br>
- [Scenario Cards](references/scenarios.md) <br>
- [Facebook Profile And Page Module Rules](references/facebook-profile-rules.md) <br>
- [Facebook Profile Content Module Rules](references/facebook-profile-content-rules.md) <br>
- [Facebook Group Module Rules](references/facebook-group-rules.md) <br>
- [Setup And Auth](references/setup-and-auth.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, tables, JSON summaries, or concise analytical text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include live KeyAPI response summaries, API method and path details, setup commands, and saved JSON file paths when the user asks for exports.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
