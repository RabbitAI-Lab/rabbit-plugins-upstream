## Description:

Low-friction food tracking - a pattern cache of the user's usual meals, a local-first journal, and Garmin Connect Nutrition as a sync target.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weirdei](https://clawhub.ai/user/weirdei)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to log meals with minimal friction, maintain a local nutrition journal, and optionally sync food entries to Garmin Connect Nutrition. It is useful when common dishes or packaged foods can be cached once and reused for fast meal logging.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use cached Garmin account tokens to read sensitive nutrition data and can change Garmin food entries when confirmed.

Mitigation: Review the skill before installing, protect cached Garmin tokens, use `--no-garmin` for local-only logging, and reserve `--yes` for entries the user has confirmed.

Risk: Corrections can clean up prior Garmin entries and the Garmin nutrition endpoints are private, so a failed or uncertain write may require review before retrying.

Mitigation: Check the script's JSON result after writes, verify Garmin entries when output reports an uncertain state, and avoid blind retries that could duplicate entries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weirdei/skills/garmin-nutrition)
- [Publisher profile](https://clawhub.ai/user/weirdei)
- [uv documentation](https://docs.astral.sh/uv/)
- [garmin-pulse companion skill](https://github.com/weirdei/garmin-pulse)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands; the helper script emits JSON and local journal files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write local JSON and Markdown journal files and can optionally sync entries to Garmin Connect when confirmed.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
