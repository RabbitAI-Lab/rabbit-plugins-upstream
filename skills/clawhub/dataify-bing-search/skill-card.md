## Description: <br>
Runs Bing web searches through the Dataify API and returns the API response directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to turn natural-language Bing search requests into Dataify API parameters, confirm the request, and retrieve raw Bing search responses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The debug endpoint override can send the user's Dataify API token to a non-Dataify destination. <br>
Mitigation: Use the fixed Dataify endpoint for normal searches and allow `--url` only for trusted debugging destinations. <br>
Risk: Search location and GPS coordinate parameters may disclose precise user location when included in a request. <br>
Mitigation: Only provide `location`, `lat`, or `lon` when they are needed for the user's search task. <br>
Risk: Persisting a Dataify token in shell profile files can increase credential exposure. <br>
Mitigation: Prefer a temporary `DATAIFY_API_TOKEN` environment variable or a per-run token for live calls. <br>


## Reference(s): <br>
- [Dataify Bing Search API Reference](references/api.md) <br>
- [Dataify Dashboard](https://dashboard.dataify.com?utm_source=skill) <br>
- [ClawHub Skill Page](https://clawhub.ai/dataify-server/skills/dataify-bing-search) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, API calls] <br>
**Output Format:** [Markdown parameter tables, shell command examples, and direct API responses in JSON or HTML.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill requires user confirmation before live API calls and returns the script output without summarizing or post-processing it.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
