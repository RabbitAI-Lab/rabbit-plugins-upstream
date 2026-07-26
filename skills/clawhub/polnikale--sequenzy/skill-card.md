## Description: <br>
Sequenzy guides agents through supported Sequenzy CLI and MCP workflows for account, subscriber, list, campaign, sequence, template, webhook, product, and transactional email operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[polnikale](https://clawhub.ai/user/polnikale) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to choose supported Sequenzy workflows, inspect state before mutations, and issue CLI or MCP-oriented guidance for email marketing, subscriber, list, campaign, sequence, template, webhook, product, and account tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill covers production Sequenzy workflows, including permanent campaign cancellation, deletion, API key creation, teammate invitations, subscriber and list changes, and webhook changes. <br>
Mitigation: Require the agent to inspect the exact resource and get explicit confirmation before canceling campaigns, deleting resources, changing subscribers or lists, inviting teammates, creating API keys, or changing webhooks. <br>
Risk: The security summary flags the guide as suspicious because it can steer an agent toward permanent campaign cancellation before clarifying intent. <br>
Mitigation: Clarify the intended operation and target campaign before cancellation, and prefer inspection or review links before any mutation. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/polnikale/skills/sequenzy) <br>
- [Command Reference](references/command-reference.md) <br>
- [Use Cases](references/use-cases.md) <br>
- [Sequenzy](https://sequenzy.com) <br>
- [Sequenzy API](https://api.sequenzy.com) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include dashboard URLs and explicit caveats for unsupported or destructive workflows.] <br>

## Skill Version(s): <br>
1.5.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
