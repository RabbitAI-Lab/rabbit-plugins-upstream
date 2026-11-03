## Description:

Estimate Huawei Cloud pre-order costs, support allowlisted resource provisioning through hcloud, and guide unsubscribe requests through the console.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud users and developers use this skill to estimate Huawei Cloud purchase costs and compare configurations. It also prepares supported resource purchases and explains console-based unsubscribe steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Resource purchases can create ongoing charges.

Mitigation: Review the configuration, itemized costs, and payment choices, then approve the specific purchase before execution; stop created resources through the console when they are no longer needed.

Risk: Broad permissions can allow unintended cloud changes.

Mitigation: Use read-only permissions for estimates and grant only the create permissions required for the intended purchases.

Risk: Cloud credentials could be exposed during setup or use.

Mitigation: Keep credentials local and do not include them in shared output.

Risk: A quote can omit lines whose pricing could not be verified.

Mitigation: Show unresolved items beside the subtotal and do not describe the subtotal as complete while pricing gaps remain.

## Reference(s):

- [Huawei Cloud KooCLI installation guide](https://support.huaweicloud.com/qs-hcli/hcli_02_003.md)
- [Huawei Cloud pricing command reference](artifact/references/pricing/commands.md)
- [Provisioning operation allowlist](artifact/references/lifecycle/commands.md)
- [Unsubscribe rules](https://support.huaweicloud.com/usermanual-billing/unsubscription_topic_2000010.md)
- [ClawHub skill page](https://clawhub.ai/agenticweb4/skills/huawei-cloud-cost-estimation)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Shell commands, Configuration instructions]

**Output Format:** [Markdown with itemized estimates, evidence, guidance, and relevant hcloud commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Quotes identify assumptions, verified lines, and unresolved pricing items.]

## Skill Version(s):

3.3.0 (source: SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
