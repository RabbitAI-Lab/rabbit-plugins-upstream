## Description:

Helps operators inspect and manage AVI load balancing and AKO Kubernetes ingress through diagnostics, configuration guidance, and controlled actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators and engineers use this skill to inspect virtual services, pools, certificates, and service engines; troubleshoot AKO ingress and synchronization; and carry out approved AVI or AKO changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to production controllers and AKO clusters can expose sensitive infrastructure or disrupt application traffic.

Mitigation: Install only for authorized operators; use least-privilege or read-only accounts and scope access to intended environments.

Risk: Enabling or disabling services, draining pool members, restarting AKO, or changing Helm settings can alter live workloads.

Mitigation: Review the target and impact, and obtain explicit approval before confirm=true or CLI double-confirmed write actions.

Risk: Locally stored production credentials may be exposed.

Mitigation: Store production secrets in a secret manager rather than a local .env file.

## Reference(s):

- [Project homepage (skill metadata)](https://github.com/vmware-skills/VMware-AVI)
- [Setup guide](artifact/references/setup-guide.md)
- [Capabilities and compatibility](artifact/references/capabilities.md)
- [CLI reference](artifact/references/cli-reference.md)
- [Agent guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline commands and structured diagnostic results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only diagnostics and explicitly approved state changes; results depend on the connected controllers and clusters.]

## Skill Version(s):

2.4.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
