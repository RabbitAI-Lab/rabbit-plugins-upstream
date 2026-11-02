## Description:

Shows one Huawei Cloud ECS instance by ID using KooCLI or the Huawei Cloud SDK fallback, returning key details as text, JSON, or an optional Markdown file.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inspect a specific ECS instance for troubleshooting and to retrieve instance attributes for follow-up workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Command overrides and region handling weaken the advertised safety limits.

Mitigation: Use dedicated read-only cloud credentials and a verified KooCLI installation; remove unrestricted command overrides, restrict SDK regions to verified Huawei endpoints, and use known region identifiers in a trusted launch environment.

Risk: A Markdown export overwrites the selected file if it already exists.

Mitigation: Choose a fresh output path or preserve the existing file before exporting.

## Reference(s):

- [KooCLI installation and credential guide](references/cli-installation-guide.md)
- [Least-privilege IAM policy](references/iam-policies.md)
- [Verification method](references/verification-method.md)
- [Huawei Cloud KooCLI quick start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [Detail text, raw JSON, or a Markdown file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports one ECS instance; an explicitly selected Markdown export path is overwritten if it already exists.]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
