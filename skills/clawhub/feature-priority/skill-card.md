## Description:

Helps prioritize Amazon product feature improvements using review frequency, user impact, and product information; it is not for sales prediction, budget approval, or automated purchasing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Product managers, operators, and developers use this skill to rank Amazon product improvement opportunities from available review evidence and product details. It guides the agent through authorization, profiling, quotation, user confirmation, execution, and status checks for the fixed product/priorities workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores an ARI API key locally and uses it for authenticated requests.

Mitigation: Use only the documented setup or configure flow, protect the local key, and avoid sharing logs or screenshots that may expose authorization details.

Risk: The skill can spend ARI credits after a user-confirmed operation.

Mitigation: Run profile and quote first, then proceed only after explicit user confirmation with the quoted requestId.

Risk: Custom workflow or focus values could broaden behavior beyond the fixed-purpose release.

Mitigation: Use only the documented product/priorities workflow and ops_product output path.

Risk: Setup error logs may contain a temporary authorization polling token.

Mitigation: Do not share setup failure logs publicly; redact temporary authorization tokens before support review.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/funewa/skills/feature-priority)
- [Amazon product feature priority workflow](references/operation-workflow.md)
- [Amazon product feature priority API reference](references/reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and evidence-based product priority findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and explicit user confirmation before credit-spending operations.]

## Skill Version(s):

1.4.11 (source: server release metadata, artifact _meta.json, CHANGELOG, and script VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
