## Description:

Analyzes pet ear, scratching, or head-shaking videos or images to produce visual observations about ear-canal color, discharge, earwax accumulation, abnormality alerts, and check-up or veterinary follow-up suggestions without providing a medical diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, pet families, boarding centers, and veterinary pre-screening workflows use this skill to analyze pet ear media for structured visual health observations, abnormality alerts, and report links. The skill supports local file or URL input and historical report lookup through its remote service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media and report data may be uploaded to remote services.

Mitigation: Use only non-sensitive media until the publisher documents data handling, retention, and service endpoints clearly.

Risk: The skill may silently create or reuse an account identity and query cloud report history.

Mitigation: Review account identity behavior before use and avoid real accounts unless the identity and history-access model is acceptable.

Risk: Reusable service tokens may be stored locally.

Mitigation: Install only in a controlled workspace, inspect local token storage, and require protected or avoided token persistence before production use.

Risk: Some configured endpoints use HTTP defaults.

Mitigation: Require HTTPS-only service URLs before using the skill with sensitive household imagery or production data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-ear-health-snapshot-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)
- [Shared analysis API reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured analysis text, with optional saved output files and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May query cloud history and return report export links; analysis output is visual-reference guidance, not a veterinary diagnosis.]

## Skill Version(s):

1.0.9 (source: server release evidence; artifact frontmatter lists 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
