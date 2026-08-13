## Description:

Retrieves Zhihuiya (PatSnap) patent claims data by patent identifier or publication number and helps present claim counts, claim text, and related-family substitutions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

IP professionals, patent analysts, R&D teams, and agents use this skill to retrieve and display patent claims from Zhihuiya (PatSnap) for known patent IDs or publication numbers. It supports single or batch claim lookup, optional family-member substitution, and clear presentation without legal interpretation unless the user asks for analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent identifiers and claim lookup requests are sent to LinkFox/PatSnap.

Mitigation: Use the skill only for patent identifiers you are comfortable sharing with those services, especially when working with sensitive research or competitive analysis.

Risk: The onboarding flow can help manage account login, API-key setup, paid plans, orders, and payment QR codes.

Mitigation: Create orders or payment QR codes only after the user explicitly selects a plan and payment method, and review billing actions before execution.

Risk: Long-lived API keys may be written into shell profile configuration during setup.

Mitigation: Avoid storing long-lived API keys in shared or backed-up shell profiles; use environment management appropriate for the user's machine and access controls.

Risk: Claim responses, cache files, QR images, and session indexes may be stored persistently on disk.

Mitigation: Review the local LinkFox output directory before use and clear stored responses or cache files when they contain sensitive patent research data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-claim-data)
- [API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples, shell commands, and saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Patent claim responses are saved locally under a LinkFox session directory; small responses may also be printed inline, while larger responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
