## Description:

Garmin Nutrition helps an agent log food with a reusable meal and product cache, local journal files, and optional Garmin Connect Nutrition sync, reads, and deletes when the user directs them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weirdei](https://clawhub.ai/user/weirdei)

### License/Terms of Use:

MIT

## Use Case:

External users and their agents use this skill to track meals with cached food patterns, maintain local nutrition journals, and optionally synchronize approved entries to Garmin Connect Nutrition. It is suited for personal food logging workflows where the user understands that nutrition data may be stored locally and sent to Garmin cloud services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Nutrition logs are health-related data and may be uploaded to Garmin Connect when logging without --no-garmin.

Mitigation: Tell users before cloud sync, preview write commands, and use --no-garmin for local-only logging.

Risk: The skill reads cached Garmin OAuth tokens and can delete Garmin food-log entries when the user approves destructive commands.

Mitigation: Install only in trusted environments, review dry-run output, and require explicit confirmation before adding --yes.

Risk: Garmin nutrition endpoints are private and may change behavior.

Mitigation: Rely on the skill's post-write log readback, avoid blind retries on uncertain sync results, and retest pinned dependencies before release updates.

## Reference(s):

- [Garmin Nutrition ClawHub Release](https://clawhub.ai/weirdei/skills/garmin-nutrition)
- [uv Documentation](https://docs.astral.sh/uv/)
- [garmin-pulse Companion Skill](https://github.com/weirdei/garmin-pulse)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; script commands return JSON and write local JSON and Markdown journal files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes are dry-run by default and require explicit approval; Garmin sync can be disabled with --no-garmin.]

## Skill Version(s):

1.1.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
