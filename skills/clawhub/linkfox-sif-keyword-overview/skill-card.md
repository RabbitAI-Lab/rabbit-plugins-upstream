## Description:

Analyzes Amazon keyword-level competition with LinkFox SIF data, including product counts, estimated search volume, popularity rank, advertising counts, and supply-demand ratio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, e-commerce operators, and their agents use this skill to query LinkFox SIF keyword overview data for a single Amazon marketplace keyword and present competition, demand, and advertising metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LinkFox API calls consume credits and may create paid usage during keyword analysis.

Mitigation: Confirm user intent before high-frequency, repeated, or multi-marketplace calls, and explain that additional calls can consume credits.

Risk: The onboarding flow can collect phone verification details and create payment orders.

Mitigation: Only run account, verification, billing, or payment steps after the user explicitly chooses that specific onboarding action.

Risk: Full API responses are retained locally in the workspace session data.

Mitigation: Tell users where response files are saved and avoid exposing or retaining sensitive keyword research data longer than needed.

Risk: Feedback reporting can send interaction details to a separate external feedback API.

Mitigation: Require confirmation or disable feedback reporting when the user does not want interaction details sent outside the session.

## Reference(s):

- [SIF keyword overview API reference](artifact/references/api.md)
- [Authentication and billing onboarding](artifact/references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-sif-keyword-overview)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, shell commands, and JSON API responses saved to local files or printed to stdout.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single-keyword LinkFox API queries; full API responses are cached and saved under a local linkfox session directory, with stdout summarized for responses larger than 8 KB.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
