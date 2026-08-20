## Description:

Analyzes pet training videos or video URLs by calling backend APIs to compare observed posture against Sit, Down, and Stay commands, report timing and success, and support non-medical training feedback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use this skill to evaluate whether a pet follows training commands in uploaded or URL-based videos. It returns posture-command match results, response timing, structured reports, and report links for training review without providing medical diagnosis or behavior therapy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Training videos or video URLs are sent to a Life Emergence/Open API backend for analysis.

Mitigation: Install only when backend processing is acceptable, use appropriate training videos, and avoid passing unrelated local paths.

Risk: The skill silently creates or reuses a local identity and can persist tokens or identity data for report history.

Mitigation: Use a contained workspace and review or clear data/smyx-api-key.txt and the local SQLite user database when identity or token reuse is not desired.

Risk: The security scan verdict is suspicious because of backend login/report calls and local token handling.

Mitigation: Review the security summary and guidance before deployment and restrict installation to environments where these behaviors are acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-training-command-execution-analysis)
- [Pet training command execution API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON analysis report with optional saved file output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include command name, command timestamp, observed pet posture, posture match score, response latency, execution status, intervention suggestion, and report link.]

## Skill Version(s):

1.0.9 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
