## Description:

Helps teams identify companies visiting their website and the pages they read by setting up consent-gated Snitcher tracking and Cargo company and session models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Website operators and developers use this skill to add consent-based, company-level visitor identification to an existing Cargo-hosted website and review the resulting company and session data. It does not identify named individuals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Website visits may be tracked before meaningful consent if the gate is wired incorrectly.

Mitigation: Review the privacy disclosure and verify in a browser that no tracker request occurs before acceptance, after rejection, or after withdrawal.

Risk: Charges per identified company can grow with website traffic.

Mitigation: Confirm the live per-company price and available credits, then obtain operator approval before deployment.

Risk: Deployment changes the website and adds visitor-identification models.

Mitigation: Review the deployment plan and require explicit approval before deploying.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/cargo-ai/skills/visitor-identification)
- [Project homepage (listed in skill metadata)](https://github.com/getcargohq/gtm-skills)
- [Consent and site wiring](references/consent.md)
- [Understanding visitor data](references/data.md)
- [Snitcher cookie consent documentation](https://docs.snitcher.com/product/tracker/cookie-consent)

## Skill Output:

**Output Type(s):** [Code, Configuration instructions, Shell commands, Guidance]

**Output Format:** [Markdown guidance with code and commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Company-level results only; deployment requires explicit operator approval.]

## Skill Version(s):

0.1.1 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
