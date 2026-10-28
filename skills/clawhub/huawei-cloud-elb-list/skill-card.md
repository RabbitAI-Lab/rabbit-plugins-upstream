## Description:

Lists Huawei Cloud Elastic Load Balancers through KooCLI or the Huawei Cloud SDK, with filters and table, JSON, name-only, and Markdown outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud developers and operators use this skill to inspect regional ELB inventories and retrieve load balancer IDs and names for operational checks or follow-on tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dependency helper's package installation path weakens download security and could expose cloud credentials to substituted software.

Mitigation: Avoid the helper; install reviewed SDK versions in an isolated environment with certificate verification enabled before providing cloud credentials.

Risk: Installing KooCLI introduces executable software into the environment.

Mitigation: Use Huawei's official installation instructions and verify the downloaded software.

Risk: Credentials used for inventory queries can access tenant ELB information.

Mitigation: Use project-scoped list-only credentials and keep executable overrides trusted.

Risk: Table and names-only queries save an inventory document locally by default.

Mitigation: Pass --no-md when you do not want a local inventory file, or choose a controlled path with --md-out.

## Reference(s):

- [KooCLI Installation & Credential Guide](references/cli-installation-guide.md)
- [Huawei Cloud KooCLI Official Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Least-Privilege IAM Policy](references/iam-policies.md)
- [Verification Method and API Details](references/verification-method.md)
- [Data Flow Diagram](references/dataflow-diagram.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [ID and name table, names-only text, raw JSON array, or Markdown table file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The standard table contains only ID and name; JSON preserves returned fields. Table and names-only modes write a Markdown inventory unless --no-md is set; --json does not write a file.]

## Skill Version(s):

1.0.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
