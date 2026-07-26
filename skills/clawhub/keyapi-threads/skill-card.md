## Description: <br>
Discover and analyze Threads users and content through the KeyAPI REST API using live official docs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xyzzero](https://clawhub.ai/user/xyzzero) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and analysts use this skill to turn Threads research requests into KeyAPI workflows for profiles, posts, replies, reposts, comments, and keyword search. It guides agents to verify current KeyAPI documentation before making authenticated live API calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can store a KeyAPI token persistently in shell startup files. <br>
Mitigation: Prefer a current-session KEYAPI_TOKEN or a dedicated secret store, and inspect or remove the managed keyapi-skills shell block when uninstalling or rotating credentials. <br>
Risk: The skill exposes broad live API request capability through helper scripts. <br>
Mitigation: Review requests before execution, confirm scope for broad reports or multi-endpoint workflows, and rely on current KeyAPI documentation for method, path, parameters, and response handling. <br>
Risk: Passing real tokens through command-line arguments may expose credentials in shared shell history or process listings. <br>
Mitigation: Avoid passing production tokens with --token in shared environments; use interactive setup, a current-session environment variable, or a dedicated secret store. <br>


## Reference(s): <br>
- [KeyAPI documentation index](https://docs.keyapi.ai/llms.txt) <br>
- [KeyAPI Threads documentation](https://docs.keyapi.ai/en/threads/) <br>
- [Threads profile search documentation](https://docs.keyapi.ai/en/threads/search_profiles.md) <br>
- [Threads user information documentation](https://docs.keyapi.ai/en/threads/fetch_user_info.md) <br>
- [Threads user posts documentation](https://docs.keyapi.ai/en/threads/fetch_user_posts.md) <br>
- [Threads post detail documentation](https://docs.keyapi.ai/en/threads/fetch_post_detail.md) <br>
- [Global rules](references/global-rules.md) <br>
- [Scenario cards](references/scenarios.md) <br>
- [Routing policy](references/routing-policy.md) <br>
- [Setup and authentication](references/setup-and-auth.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with shell command examples and optional JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call live KeyAPI endpoints through helper scripts and may write response JSON when an output file is requested.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
