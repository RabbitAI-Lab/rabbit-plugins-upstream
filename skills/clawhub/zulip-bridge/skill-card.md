## Description: <br>
High-performance Zulip bridge skill that enables messaging, stream monitoring, and administrative actions on Zulip servers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[niyazmft](https://clawhub.ai/user/niyazmft) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and teams use this skill to let an OpenClaw agent interact with Zulip streams, topics, direct messages, reactions, and presence through a configured Zulip plugin. It is also useful for stream monitoring and guarded administrative workflows when those actions are explicitly enabled. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can direct an agent to send messages or monitor Zulip activity through the configured plugin. <br>
Mitigation: Install it only for agents intended to connect to Zulip, and grant only the Zulip credentials and plugin authority required for the intended workspace. <br>
Risk: Administrative actions can affect users or streams if enabled. <br>
Mitigation: Keep admin actions disabled unless they are required, and review administrative requests before execution. <br>
Risk: The skill is deprecated and no longer actively updated. <br>
Mitigation: Prefer the replacement @niyazmft/openclaw-zulip plugin when active maintenance is required. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/niyazmft/skills/zulip-bridge) <br>
- [Publisher Profile](https://clawhub.ai/user/niyazmft) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a configured Zulip plugin; responses may include messaging targets, setup steps, and operational constraints.] <br>

## Skill Version(s): <br>
2026.7.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
