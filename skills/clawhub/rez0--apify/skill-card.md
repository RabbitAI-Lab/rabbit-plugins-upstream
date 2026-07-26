## Description: <br>
Run Apify Actors for web scraping, crawling, automation, and structured dataset retrieval through the Apify REST API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rez0](https://clawhub.ai/user/rez0) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to find and run Apify Actors, monitor runs, and retrieve dataset, key-value store, and log outputs. It is intended for web scraping, crawling, search extraction, and other Apify automation workflows that the user has authorized. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Apify token may grant broad account authority beyond simple scraping and result retrieval. <br>
Mitigation: Use a restricted Apify token where available and only provide the token for workflows you intend the agent to perform. <br>
Risk: The skill can guide calls that create or change Apify schedules, webhooks, actors, builds, environment variables, or account limits. <br>
Mitigation: Require explicit user confirmation before allowing account-changing Apify operations. <br>
Risk: Actor runs can access private, internal, or sensitive URLs if the user provides them. <br>
Mitigation: Avoid private or sensitive targets unless the user explicitly confirms the data source and intended handling. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/rez0/apify) <br>
- [Apify API documentation](https://docs.apify.com/api/v2) <br>
- [Apify API OpenAPI spec](openapi.json) <br>
- [Apify Store](https://apify.com/store) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with curl commands and JSON-oriented API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires APIFY_TOKEN and either curl or wget; API results may include JSON, CSV, JSONL, XML, XLSX, RSS, logs, screenshots, HTML, or key-value store records depending on the selected Apify Actor and endpoint.] <br>

## Skill Version(s): <br>
1.0.4 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
