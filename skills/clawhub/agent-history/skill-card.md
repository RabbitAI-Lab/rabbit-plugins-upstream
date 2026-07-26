## Description: <br>
Agent History helps agents search and read prior local AI coding-agent conversations with the `ochist` CLI so they can recover past research, commands, errors, and decisions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[adlternative](https://clawhub.ai/user/adlternative) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use this skill to find earlier local agent conversations before repeating research, commands, debugging work, or codebase exploration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search results can expose sensitive prior coding-agent conversations, including secrets, credentials, private code, or unrelated user data. <br>
Mitigation: Start with project-scoped searches, use global searches only when necessary, and review results before sharing or reusing them. <br>


## Reference(s): <br>
- [Server-resolved GitHub source](https://github.com/adlternative/agent-historian/tree/main/skills/agent-history) <br>
- [ClawHub skill page](https://clawhub.ai/adlternative/skills/agent-history) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, text] <br>
**Output Format:** [Markdown guidance with inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only local history lookup; recommends project-scoped searches, paging, and selective part reads to limit unnecessary exposure of prior chat content.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
