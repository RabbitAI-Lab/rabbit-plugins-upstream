## Description:

Derives account-merge guidance, merges an account revision into a local record, and optionally submits the result to a configured endpoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Account operations teams and developers use this skill to set field-merge rules, apply an account revision, and save the merged record locally. They can optionally submit the result to a configured delivery endpoint.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured external delivery can submit merged account data without a separate confirmation step.

Mitigation: Leave delivery endpoints and credentials unset unless submission is intended; inspect any delivery-config file before running.

Risk: Local output may contain account data.

Mitigation: Use a dedicated output directory with appropriate access controls.

## Reference(s):


## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON result and local account-merge artifact]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a local effect receipt and, when delivery is configured, an external delivery receipt.]

## Skill Version(s):

1.2.0 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
