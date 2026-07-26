## Description: <br>
A single-device multi-agent task-chain methodology based on MGC that provides prompt templates for Master, Script, and Executor agents to coordinate work around sensitive resources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zkeviny](https://clawhub.ai/user/zkeviny) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to configure a local multi-agent collaboration flow where a Master Agent decomposes work, a Script Agent prepares reusable scripts, and an Executor Agent runs authorized MGC tasks without receiving plaintext credentials or script source. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents can operate scripts that retrieve local secrets or perform credential-backed actions. <br>
Mitigation: Require explicit user approval before any credential-backed, publishing, messaging, file-writing, or persistent-memory update, and restrict MGC tool access to trusted agents. <br>
Risk: The workflow relies on prompt constraints for role separation rather than enforced identity or permission controls. <br>
Mitigation: Use enforced tool scopes, separate agent runtimes, logging, and review gates for sensitive accounts or high-impact operations. <br>
Risk: Reusable scripts and collaboration best-practice updates may persist sensitive behavior or unsafe assumptions across tasks. <br>
Mitigation: Review stored scripts and best-practice updates before reuse, clean up obsolete artifacts, and avoid deploying this skill with highly sensitive accounts unless additional controls are in place. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zkeviny/skills/mgc-task-chain-meta-skill-en) <br>
- [MGC Core Repository](https://github.com/zkeviny/MGC-Blackbox) <br>
- [Artifact README](artifact/README.md) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [Master Agent prompt](artifact/prompts/master_agent.md) <br>
- [Script Agent prompt](artifact/prompts/script_agent.md) <br>
- [Executor Agent prompt](artifact/prompts/executor_agent.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown prompt templates with inline JSON, Python, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces role-specific agent prompts, MGC tool usage guidance, task reports, script storage records, and collaboration best-practice updates.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and artifact manifest) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
