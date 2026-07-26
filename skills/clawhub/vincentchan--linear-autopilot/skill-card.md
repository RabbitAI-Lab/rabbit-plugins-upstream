## Description: <br>
Automate Linear task processing with Discord notifications and git sync. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vincentchan](https://clawhub.ai/user/vincentchan) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to connect Linear tasks to Discord-driven Clawdbot workflows, including task intake, status updates, notifications, and optional git sync. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: External Linear events can drive agent work, Linear status updates, Discord messages, and git pushes. <br>
Mitigation: Require human review before running tasks or pushing git commits, use workflow filters for ready-to-process tasks, and keep the automation in a private low-risk Discord channel. <br>
Risk: Linear API keys, Discord bot tokens, and webhook URLs are sensitive credentials used by the setup. <br>
Mitigation: Use dedicated low-privilege credentials, treat all webhook URLs and bot tokens as secrets, store them only in local or service secret stores, and rotate them if exposed. <br>
Risk: A misconfigured automation platform can continue sending unwanted task events. <br>
Mitigation: Document and test how to quickly disable the Make.com, Pipedream, or Zapier workflow before relying on the integration. <br>


## Reference(s): <br>
- [Linear Autopilot on ClawHub](https://clawhub.ai/vincentchan/skills/linear-autopilot) <br>
- [Make.com Setup Guide](references/make-setup.md) <br>
- [Pipedream Setup Guide](references/pipedream-setup.md) <br>
- [Zapier Setup Guide](references/zapier-setup.md) <br>
- [Linear GraphQL API Endpoint](https://api.linear.app/graphql) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration, code] <br>
**Output Format:** [Markdown guidance with shell commands, JSON configuration snippets, and a Bash helper script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces setup instructions for Linear, Discord, Make.com, Pipedream, Zapier, and optional git sync workflows.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
