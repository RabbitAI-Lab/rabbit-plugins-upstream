## Description: <br>
Agentar helps users install and use the Agentar CLI to run chat, delegate office, image, and video tasks to Agentar platform agents, configure credentials, test sessions and attachments, and troubleshoot CLI workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[openagentar](https://clawhub.ai/user/openagentar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to run Agentar CLI chat workflows, select built-in scenario agents for office, image, or video tasks, configure credentials, test sessions and attachments, and troubleshoot ordinary CLI usage. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow installs an external CLI and skill package from publisher-hosted URLs. <br>
Mitigation: Install only if you trust the CLI publisher and installer source; download and inspect the installer and verify checksums or signatures when available. <br>
Risk: Credential examples involve API keys and local token or state files. <br>
Mitigation: Avoid putting secrets in shell history, prefer environment or secret-manager handling where practical, store token files with restrictive permissions, and revoke credentials when no longer needed. <br>


## Reference(s): <br>
- [Agentar on ClawHub](https://clawhub.ai/openagentar/skills/agentar) <br>
- [Agentar CLI Quick Reference](references/agentar-cli-quick-reference.md) <br>
- [Public production install script](https://dtaiagtavtr.antdigital.com/agentar-cli/install.sh) <br>
- [Public production skill zip](https://dtaiagtavtr.antdigital.com/agentar-cli/skill.zip) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash commands and troubleshooting tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include text, JSON, JSONL, SSE, or debug output mode guidance for Agentar CLI commands.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
