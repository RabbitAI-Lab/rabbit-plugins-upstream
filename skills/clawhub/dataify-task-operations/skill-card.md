## Description: <br>
Continues a Dataify Builder job after submission by checking status, explaining failures, retrieving available results, or reporting a safe handoff when automated retrieval is unavailable. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to follow up on asynchronous Dataify scraper tasks: checking status, retrieving results or links, understanding failures, and handing off to the dashboard when no retrieval tool is installed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses DATAIFY_API_TOKEN to check Dataify task status and retrieve available results. <br>
Mitigation: Use it only in environments where the token is intended for Dataify job follow-up, and keep the token in the environment rather than command-line arguments or logs. <br>
Risk: Task results, cookies, signed URLs, or private result contents may be sensitive. <br>
Mitigation: Do not expose secrets or private result contents in logs; summarize by default while preserving access to raw data. <br>
Risk: Retrying paid or high-volume Dataify tasks can create cost or volume impact. <br>
Mitigation: Require explicit user confirmation before any paid or high-volume retry. <br>
Risk: A task ID alone does not prove task completion. <br>
Mitigation: Check the provider state when tooling is available, preserve unknown states verbatim, and use an explicit dashboard handoff when automated retrieval is unavailable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-task-operations) <br>
- [dataify-server publisher profile](https://clawhub.ai/user/dataify-server) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown status updates, result summaries, failure explanations, handoff guidance, and links when available] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Preserves access to raw data when results are available and avoids exposing tokens, signed URLs, cookies, or private result contents.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
