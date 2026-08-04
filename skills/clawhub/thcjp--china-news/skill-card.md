## Description: <br>
Aggregates Chinese-source news and returns news items, summaries, status, and execution logs for agent workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, employees, and developers can use this skill in an agent to retrieve and summarize China-focused news or information by date, channel, keyword, or source. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill declares local command execution while its stated news task does not clearly require broad shell access. <br>
Mitigation: Review the skill before installation, run it in a sandbox, and allow only commands that are necessary for the requested news retrieval workflow. <br>
Risk: The artifact includes broad programming and deployment language unrelated to China news retrieval, which can make routing and expected behavior ambiguous. <br>
Mitigation: Prefer or publish a narrowed version whose instructions focus on news retrieval, source handling, summarization, and error handling. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/china-news) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, guidance] <br>
**Output Format:** [Markdown or JSON news results with summaries and execution status] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include execution logs, status metadata, retries, and error details.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
