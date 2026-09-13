## Description:

论文降重服务，0.01元/次，AI智能改写降低重复率，保持原意不变

This skill is ready for commercial/non-commercial use.

## Publisher:

[2789-bin](https://clawhub.ai/user/2789-bin)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to submit Chinese academic-paper text for paid AI rewriting that aims to reduce repetition while preserving the original meaning, arguments, data, and logic.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted paper text is sent to a paid external endpoint.

Mitigation: Avoid submitting confidential, unpublished, regulated, or proprietary writing unless the publisher provides clear privacy, retention, and payment-consent terms.

Risk: The bundled script disables HTTPS certificate and hostname verification.

Mitigation: Require normal TLS identity checks before relying on the service for sensitive or production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/2789-bin/skills/paper-rewrite)
- [Publisher profile](https://clawhub.ai/user/2789-bin)
- [Service endpoint](https://192.144.154.90/demo/a2m/resource)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [JSON response containing rewritten text, errors, or payment-required details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Input text is truncated to 30000 characters; the service may require a 0.01 CNY payment before returning results.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
