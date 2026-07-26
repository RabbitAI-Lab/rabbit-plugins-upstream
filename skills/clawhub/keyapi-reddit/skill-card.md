## Description: <br>
Analyze Reddit posts, comments, users, subreddits, feeds, rules, settings, and search signals through the KeyAPI REST API using live official docs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xyzzero](https://clawhub.ai/user/xyzzero) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and support agents use this skill to turn Reddit research questions into documentation-guided KeyAPI workflows for post, comment, user, subreddit, feed, search, and trend analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional setup flow stores a KeyAPI token in the user's shell profile. <br>
Mitigation: Use the interactive setup command, treat KEYAPI_TOKEN as a secret, avoid printing or restating tokens, and prefer local environment configuration over passing tokens on the command line. <br>
Risk: Broad reports, repeated requests, or multi-page workflows make live KeyAPI calls and may consume credits. <br>
Mitigation: Confirm report scope, page depth, and requested sections before launching multi-endpoint or paginated workflows. <br>
Risk: API-derived Reddit analysis can mix observed data with model inference. <br>
Mitigation: Separate observed KeyAPI response facts from interpretation in user-facing reports. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xyzzero/skills/keyapi-reddit) <br>
- [KeyAPI documentation index](https://docs.keyapi.ai/llms.txt) <br>
- [KeyAPI Reddit documentation](https://docs.keyapi.ai/en/reddit/) <br>
- [KeyAPI authentication documentation](https://docs.keyapi.ai/overview/authentication#bearer-authentication) <br>
- [Global Reddit KeyAPI rules](references/global-rules.md) <br>
- [Reddit scenario cards](references/scenarios.md) <br>
- [Reddit routing policy](references/routing-policy.md) <br>
- [Setup and authentication](references/setup-and-auth.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with optional shell commands, code snippets, structured analysis, and JSON excerpts from KeyAPI responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May execute live KeyAPI requests when credentials are configured; broad reports can require multiple paginated API calls.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
