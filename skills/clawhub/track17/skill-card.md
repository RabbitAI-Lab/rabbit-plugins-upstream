## Description: <br>
Track parcels via the 17TRACK API with local SQLite storage, polling, and optional webhook ingestion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tristanmanchester](https://clawhub.ai/user/tristanmanchester) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to add, sync, and summarize parcel tracking records via 17TRACK while keeping a local workspace database. It supports polling by default and optional webhook ingestion when push updates are needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a 17TRACK API token and stores parcel history in the workspace. <br>
Mitigation: Install only if that data handling is acceptable, keep TRACK17_TOKEN secret, and restrict access to the workspace data directory. <br>
Risk: Webhook mode can receive untrusted or invalidly signed payloads that may be stored and applied locally. <br>
Mitigation: Prefer polling unless webhooks are required; when using webhooks, bind the server to localhost or place it behind a trusted endpoint and configure TRACK17_WEBHOOK_SECRET. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tristanmanchester/skills/track17) <br>
- [17TRACK Tracking API v2.2](https://api.17track.net/track/v2.2) <br>
- [17TRACK carrier list resource](https://res.17track.net/asset/carrier/info/apicarrier.all.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with command examples and parcel status summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a 17TRACK API token; command execution may create a local SQLite database and webhook inbox files in the workspace.] <br>

## Skill Version(s): <br>
0.1.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
