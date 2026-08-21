## Description:

Produces Qi Men Dun Jia time charts for a specified date or the current time, showing the yin/yang dun bureau, Zhi Fu, Zhi Shi, stems, Kong Wang, Yi Ma, summary lines, and nine-palace chart data from QiyueAstro.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bloodymarygg](https://clawhub.ai/user/bloodymarygg)

### License/Terms of Use:

MIT-0

## Use Case:

External users ask an agent to fetch and present a Qi Men Dun Jia chart for timing, direction, or self-exploration questions. The skill formats QiyueAstro API results and avoids independent fortune interpretation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Question text and optional date are sent to qiyueastro.com when the skill calls the external chart API.

Mitigation: Do not include sensitive personal, financial, medical, or confidential details in the question field.

Risk: Users may treat chart output as decision guidance beyond the skill's stated entertainment and self-exploration purpose.

Mitigation: Present the returned chart data without adding independent fortune interpretation, and preserve the source-provided framing.

## Reference(s):

- [QiyueAstro](https://qiyueastro.com)
- [QiyueAstro Qi Men Dun Jia API](https://qiyueastro.com/api/v1/openclaw/qimen)
- [ClawHub skill page](https://clawhub.ai/bloodymarygg/skills/qiyue-qimen-drawer)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [Markdown text containing returned chart fields, summary lines, and nine-palace entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a disclosed external API; no API key, login, local file access, or persistence is required by the skill.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
