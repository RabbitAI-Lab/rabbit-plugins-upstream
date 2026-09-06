## Description:

Review a rendered interface with an isolated committee of orthogonal visual experts for UI audits, responsive and theme checks, edge-state coverage, screenshot-based accessibility review, adversarial finding validation, and optional fix-and-recapture loops.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antreasantoniou](https://clawhub.ai/user/antreasantoniou)

### License/Terms of Use:

MIT

## Use Case:

Developers and product teams use Visual QA before releases or after layout changes to capture representative UI states, run independent screenshot-based reviews, synthesize findings, and optionally verify scoped fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive UI screenshots may expose personal data, account identifiers, access tokens, or private project context.

Mitigation: Use synthetic fixtures for sensitive projects, keep real-account captures outside version control, and choose approved capture and review environments.

Risk: Fix mode can grant an agent authority to edit application code.

Mitigation: Use review mode by default; enable fix mode only with explicit authority, disjoint file scopes, reviewed diffs, and recapture of affected states.

Risk: Screenshot review cannot prove DOM semantics, keyboard behavior, screen-reader output, backend correctness, network behavior, or runtime performance.

Mitigation: Route non-visual claims to appropriate accessibility, interaction, API, network, or performance tests.

## Reference(s):

- [Visual QA ClawHub skill page](https://clawhub.ai/antreasantoniou/skills/visual-qa)
- [Heimdall browser/API test project](https://github.com/AntreasAntoniou/heimdall)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with structured findings, manifest validation commands, proposed diffs when fix mode is explicitly authorized, and recapture instructions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses screenshot manifests and project adapters; review mode does not authorize implementation by default.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
