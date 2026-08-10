## Description: <br>
Jiying is a multi-agent trust infrastructure skill for orchestrating knowledge work with constitution-as-code checks, a trusted execution protocol, quality gates, and audit-oriented review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vane1981](https://clawhub.ai/user/vane1981) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers and teams use this skill to run a local multi-agent workflow that plans, researches, creates, reviews, and exports knowledge-work outputs while applying trust, quality, and audit checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API key handling is not documented in detail. <br>
Mitigation: Use a restricted DeepSeek API key if possible, avoid hardcoding or committing it, and confirm how credentials are stored before regular use. <br>
Risk: Running npm install, the local server, or Electron mode executes third-party application code. <br>
Mitigation: Review the project before installation and run it in a controlled local environment appropriate for third-party tools. <br>
Risk: Audit logs and indexed knowledge may contain sensitive workflow content. <br>
Mitigation: Check where logs, indexed knowledge, and credentials are stored, and avoid sensitive inputs until retention and storage behavior are understood. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/vane1981/skills/jiying) <br>
- [Project portfolio](https://vane1981-2011.github.io/jiying/portfolio/) <br>
- [Review report](https://vane1981-2011.github.io/jiying/portfolio/稽影系列_参赛作品_复核报告.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands, API endpoint descriptions, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include locally generated review outputs, audit records, and exported knowledge-work artifacts depending on the configured workflow.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
