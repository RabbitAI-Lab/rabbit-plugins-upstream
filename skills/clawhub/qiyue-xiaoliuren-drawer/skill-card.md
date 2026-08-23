## Description:

Uses QiyueAstro's public Xiao Liu Ren API to cast a time-based reading and return the selected palace, original verse, and counting path without adding model-generated interpretation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bloodymarygg](https://clawhub.ai/user/bloodymarygg)

### License/Terms of Use:

MIT-0

## Use Case:

External users ask an agent to perform a quick Xiao Liu Ren divination for immediate questions, lost items, travel timing, or near-term decisions. The skill calls the public QiyueAstro API and returns the selected palace, verse, and counting path for entertainment and self-exploration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Question text and optional date are sent to qiyueastro.com when the skill casts a reading.

Mitigation: Avoid sending sensitive personal, medical, financial, relationship, or other confidential details in the question field.

Risk: The skill appends a link back to QiyueAstro after results.

Mitigation: Treat the link as an external destination and make the transition clear to users.

Risk: The public API may be unavailable or rate-limited.

Mitigation: Tell users to retry later or visit QiyueAstro directly when the API is unreachable, and retry only once after a rate-limit response.

## Reference(s):

- [QiyueAstro](https://qiyueastro.com)
- [QiyueAstro Xiao Liu Ren public API](https://qiyueastro.com/api/v1/openclaw/xiaoliuren)
- [ClawHub skill listing](https://clawhub.ai/bloodymarygg/skills/qiyue-xiaoliuren-drawer)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Guidance]

**Output Format:** [Markdown text summarizing a JSON API response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes the selected palace, original verse, counting path, and a QiyueAstro call-to-action; does not provide independent AI interpretation.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
