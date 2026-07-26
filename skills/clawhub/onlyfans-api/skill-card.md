## Description: <br>
Query OnlyFans data and analytics through OnlyFansAPI.com, including revenue summaries, model performance, Free Trial and Tracking Link conversion analytics, and link earnings comparisons. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[martingalovic](https://clawhub.ai/user/martingalovic) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External creators, agencies, and their agents use this skill to query OnlyFansAPI.com for account revenue, model rankings, earnings breakdowns, and link conversion analytics across connected accounts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can query sensitive OnlyFans account, revenue, subscriber, and link-performance analytics. <br>
Mitigation: Install only when this access is intended, protect ONLYFANSAPI_API_KEY, prefer a least-privilege or read-only key if available, and keep requests scoped to the needed report. <br>
Risk: Generated curl commands can make authenticated network requests. <br>
Mitigation: Review commands before execution, especially if a command targets a domain other than app.onlyfansapi.com or tries to read local files. <br>


## Reference(s): <br>
- [OnlyFansAPI Docs](https://docs.onlyfansapi.com) <br>
- [OnlyFansAPI Console](https://app.onlyfansapi.com) <br>
- [OnlyFans API Access on ClawHub](https://clawhub.ai/martingalovic/skills/onlyfans-api) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, API Calls, Shell commands, Guidance] <br>
**Output Format:** [Markdown with tables and inline bash/curl commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Formats currency to two decimal places, percentages to one decimal place, and includes total rows for multi-model summaries.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact metadata: 1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
