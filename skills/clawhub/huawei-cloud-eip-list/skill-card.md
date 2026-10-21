## Description:

Lists Huawei Cloud Elastic IP instances in a tenant region through KooCLI or its SDK fallback, with table, JSON, and compact name/IP output modes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators can inventory Elastic IPs in a Huawei Cloud tenant, inspect their status and bindings, and obtain IDs for follow-up workflows. The skill is intended for read-only listing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crafted region input may redirect authenticated requests.

Mitigation: Validate region values before use with cloud credentials; wait for region validation safeguards.

Risk: Command overrides may weaken the read-only safeguards.

Mitigation: Avoid unrestricted command overrides and use an IAM identity limited to EIP listing. Keep credentials out of chat.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/wlc-dev/skills/huawei-cloud-eip-list)
- [IAM policies](references/iam-policies.md)
- [KooCLI installation guide](references/cli-installation-guide.md)
- [Verification method](references/verification-method.md)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Full-field text table, JSON array, or compact EIP alias/public-IP list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports ID, status, and public-IP filters with marker-based paging; designed for read-only inventory retrieval.]

## Skill Version(s):

1.0.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
