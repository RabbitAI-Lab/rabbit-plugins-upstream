## Description: <br>
Operating doctrine for X/Twitter account automation: stable Chrome sessions, role separation, human-like interaction, careful posting, reply discipline, and recovery patterns for scheduled account activity where account safety and long-term reputation matter more than raw output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alexbloch-ia](https://clawhub.ai/user/alexbloch-ia) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, agencies, and brand teams use this skill to guide agents that assist with X/Twitter posting, replies, monitoring, account maintenance, and recovery through a logged-in browser. It is intended for workflows where reputation, compliance, and controlled human-like operation are more important than high-volume automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agent-assisted posting, replies, likes, follows, and DMs can create reputational or compliance harm if actions are published without review. <br>
Mitigation: Use human review or strict approval gates for public or private account actions where reputation, regulated advice, or brand safety matters. <br>
Risk: Misconfigured browser profiles, workspace paths, or webhooks can direct activity or alerts to the wrong account or channel. <br>
Mitigation: Configure the browser profile, workspace directory, account handle, and webhook intentionally before use, then verify the logged-in session and target account before any public action. <br>
Risk: Automated interaction can become spam-like or unsafe if an agent forces scheduled output when there is no useful action to take. <br>
Mitigation: Follow the skill's guidance to draft locally, read context before acting, skip weak posting slots, cap replies, and stop when the browser or account state is unstable. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/alexbloch-ia/skills/twitter-account-operations) <br>
- [OpenClaw](https://openclaw.ai) <br>
- [Claude Code](https://claude.ai/code) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with YAML configuration examples and inline shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces operating doctrine, checklists, recovery procedures, reply skeletons, and browser-automation command examples for agent-assisted X/Twitter account work.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
