## Description: <br>
Create, manage, and deploy ElevenLabs conversational AI agents. Use when the user wants to work with voice agents, list their agents, create new ones, or manage agent configurations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sindrenilsen](https://clawhub.ai/user/sindrenilsen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to work with ElevenLabs conversational AI agents from an agent-assisted workflow, including listing, creating, syncing, configuring, and deploying agents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can authenticate to an ElevenLabs account and deploy remote agent changes. <br>
Mitigation: Use it only with the intended ElevenLabs account and confirm what will be pushed before approving deployment or tool changes. <br>
Risk: The skill can create or modify local project and configuration files. <br>
Mitigation: Run it in a workspace where those files are expected, and review generated agent and tool configuration before relying on it. <br>
Risk: Some workflows instruct the agent to hide setup details or command errors from the user. <br>
Mitigation: Keep low-level CLI output out of the interface, but disclose material account, workspace, local-versus-remote, and deployment status before taking consequential action. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/sindrenilsen/skills/elevenlabs-agents) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown responses with tables and code snippets, plus local configuration files and ElevenLabs CLI operations when needed.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the elevenlabs CLI and an authenticated ElevenLabs account; the agent should distinguish local and remote agent state.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
