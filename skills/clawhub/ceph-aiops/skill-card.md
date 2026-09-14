## Description:

Ceph AIops helps agents diagnose and operate Ceph clusters through the ceph-mgr Dashboard REST API, including health analysis, OSD, PG, pool, RBD, CephFS, RGW inspection, and governed write operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, storage operators, and SREs use this skill to triage Ceph health warnings, inspect cluster storage state, and plan operational actions. It can also invoke governed write workflows for cluster flags, OSD lifecycle, pool settings, RBD objects, scrubs, and recovery throttling when the connected Dashboard account permits them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and runs an external ceph-aiops executable that can access Ceph credentials and operate a live cluster.

Mitigation: Verify the package source and version out of band before installation, and start with a dedicated read-only ceph-mgr Dashboard account.

Risk: Write tools can make destructive or irreversible Ceph changes, including OSD purge, pool deletion, and RBD deletion when the connected account has permission.

Mitigation: Grant administrator rights only for planned write sessions, require dry-run review where available, and confirm cluster state before executing high-risk operations.

Risk: Credentials can be exposed if passwords are passed directly on command lines or reused from broad-privilege human accounts.

Mitigation: Use the encrypted secret store or non-interactive master password flow, avoid passing passwords with --value, and use a dedicated least-privilege Dashboard account.

Risk: Some write and multi-node rebalance behavior has not been verified against a live cluster in the artifact evidence.

Mitigation: Run ceph-aiops doctor and validate intended workflows in a MicroCeph or staging cluster before using them on production data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/ceph-aiops)
- [Project homepage](https://github.com/AIops-tools/Ceph-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with command snippets and structured operational recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Ceph health findings, risk-tier notes, dry-run steps, audit context, and undo guidance.]

## Skill Version(s):

0.11.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
