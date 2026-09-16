## Description:

Generates Huawei Cloud pre-order estimates, provisions allowlisted resources through hcloud behind dry-run and confirmation gates, and routes unsubscribe requests to console guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to estimate Huawei Cloud pre-order costs, prepare allowlisted hcloud provisioning commands, and route unsubscribe requests to console-only guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Provisioning commands may create billable Huawei Cloud resources.

Mitigation: Use least-privilege IAM, require hcloud help checks, complete --dryrun successfully, review the fee summary, and wait for explicit confirmation before execution.

Risk: Huawei Cloud AK/SK credentials can be exposed if pasted into chat or command output.

Mitigation: Use locally configured profiles or environment variables outside chat, avoid sharing secrets, and prefer least-privilege IAM users.

Risk: Manual hcloud installation can execute downloaded scripts or sudo commands.

Mitigation: Verify downloads against Huawei Cloud's official KooCLI release guidance and review installer content before running it locally.

Risk: Returned estimates may differ from final bills or omit unavailable pricing.

Mitigation: Treat current hcloud responses as authoritative for the session, present totals as not final bills, and obtain separate approval when price is unknown.

Risk: Unsubscribe or non-allowlisted write requests could affect cloud resources outside the skill boundary.

Mitigation: Do not emit or run unsubscribe operations, refuse non-allowlisted writes, and route those requests to the Huawei Cloud console or read-only billing paths.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/agenticweb4/skills/huawei-cloud-cost-estimation)
- [Publisher profile](https://clawhub.ai/user/agenticweb4)
- [Project homepage](https://github.com/concept-git/cloud-concept-skills/tree/main/skills/en/huawei-cloud-cost-estimation)
- [KooCLI installation guide](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Huawei Cloud unsubscribe rules](https://support.huaweicloud.com/usermanual-billing/unsubscription_topic_2000010.html)
- [Huawei Cloud period quotation API](https://support.huaweicloud.com/api-bpconsole/bcloud_01002.html)
- [Huawei Cloud on-demand quotation API](https://support.huaweicloud.com/api-bpconsole/bcloud_01001.html)
- [Huawei Cloud resource spec API](https://support.huaweicloud.com/api-oce/qct_00008.html)
- [references/cli-installation.md](references/cli-installation.md)
- [references/iam-policies.md](references/iam-policies.md)
- [references/lifecycle/concepts.md](references/lifecycle/concepts.md)
- [references/lifecycle/commands.md](references/lifecycle/commands.md)
- [references/pricing/commands.md](references/pricing/commands.md)
- [references/pricing/semantic/catalog.yml](references/pricing/semantic/catalog.yml)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, cost summaries, and confirmation prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires hcloud KooCLI 7.2+, matching IAM permissions, outbound network access, and user-managed Huawei Cloud credentials.]

## Skill Version(s):

3.2.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
