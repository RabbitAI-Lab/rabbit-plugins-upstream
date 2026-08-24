## Description:

Determine a signature requirement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Delivery operations users use this skill to determine whether a delivery handoff requires a signature from the package class and service level supplied in the request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill's output is operational guidance based only on the package_class and service_level values provided by the user.

Mitigation: Verify decisions against carrier policy or internal delivery rules when exact compliance matters.

Risk: Incorrect or incomplete delivery_request values can produce an incorrect signature requirement.

Mitigation: Confirm that package_class and service_level are present and match the delivery being evaluated before using the result.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wxt-ai/skills/delivery-signature-requirement-identifier)
- [ClawHub Publisher Profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [Boolean result in the requires_signature field]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the package_class and service_level values supplied in delivery_request.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
