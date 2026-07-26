## Description: <br>
Cognitive Memory provides an agent memory system with episodic, semantic, procedural, and core stores, plus recall, decay, reflection, and audit workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[icemilo414](https://clawhub.ai/user/icemilo414) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to add a durable local memory architecture to an agent workspace, including memory setup, routing prompts, reflection flows, decay scoring, and audit tracking. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill creates long-lived local memory that can persist sensitive user or project details. <br>
Mitigation: Use a clean workspace, avoid storing secrets, and review retained memory files before enabling search or sharing the workspace. <br>
Risk: The setup and upgrade scripts can initialize or commit changes through git in the target workspace. <br>
Mitigation: Review the scripts before execution, run them only in the intended workspace, and disable or inspect auto-commit behavior if it does not fit the deployment policy. <br>
Risk: The memory and reflection instructions can shape agent behavior through identity, persona, token-reward, and self-reflection sections. <br>
Mitigation: Review and narrow trigger phrases, remove token-reward or identity/persona sections where inappropriate, and require user approval before reflection or memory writes. <br>
Risk: Multi-agent shared memory can expose vault or user-pinned content beyond the intended agent. <br>
Mitigation: Restrict vault and sub-agent access, require main-agent review for proposed memory writes, and audit changes to memory files. <br>


## Reference(s): <br>
- [Architecture](artifact/references/architecture.md) <br>
- [Reflection Process](artifact/references/reflection-process.md) <br>
- [Routing Prompt](artifact/references/routing-prompt.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/icemilo414/skills/cognitive-memory) <br>
- [Publisher Profile](https://clawhub.ai/user/icemilo414) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code] <br>
**Output Format:** [Markdown guidance with shell commands, JSON configuration, scripts, and file templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Initializes and updates local memory files, templates, and git-backed audit records when the provided scripts are run.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
