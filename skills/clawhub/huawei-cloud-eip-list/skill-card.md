## Description:

Lists Huawei Cloud Elastic IP instances by region and filters, returning a table, JSON array, or compact name and IP list through KooCLI or its SDK fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud administrators and developers use the skill to inspect tenant EIP inventory by region, filter results by ID, status, or public IP, and obtain structured results for reviews or follow-on tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unchecked settings can replace the intended command or redirect authenticated requests.

Mitigation: Remove or lock down command overrides, restrict regions to approved Huawei endpoints, and use a dedicated list-only cloud identity with credentials configured outside chat.

Risk: The remote KooCLI installer and live SDK/API behavior have not been verified.

Mitigation: Obtain KooCLI through Huawei's verified installation instructions and review live behavior before credentialed use.

## Reference(s):

- [KooCLI Installation & Credential Guide](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Least-Privilege IAM Policy](references/iam-policies.md)
- [API and Parameter Verification](references/verification-method.md)
- [Credential Setup and SDK Fallback](references/cli-installation-guide.md)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Full-field table, raw JSON array, or compact EIP name and public-IP list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports region and server-side filters; results are paged automatically.]

## Skill Version(s):

1.0.4 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
