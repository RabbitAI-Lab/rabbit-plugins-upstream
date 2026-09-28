## Description:

Screens text for safety and disclosure risks and identifies AI agents from User-Agent strings using Overwing Atlas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[frod27](https://clawhub.ai/user/frod27)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to screen incoming or outgoing text, choose whether to block, redact, review, or allow it, and assess claimed AI crawler identities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Screened text and optional context are sent to Overwing.

Mitigation: Submit only necessary content and avoid unrelated secrets or sensitive context.

Risk: Signup credentials and API authentication require care.

Mitigation: Use a unique signup password, protect the API key, and control any OVERWING_BASE_URL override.

Risk: The optional MCP package introduces a supply-chain dependency.

Mitigation: Review or pin the package before running it through npx.

Risk: Safety verdicts and User-Agent claims may be uncertain or spoofed.

Mitigation: Review uncertain or consequential decisions with a human and check the reported verification class.

## Reference(s):

- [Overwing skill release](https://clawhub.ai/frod27/skills/overwing)
- [Overwing homepage](https://overwing.ai)
- [Overwing API documentation](https://overwing.ai/docs)
- [Overwing Atlas](https://overwing.ai/atlas)

## Skill Output:

**Output Type(s):** [Guidance, Text]

**Output Format:** [Text or Markdown summaries of JSON verdicts and agent lookup results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include recommended actions, per-rule findings, confidence, and agent verification classes.]

## Skill Version(s):

1.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
