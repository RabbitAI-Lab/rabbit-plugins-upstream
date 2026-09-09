## Description:

Audits Python code against an upstream reference to classify original versus derivative work and report matching expressive fragments, exemptions, and risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ffseika0304](https://clawhub.ai/user/ffseika0304)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineering leads, and release reviewers use this skill to compare Python code with an upstream reference before shipping, accepting outside contributions, or validating a clean-room rewrite. It provides local audit findings and remediation guidance for ownership review; it is not legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release includes an optional paid Alipay/x402 workflow and wallet commands.

Mitigation: Require explicit user approval before installing payment tooling, binding a wallet, or running payment commands; review the exact payment package version before use.

Risk: A payment-certification embed path can mark a report as paid without enforcing signature validation.

Mitigation: Treat reports produced by the embed path alone as untrusted unless receipt verification is run independently and succeeds.

Risk: The scanner verdict is suspicious because the payment and wallet workflow is under-disclosed relative to the audit feature.

Mitigation: Present the payment requirement clearly before full-report unlock and keep local audit execution separate from networked payment steps.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ffseika0304/skills/code-ownership-audit)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance, shell commands]

**Output Format:** [Plain text, Markdown, or JSON audit reports with optional shell-command guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preview reports summarize risk counts and categories; full reports include locations, line numbers, detailed findings, fix suggestions, and optional payment receipt certification.]

## Skill Version(s):

1.3.3 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
