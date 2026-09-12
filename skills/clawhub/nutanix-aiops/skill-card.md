## Description:

Nutanix AIops helps agents inspect and operate Nutanix Prism Central v4 estates through governed MCP and CLI workflows for clusters, VMs, storage, networking, data protection, alerts, LCM, capacity, and RCA.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, infrastructure operators, and site reliability teams use this skill to query Nutanix estate health, triage alerts, manage VM lifecycle tasks, inspect storage and networking, run DR and LCM workflows, and generate capacity or RCA guidance through Prism Central v4.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform destructive Prism Central operations and does not decide whether a write is authorized.

Mitigation: Start with a least-privilege read-only Prism Central account, require dry-run review and human approval before destructive actions, and rely on Prism Central RBAC for write authority.

Risk: The release installs an unpinned executable package.

Mitigation: Pin and verify the nutanix-aiops package version and source before deployment.

Risk: Secrets include a master password environment variable and a deprecated plaintext password fallback.

Mitigation: Protect NUTANIX_AIOPS_MASTER_PASSWORD, avoid exposing legacy password environment variables, and migrate legacy values into the encrypted secret store.

Risk: Some operational paths are documented as needing live verification beyond mocked Prism Central v4 responses.

Mitigation: Run nutanix-aiops doctor and validate high-risk workflows against non-production or throwaway resources before production use.

## Reference(s):

- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)
- [Project homepage](https://github.com/AIops-tools/Nutanix-AIops)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API Calls, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and structured operational results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run previews, audit and undo guidance, Prism Central task identifiers, RCA findings, and operational risk labels.]

## Skill Version(s):

0.11.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
