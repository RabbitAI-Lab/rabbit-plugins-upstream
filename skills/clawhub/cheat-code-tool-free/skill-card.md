## Description: <br>
Cheat Code Tool Free helps an AI agent perform external knowledge lookups for current technical documentation, API specifications, and domain knowledge beyond its training data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent retrieve structured external knowledge when its built-in training data may be stale or incomplete. Typical use cases include checking current technical documentation, API specifications, standards, and domain facts before composing an answer. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The documented authority and triggers are broader than a user may expect for a read-only external lookup helper. <br>
Mitigation: Use the skill only for explicit user-directed lookup requests and review proposed actions before execution. <br>
Risk: External lookup requests may send user-provided content to a knowledge service. <br>
Mitigation: Use a least-privilege token and avoid sending sensitive, regulated, or confidential content. <br>
Risk: The artifact mentions create/export operations and callback URLs without clear behavior guarantees. <br>
Mitigation: Treat create/export and callback behavior as undefined unless the publisher provides clearer documentation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/cheat-code-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Artifact skill definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a knowledge-service token and network access; free edition documentation describes single-query usage and daily query limits.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
