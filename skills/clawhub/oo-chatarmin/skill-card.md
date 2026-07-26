## Description: <br>
Chatarmin lets an agent read, create, update, and delete Chatarmin data through an OOMOL-connected account using the oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate a connected Chatarmin account from an agent workflow, including contacts, campaigns, flows, voucher pools, webhooks, analytics, and WhatsApp messaging. It is suited to account-management tasks where the user can review proposed payloads before state-changing actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can operate a connected Chatarmin account and trigger sensitive account-management actions. <br>
Mitigation: Install it only when the user intends to let an agent use the connected account, and review proposed payloads before approving writes, message sends, webhook changes, voucher changes, or deletions. <br>
Risk: Destructive actions can remove contacts, voucher pools, webhooks, or voucher codes. <br>
Mitigation: Require explicit approval for the exact target and effect before running destructive actions. <br>


## Reference(s): <br>
- [Chatarmin homepage](https://chatarmin.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-chatarmin) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload or response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
