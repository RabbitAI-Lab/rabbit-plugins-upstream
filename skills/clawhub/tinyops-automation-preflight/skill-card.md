## Description:

Audits public webpages for automation and integration readiness through TinyOps paid preflight services, returning evidence-backed readiness findings, prioritized integration risks, or acceptance checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tinyopsstudio](https://clawhub.ai/user/tinyopsstudio)

### License/Terms of Use:

MIT

## Use Case:

Developers and automation engineers use this skill to evaluate public web pages before building or validating workflow integrations. It helps summarize readiness evidence, prioritize integration risks, and request an acceptance pack when a structured launch checklist is needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends a target public URL and optional objective text to TinyOps/RapidAPI or the x402 service.

Mitigation: Use only public, unauthenticated, non-sensitive URLs and avoid including secrets, session tokens, customer data, or credential-bearing links.

Risk: The skill can initiate paid requests for readiness analysis or acceptance-pack results.

Mitigation: Verify live payment requirements and obtain explicit user authorization for the exact purchase before any paid request.

Risk: The result is readiness evidence, not an end-to-end integration proof or vulnerability scan.

Mitigation: Present findings with uncertainty, distinguish observed evidence from recommendations, and use separate testing or security review for those purposes.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/tinyopsstudio/skills/tinyops-automation-preflight)
- [TinyOps x402 OpenAPI document](https://x402-preflight.tinyopsstudio.com/openapi.json)
- [Automation Integration Preflight API on RapidAPI](https://rapidapi.com/tinyopsstudio/api/automation-integration-preflight)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples and optional structured JSON reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include readiness labels, evidence summaries, prioritized gaps, next actions, acceptance tests, and raw structured responses when requested.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
