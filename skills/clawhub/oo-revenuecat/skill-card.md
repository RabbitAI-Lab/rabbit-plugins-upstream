## Description:

Enables an agent to read RevenueCat customer, subscription, entitlement, offering, product, project, and revenue metric data through an OOMOL-connected RevenueCat account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect RevenueCat projects, customers, subscriptions, entitlements, offerings, products, and revenue metrics from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that can execute unverified code.

Mitigation: Prefer a verified package, or separately download, inspect, and integrity-check the installer before execution.

Risk: RevenueCat access is brokered through OOMOL-connected credentials.

Mitigation: Install only if that brokered access model is acceptable, and connect a RevenueCat API key with only the scopes needed.

Risk: Future connector actions may change or remove RevenueCat data if marked write or destructive.

Mitigation: Review the live action schema, exact payload, target, and effect before approving any write or destructive action.

## Reference(s):

- [RevenueCat homepage](https://www.revenuecat.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-revenuecat)

## Skill Output:

**Output Type(s):** [Shell commands, JSON data, Guidance]

**Output Format:** [Markdown instructions with inline shell commands; connector responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include a data payload and meta.executionId.]

## Skill Version(s):

1.0.2 (source: evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
