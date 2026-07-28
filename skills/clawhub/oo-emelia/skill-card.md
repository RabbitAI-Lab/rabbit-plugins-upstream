## Description: <br>
Emelia helps agents read Emelia campaign, contact, provider, and webhook information through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect Emelia email campaign data, campaign activity, campaign contacts, configured email providers, and user webhooks from an authenticated Emelia account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read campaign, contact, provider, and webhook information from the user's connected Emelia account when invoked. <br>
Mitigation: Install and invoke it only when Emelia account data access is intended; ask the agent not to query Emelia for casual or ambiguous mentions. <br>
Risk: Expired credentials, missing scopes, or billing stops can prevent connector actions from completing. <br>
Mitigation: Follow the skill's recovery guidance only after a command fails with the matching authentication, connection, scope, credential, or billing error. <br>


## Reference(s): <br>
- [Emelia homepage](https://emelia.io/) <br>
- [oo CLI repository](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, JSON] <br>
**Output Format:** [Markdown guidance with bash command examples and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Emelia account data; action schemas should be checked before constructing request payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: artifact metadata and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
