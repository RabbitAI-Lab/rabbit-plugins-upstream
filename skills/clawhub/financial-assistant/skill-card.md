## Description: <br>
Reads and analyzes financial data already imported into a locally running LittleBeaver Financial Assistant, including statements, metrics, trends, comparisons, payment collections, and local financial Q&A through read-only localhost access. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yk-niu](https://clawhub.ai/user/yk-niu) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and local agents use this skill to answer questions about company financial statements, financial metrics, and period-over-period trends from data the user has already imported into LittleBeaver Financial Assistant. It is intended for local financial lookup and analysis, with explicit company, period, reporting dimension, and unit context in responses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can return private financial report data from the user's local LittleBeaver Financial Assistant instance. <br>
Mitigation: Treat returned financial data as private and avoid sending it to external services unless the user explicitly requests that. <br>
Risk: Implicit invocation may cause the skill to be used for relevant financial questions without a separate confirmation prompt. <br>
Mitigation: Confirm company, period, and reporting dimension when ambiguous, and use only localhost read-only endpoints for retrieval. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/yk-niu/skills/financial-assistant) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Chinese Markdown answers with optional JSON data returned from local read-only API calls.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses should preserve returned units, distinguish missing values from zero, and avoid unsupported trend or causality claims.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
