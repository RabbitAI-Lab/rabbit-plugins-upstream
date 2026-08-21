## Description:

Detects and analyzes indoor plant light stress from images and optional lux data, identifying low or excessive light symptoms and suggesting adjustments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and plant-care agents use this skill to analyze indoor plant images or videos, optionally with lux data, and receive light-stress classification plus care adjustment guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, or supplied URLs are sent to the configured remote analysis service.

Mitigation: Use only media appropriate for that service, avoid sensitive backgrounds, and review endpoint configuration before deployment.

Risk: The skill creates or reuses local identity-linked state and may store tokens in a workspace SQLite database.

Mitigation: Run the skill in a controlled workspace and restrict access to persisted identity or token state.

Risk: History queries can retrieve remote analysis records under the resolved identity.

Mitigation: Enable history lookup only when identity-scoped report retrieval is expected and acceptable.

Risk: The authoritative security verdict is suspicious due to under-disclosed endpoint and persistence behavior.

Mitigation: Require security review of endpoint configuration and persistence behavior before production rollout.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-indoor-plant-light-stress-detect-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON text, with optional saved file output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and history tables when list mode is used.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
