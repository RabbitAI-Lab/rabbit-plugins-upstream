## Description:

Helps add consent-gated, company-level website visitor identification to a Cargo-hosted site and keeps company and session records current through Snitcher.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, sales, and engineering teams use this skill to add company-level visitor intelligence to an existing Cargo-hosted website, review the deployment plan, and understand which companies visited and what pages they viewed. It does not identify individual visitors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Third-party visitor tracking may collect data without appropriate consent or disclosure.

Mitigation: Review the privacy disclosure and applicable consent requirements; verify the tracker makes no requests before acceptance or after rejection or withdrawal.

Risk: Usage-based billing can grow with the number of identified companies and has no built-in cap.

Mitigation: Check live Snitcher pricing and Cargo credit balance, review the generated plan, and require explicit approval before deployment.

Risk: Company identification from a shared or masked network can be mistaken for a named visitor or purchasing intent.

Mitigation: Report findings only at company level and qualify counts as visits from identified networks, not individual identities or confirmed buying signals.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/cargo-ai/skills/visitor-identification)
- [Project homepage (listed in skill metadata)](https://github.com/getcargohq/gtm-skills)
- [Consent and site integration guide](artifact/references/consent.md)
- [Visitor data and reporting guide](artifact/references/data.md)
- [Snitcher cookie consent documentation](https://docs.snitcher.com/product/tracker/cookie-consent)

## Skill Output:

**Output Type(s):** [Code, Configuration instructions, Shell commands, Guidance]

**Output Format:** [Markdown with code and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Company-level records and session data become available after the Cargo sync interval; deployment requires operator approval.]

## Skill Version(s):

0.1.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
