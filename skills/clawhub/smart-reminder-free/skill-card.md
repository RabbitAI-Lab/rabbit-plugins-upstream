## Description: <br>
Captures Chinese natural-language event descriptions, stores structured reminder data, applies default reminder offsets, and supports basic schedule queries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent developers use this skill to turn Chinese reminder requests into structured events, reminder schedules, and short schedule-query responses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reminder delivery is under-scoped and the provided Telegram cron example can send event details to a fixed recipient. <br>
Mitigation: Review before installing and do not run the Telegram cron example until the recipient, channel, and consent flow are changed to controlled values. <br>
Risk: Reminder details are stored locally in an events.yml file that may contain personal calendar information. <br>
Mitigation: Protect the events file and avoid Git-syncing it unless the user intentionally wants those calendar details stored in the repository. <br>


## Reference(s): <br>
- [Detailed Reference](references/detail.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with YAML event examples, Python snippets, shell command examples, and plain-text schedule responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local reminder data examples for events.yml and reminder scheduling guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
