## Description: <br>
Captures learnings, errors, and corrections to enable continuous improvement. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[space-cadet](https://clawhub.ai/user/space-cadet) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use this skill to keep local project memory about failed commands, user corrections, missing capabilities, and recurring workflow improvements. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local learning logs could capture sensitive details, credentials, private conversation content, or environment values if the agent records too much context. <br>
Mitigation: Do not log secrets, tokens, private keys, or environment variables; periodically review `.learnings/` and promoted memory files. <br>
Risk: Incorrect or stale entries could be promoted into project memory and influence future agent behavior. <br>
Mitigation: Review pending learning, error, and feature-request entries at natural breakpoints before promoting them to project memory. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/space-cadet/skills/self-improving-agent) <br>
- [ClawHub Publisher Profile](https://clawhub.ai/user/space-cadet) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Guidance, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and markdown templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates or updates local .learnings markdown files without overwriting existing files.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
