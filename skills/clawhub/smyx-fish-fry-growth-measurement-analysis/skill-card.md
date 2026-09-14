## Description:

Measures fish fry body length and growth rate from periodic tank images or video that include a known-size reference object, then returns structured growth statistics, curve data, alerts, recommendations, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External aquaculture operators, ornamental fish breeders, laboratory users, and developers can use this skill to analyze fry tank images or videos with a calibration object, estimate body length and growth trends, query prior reports, and produce structured management guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads media to configured remote services and queries identity-linked cloud report history.

Mitigation: Use only media approved for those services, confirm remote data handling with the publisher, and avoid private or regulated imagery until handling and retention are documented.

Risk: The skill can create or reuse a local identity and store bearer-style tokens in a shared SQLite database.

Mitigation: Run it in an isolated workspace or account, restrict access to the workspace data directory, and rotate or remove stored tokens after evaluation.

Risk: The authoritative security verdict is suspicious and calls out endpoint, identity-scope, and token-persistence concerns.

Mitigation: Do not use it in production until the publisher documents data handling, scopes identity use, protects or avoids local token persistence, and moves defaults to HTTPS production services.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-fry-growth-measurement-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Files, Guidance]

**Output Format:** [Markdown or JSON structured report with report links; optional saved output file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a local media file path or media URL for analysis, or --list for history queries; supports basic, standard, and json detail levels.]

## Skill Version(s):

1.0.9 (source: server release evidence and target metadata; artifact frontmatter says 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
