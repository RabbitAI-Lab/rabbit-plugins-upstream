## Description:

Summarizes local OpenClaw session logs to report task durations, tool and skill usage, model activity, and token consumption.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT

## Use Case:

OpenClaw users and developers use this skill to review local agent usage, identify slow tools, and compare task durations and token consumption across agents and models.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reading local session logs for all agents exposes potentially sensitive usage metadata; JSON exports can include session IDs, tool and model metadata, and cost fields.

Mitigation: Grant access only to the intended local logs, use the summary report by default, and restrict access to any JSON export.

Risk: Scheduled report announcements can send usage metadata to an unintended destination.

Mitigation: Enable scheduled delivery only when requested and check the announce or push destination before sending.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-usage-report)
- [Project documentation](https://github.com/dtsola/xiaoyaoclaw-usage-report)
- [Usage report design](docs/DESIGN.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Plain-text usage report or optional JSON export, summarized for the user in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports aggregated task, token, model, tool, skill, and daily usage statistics; duration estimates are approximate.]

## Skill Version(s):

1.0.3 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
