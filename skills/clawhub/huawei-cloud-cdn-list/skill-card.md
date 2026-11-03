## Description:

Lists and filters a Huawei Cloud tenant’s CDN accelerated domains, returning a table, JSON, or compact domain-name list.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations engineers use this skill to inventory a tenant’s accelerated domains and inspect their status, CNAME, business type, and other returned fields. Its read-only query supports routine checks and follow-on CDN workflows that need domain details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dependency helper installs SDK packages from package indexes and uses --trusted-host for mirror installs.

Mitigation: Before running it, remove --trusted-host and install reviewed, pinned dependencies in an isolated environment.

Risk: Environment overrides can change the CLI executable or add arguments to its invocation.

Mitigation: Leave CDN_LIST_HCLOUD_BIN and CDN_LIST_HCLOUD_ARGS unset unless you deliberately trust their values.

Risk: Cloud credentials used for inventory queries could grant broader access than needed or be exposed in chat.

Mitigation: Use a dedicated read-only Huawei identity and keep credentials out of chat.

## Reference(s):

- [IAM Policies](references/iam-policies.md)
- [KooCLI Installation and Credential Guide](references/cli-installation-guide.md)
- [Verification Method and API Details](references/verification-method.md)
- [Huawei Cloud KooCLI Official Download Guidance](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Tabular text, a compact domain-name list, or a JSON array]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports region and domain filters, with automatic pagination.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
