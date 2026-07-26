## Description: <br>
Screen Activity Tracker Lite helps an agent start, stop, summarize, and search scheduled macOS screen activity tracking that captures screenshots, analyzes them with a configured vision model endpoint, and logs results to local Markdown. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zeject](https://clawhub.ai/user/zeject) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to keep a searchable local record of screen activity and generate daily summaries from periodic screenshots. It is intended for macOS workflows where the user explicitly wants screen tracking, local Markdown logs, and configurable vision-model analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Periodic full-screen screenshots can capture passwords, private messages, customer data, or other sensitive information. <br>
Mitigation: Run tracking only when appropriate, pause it before sensitive work, keep retention short, and delete stored screenshots and Markdown logs when they are no longer needed. <br>
Risk: Screenshots may be analyzed through the configured HTTP vision-model endpoint. <br>
Mitigation: Prefer a localhost-only or otherwise trusted endpoint, and disable or remove remote analysis unless the endpoint and its data handling are acceptable. <br>
Risk: Users may not notice that tracking continues on a schedule. <br>
Mitigation: Confirm the cron job status before and after use, document how to stop tracking, and verify stored data locations before installing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zeject/skills/screen-activity-tracker-lite) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Markdown, Guidance] <br>
**Output Format:** [Markdown guidance with JSON cron requests and bash command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates local Markdown activity logs and screenshot files under the configured output directory.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
