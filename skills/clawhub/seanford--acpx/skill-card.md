## Description: <br>
Use acpx as a headless ACP CLI for agent-to-agent communication, including prompt/exec/sessions workflows, session scoping, queueing, permissions, and output formats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seanford](https://clawhub.ai/user/seanford) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation engineers use this skill to run coding agents through acpx, manage persistent or one-shot ACP sessions, queue prompts, and consume structured agent output from scripts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Unattended approval can allow an agent to proceed without interactive permission review. <br>
Mitigation: Use default or safer approval modes by default, and reserve approve-all behavior for isolated, tightly controlled automation. <br>
Risk: Persistent local session and credential storage may expose sensitive context or credentials if the host account is not protected. <br>
Mitigation: Review what is stored under ~/.acpx, protect configured credentials, and avoid sharing or checking in local acpx state. <br>
Risk: Raw agent commands can run an unexpected or untrusted ACP adapter. <br>
Mitigation: Use built-in agent names or trusted adapter commands, and review raw --agent command targets before use. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with bash command examples and optional text, quiet, or NDJSON CLI output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Behavior depends on the selected agent command, cwd/session scope, permission mode, timeout, queue settings, and output format.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
