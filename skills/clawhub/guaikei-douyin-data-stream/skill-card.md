## Description:

This skill helps agents retrieve public Douyin data for keyword search, creator posts, video comments, and real-time trending topics, returning structured JSON for analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to collect public Douyin search, creator, comment, and hot-list data for content planning, competitor analysis, public sentiment monitoring, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Douyin search terms, account or video targets, and the Guaikei API token to www.guaikei.com.

Mitigation: Use the skill only when that external service exposure is acceptable, and avoid submitting sensitive targets or private business queries.

Risk: Collected Douyin data is persisted locally in generated logs without clear retention controls.

Mitigation: Treat logs as sensitive business data, store them appropriately, and clean them up on a defined retention schedule.

Risk: Ambiguous short-video or hot-topic requests can trigger broad data collection behavior.

Mitigation: Confirm intent and scope before using the skill for ambiguous requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-data-stream)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Guaikei service site](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [shell commands, json, guidance]

**Output Format:** [JSON from CLI stdout with logs and prompts on stderr]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; stores JSON logs locally; each request supports up to 10000 public data records.]

## Skill Version(s):

1.0.0 (source: server release evidence, package.json, changelog, and runtime constants)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
