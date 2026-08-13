## Description:

RevenueCat (revenuecat.com). Use this skill for ANY RevenueCat request -- searching and reading data. Whenever a task involves RevenueCat, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect RevenueCat projects, customers, subscriptions, entitlements, offerings, products, and revenue metrics through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: RevenueCat lookup results can expose sensitive customer, subscription, entitlement, and revenue data.

Mitigation: Invoke the skill only for intended RevenueCat lookup tasks and handle returned customer, subscription, and revenue data as sensitive business information.

Risk: First-time CLI installation, login, or RevenueCat account connection changes the local or account setup before lookups can run.

Mitigation: Review and approve first-time install, login, and account-connection steps before allowing them; routine lookup actions should use the existing connected account.

## Reference(s):

- [RevenueCat homepage](https://www.revenuecat.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions are read-only in the available action list; responses may contain sensitive customer, subscription, entitlement, and revenue data.]

## Skill Version(s):

1.0.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
