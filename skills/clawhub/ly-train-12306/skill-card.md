## Description:

12306 官方接口高铁/火车票余票查询（免费、零配置、多日期对比）

This skill is ready for commercial/non-commercial use.

## Publisher:

[jianbo1110-cjb](https://clawhub.ai/user/jianbo1110-cjb)

### License/Terms of Use:

MIT-0

## Use Case:

External travelers and agents use this skill to check 12306 train availability, schedules, trip duration, and seat-status options across one or more travel dates without login credentials or an API key.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill requires internet access to 12306 and may refresh a local station-code cache.

Mitigation: Run it only where outbound access to kyfw.12306.cn and local cache writes are expected.

Risk: Train availability is live and may change, and 12306 may rate-limit or reject requests.

Mitigation: Confirm final ticket status in the official 12306 website or app and retry later after rate-limit failures.

Risk: The skill checks availability only and does not buy tickets.

Mitigation: Use the official 12306 website or app for purchasing and account-sensitive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jianbo1110-cjb/skills/ly-train-12306)
- [Publisher profile](https://clawhub.ai/user/jianbo1110-cjb)
- [12306 service endpoint](https://kyfw.12306.cn)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Human-readable text with command-line examples and train availability results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include train numbers, stations, departure and arrival times, trip duration, booking status, and seat availability.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
