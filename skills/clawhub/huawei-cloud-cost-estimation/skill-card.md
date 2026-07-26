## Description: <br>
Generates Huawei Cloud pre-order price estimates, prepares confirmed allowlisted hcloud create commands with dry-run and cost checks, and gives console-only unsubscribe guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agenticweb4](https://clawhub.ai/user/agenticweb4) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud operators, and cost reviewers use this skill to estimate Huawei Cloud costs, prepare tightly controlled resource creation through hcloud, and route unsubscribe requests to the Huawei Cloud console with account and refund checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Confirmed create or order actions can change the user's Huawei Cloud account and incur charges. <br>
Mitigation: Use least-privilege IAM credentials and require runtime help lookup, cost review, successful --dryrun, and explicit user confirmation before execution. <br>
Risk: Cloud pricing or resource parameters may be inaccurate if inferred from memory or copied from stale examples. <br>
Mitigation: Use only current hcloud help and BSS pricing responses, and disclose unknown costs before asking for confirmation. <br>
Risk: Credential exposure could occur if access keys or tokens are pasted into chat. <br>
Mitigation: Refuse credentials in chat and direct users to configure hcloud locally with least-privilege IAM credentials. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/agenticweb4/skills/huawei-cloud-cost-estimation) <br>
- [Huawei Cloud KooCLI quick installation](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html) <br>
- [Huawei Cloud console](https://console.huaweicloud.com) <br>
- [Huawei Cloud unsubscribe rules](https://support.huaweicloud.com/usermanual-billing/unsubscription_topic_2000010.html) <br>
- [Pricing commands](references/pricing/commands.md) <br>
- [Lifecycle concepts](references/lifecycle/concepts.md) <br>
- [Lifecycle command allowlist](references/lifecycle/commands.md) <br>
- [Pricing IAM policies](references/pricing/iam-policies.md) <br>
- [KooCLI installation guide](references/cli-installation.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with hcloud command snippets and cost summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Create flows require runtime help lookup, successful --dryrun, cost review or explicit unknown-cost acknowledgment, and user confirmation before execution.] <br>

## Skill Version(s): <br>
3.1.0 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
