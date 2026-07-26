## Description: <br>
Analyze Twitter/X content through the KeyAPI REST API using live official docs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xyzzero](https://clawhub.ai/user/xyzzero) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and social media teams use this skill to turn Twitter/X research requests into documentation-verified KeyAPI workflows for tweets, profiles, timelines, search, trends, communities, lists, jobs, Spaces, and social graph analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A KeyAPI token can be exposed if it is pasted into chat, printed, or passed through shell history with a command-line token flag. <br>
Mitigation: Prefer the interactive setup command, avoid printing or restating KEYAPI_TOKEN, and review the managed shell-profile entry created by setup. <br>
Risk: Twitter/X lookup queries and returned data are sent to KeyAPI for live API execution. <br>
Mitigation: Use the skill only when KeyAPI processing is acceptable for the intended data, and scope requests to the minimum useful query and result depth. <br>
Risk: Broad follower, following, or social-graph reports can trigger many live API calls and collect large relationship datasets. <br>
Mitigation: Confirm page depth, report sections, and clear limits before broad graph workflows. <br>


## Reference(s): <br>
- [KeyAPI docs index](https://docs.keyapi.ai/llms.txt) <br>
- [KeyAPI Twitter docs](https://docs.keyapi.ai/en/twitter/) <br>
- [KeyAPI bearer authentication](https://docs.keyapi.ai/overview/authentication#bearer-authentication) <br>
- [Global rules](references/global-rules.md) <br>
- [Scenario cards](references/scenarios.md) <br>
- [Routing policy](references/routing-policy.md) <br>
- [Twitter/X rules](references/twitter-rules.md) <br>
- [Twitter/X content module rules](references/twitter-content-rules.md) <br>
- [Twitter/X profile and social module rules](references/twitter-profile-social-rules.md) <br>
- [Twitter/X community and network module rules](references/twitter-community-rules.md) <br>
- [Setup and auth](references/setup-and-auth.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown analysis, JSON/API response summaries, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can provide concise reports, tables, raw JSON on request, and setup or API commands.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
