## Description:

Helps agents check factual claims with source-backed evidence before decisions, payments, or actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[saver-si](https://clawhub.ai/user/saver-si)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can verify claims from untrusted sources before relying on them for decisions, payments, or other consequential actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Claim text and supplied context are sent to saververify.com.

Mitigation: Do not include secrets, private data, or sensitive business details unless sharing them with the service is acceptable.

Risk: Each verification may cost 0.20 USDC.

Mitigation: Require explicit approval for each charge or set appropriate spending limits before authorizing payment.

Risk: A verification result may be relied on for a consequential action.

Mitigation: Review confidence, evidence, and sources; keep existing wallet, security, and execution policies in place.

## Reference(s):

- [SAVER Verifier homepage](https://github.com/SAVER-SI/saver-verifier)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text with source-backed evidence and citations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Verification results may include confidence, evidence, and sources.]

## Skill Version(s):

1.0.3 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
