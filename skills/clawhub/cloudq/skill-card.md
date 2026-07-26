## Description: <br>
CloudQ helps agents answer multi-cloud operations questions, manage Tencent Cloud Smart Advisor workflows, inspect architecture health, and provide AIOps, ChatOps, CloudOps, cost, inventory, and compliance guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[1ncludesteven](https://clawhub.ai/user/1ncludesteven) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud operators, and site reliability teams use CloudQ to route cloud and multi-cloud operations requests to Tencent Cloud Smart Advisor, retrieve architecture assessments, run advisor setup checks, and return operational guidance or console links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use Tencent Cloud credentials and participate in CloudQ advisor setup. <br>
Mitigation: Use a least-privilege Tencent Cloud subaccount and review the requested CAM policies before approving setup. <br>
Risk: Normal checks or chat handling can make privileged Tencent Cloud changes. <br>
Mitigation: Require explicit user approval before enabling advisor authorization, creating roles, attaching policies, or deleting cloud roles. <br>
Risk: Generated passwordless Tencent Cloud console links can grant console access for their validity window. <br>
Mitigation: Do not share generated console links, and treat them as sensitive access material. <br>
Risk: Cleanup with cloud deletion can remove the CloudQ CAM role. <br>
Mitigation: Run cloud cleanup only when the user intends to delete the CloudQ role. <br>


## Reference(s): <br>
- [CloudQ ClawHub release page](https://clawhub.ai/1ncludesteven/skills/cloudq) <br>
- [1ncludesteven publisher profile](https://clawhub.ai/user/1ncludesteven) <br>
- [CloudQChatCompletions API reference](references/api/CloudQChatCompletions.md) <br>
- [Tencent Cloud Smart Advisor console](https://console.cloud.tencent.com/advisor) <br>
- [Tencent Cloud API key management](https://console.cloud.tencent.com/cam/capi) <br>
- [Tencent Cloud CloudQ overview article](https://cloud.tencent.com/developer/article/2645159) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-backed command results with inline shell commands and links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [CloudQ may return asynchronous task status, operational guidance, and Tencent Cloud console links.] <br>

## Skill Version(s): <br>
1.8.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
