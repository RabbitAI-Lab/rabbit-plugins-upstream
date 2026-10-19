## Description:

Independently checks external factual claims in agent research, reports, or other tool outputs using web evidence and cited sources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[saver-si](https://clawhub.ai/user/saver-si)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agents use this skill to obtain a cited second check of factual claims before relying on them. It is not intended for wallet security, transaction simulation, or arithmetic.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Claims or optional context sent to an external verification service may contain sensitive information.

Mitigation: Send only information approved for external disclosure; exclude secrets, wallet recovery data, and sensitive personal information.

Risk: Paid verification can incur charges, including for results with insufficient evidence.

Mitigation: Require explicit approval or a bounded spending policy before signing a payment; do not automatically pay again after a lost response.

Risk: A cited verdict may still misinterpret sources or be mistaken for authorization to take action.

Mitigation: Inspect cited sources and use dedicated tools and existing execution policies for high-impact decisions.

## Reference(s):

- [SAVER Verifier homepage](https://saververify.com)
- [Verification tool schema](https://saververify.com/agent-tool.json)
- [Paid verification examples](https://saververify.com/examples.json)
- [ClawHub skill listing](https://clawhub.ai/saver-si/skills/saver-verifier)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown with a verification verdict and cited sources]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report insufficient evidence.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
