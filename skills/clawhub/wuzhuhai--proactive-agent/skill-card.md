## Description: <br>
Transform AI agents from task-followers into proactive partners that anticipate needs and continuously improve with persistent memory, proactive check-ins, security hardening, self-healing patterns, and verification habits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wuzhuhai](https://clawhub.ai/user/wuzhuhai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to configure an AI agent that maintains durable workspace memory, asks useful follow-up questions, performs proactive checks, and applies security and verification routines before reporting work complete. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Durable memory files can retain secrets, sensitive personal details, or stale profile information. <br>
Mitigation: Set retention limits before use, avoid storing secrets or sensitive personal details, and regularly review, prune, or delete retained memory files. <br>
Risk: Proactive checks, autonomous work, and spawned agents can exceed the user's intended scope. <br>
Mitigation: Require approval for calendar, web, account, spawned-agent, public, external, or irreversible actions, and keep spawned agents tracked until completion. <br>
Risk: External content can contain prompt-injection instructions that conflict with the user's goals. <br>
Mitigation: Treat fetched content as data rather than instructions, scan for injection patterns, and require human approval before acting on suspicious content. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/wuzhuhai/skills/proactive-agent) <br>
- [Security Patterns Reference](references/security-patterns.md) <br>
- [Onboarding Flow Reference](references/onboarding-flow.md) <br>
- [Hal 9001 Author Profile](https://x.com/halthelobster) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline code blocks, workspace file templates, checklists, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces operating guidance for an agent; generated actions should be reviewed before external, irreversible, or sensitive use.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
