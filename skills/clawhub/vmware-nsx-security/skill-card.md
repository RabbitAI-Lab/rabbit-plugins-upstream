## Description:

Helps agents inspect and manage VMware NSX distributed firewall policies, security groups, VM tags, traceflow diagnostics, and IDS/IPS status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure and security engineers use this skill to review NSX firewall coverage, diagnose traffic paths, and manage distributed firewall policies, groups, and tags with approval for changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Firewall changes can unintentionally block access or weaken segmentation.

Mitigation: Use least-privilege NSX credentials, review proposed changes and delete previews, and require normal change-control approval for production writes.

Risk: Stored production credentials or an unreviewed external package may expose a sensitive NSX environment.

Mitigation: Inject production secrets through a secret manager or keychain instead of persistent .env passwords when possible, and review the external package before deployment.

## Reference(s):

- [Project homepage (release metadata)](https://github.com/vmware-skills/VMware-NSX-Security)
- [Setup guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Analysis]

**Output Format:** [Text or Markdown, with commands and structured tool results where applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include NSX policy details, firewall rule statistics, and traceflow findings.]

## Skill Version(s):

1.15.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
