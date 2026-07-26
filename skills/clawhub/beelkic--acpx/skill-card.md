## Description: <br>
Use acpx as a headless ACP CLI for agent-to-agent communication, including prompt/exec/sessions workflows, session scoping, queueing, permissions, and output formats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[Beelkic](https://clawhub.ai/user/Beelkic) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use Acpx to run coding agents through a headless ACP CLI, manage persistent or one-shot sessions, queue prompts, and consume structured output in automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Permissive approval modes may allow unintended agent actions in sensitive repositories. <br>
Mitigation: Use trusted ACP adapters, prefer --approve-reads or --deny-all for routine work, and reserve --approve-all for trusted contexts. <br>
Risk: Project configuration can expose credentials if sensitive auth values are stored carelessly. <br>
Mitigation: Protect project config files from source control and other users, and avoid storing credentials there unless that exposure is acceptable. <br>


## Reference(s): <br>
- [Acpx ClawHub release](https://clawhub.ai/Beelkic/acpx) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides text, JSON, and quiet output modes for acpx-driven automation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
