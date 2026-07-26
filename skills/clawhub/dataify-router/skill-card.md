## Description: <br>
Routes broad web research, search, scraping, monitoring, media, marketplace, social, travel, jobs, maps, and competitive-intelligence requests to the smallest suitable Dataify workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agents use this skill to translate outcome-based data collection requests into the smallest Dataify capability plan, then execute or hand off search, web unlocking, scraping, and task lifecycle steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: High-volume, media-download, or asynchronous Builder jobs may create unexpected cost, scope, or completion-state issues. <br>
Mitigation: Confirm source coverage, scope, and cost drivers before those jobs, and return Builder task IDs and asynchronous state through the task lifecycle workflow. <br>
Risk: Dataify workflows use DATAIFY_API_TOKEN and may route broad research or scraping requests across multiple sources. <br>
Mitigation: Read the token from the environment only, never print it, and review the planned source coverage before execution. <br>


## Reference(s): <br>
- [Dataify capability map](artifact/references/capability-map.md) <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-router) <br>


## Skill Output: <br>
**Output Type(s):** [text, guidance] <br>
**Output Format:** [Concise text or markdown summaries with source coverage, important limitations, and asynchronous task state when relevant.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Raw output is provided only when requested; DATAIFY_API_TOKEN should not be exposed in commands or responses.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
