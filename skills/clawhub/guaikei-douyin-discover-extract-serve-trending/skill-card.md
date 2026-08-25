## Description:

Searches public Douyin content, retrieves creator posts and video comments, and returns real-time trending lists as structured JSON for short-video research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run Douyin research workflows: keyword search, creator post extraction, comment collection, and real-time trend monitoring for content planning, competitor analysis, and sentiment review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger rules can send vague user requests, Douyin URLs, or identifiers to guaikei.com.

Mitigation: Require explicit Douyin or short-video research intent before invocation, especially for vague requests such as "check this" or "search it."

Risk: Public-result data and sensitive research targets may be saved as local JSON logs.

Mitigation: Tell users when logs are written and delete logs that contain sensitive research targets.

Risk: The security verdict is suspicious because external requests and local result logging are part of normal operation.

Mitigation: Install only when users accept the external data transfer and local logging posture described in the security guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-discover-extract-serve-trending)
- [Guaikei service site](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [json, shell commands, configuration, guidance]

**Output Format:** [JSON CLI output with stderr logs and human-readable command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; results may be saved as local JSON logs.]

## Skill Version(s):

1.0.0 (source: server release metadata, SKILL.md metadata, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
