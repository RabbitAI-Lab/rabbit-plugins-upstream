## Description: <br>
AI Guardian helps agents observe and govern single-endpoint local LLM runtimes by inventorying models, scanning prompts, policy-gating generation, recording usage, and surfacing anomalies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, security reviewers, and operations teams use this skill to inspect local LLM endpoints, detect unsanctioned or drifted models, scan prompts for sensitive content, and route approved prompts through a governance guard. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review reports that installer metadata points to a different package than the documented install command. <br>
Mitigation: Resolve the package-name mismatch before installation or publication, and verify the package source before running the skill. <br>
Risk: The security review reports high-impact write actions without built-in authorization gates. <br>
Mitigation: Expose only scan and observe tools for routine use, and run against a runtime or account that cannot administer model storage unless writes are intended. <br>
Risk: The security guidance treats local audit and usage databases as sensitive operational records. <br>
Mitigation: Restrict access to the local state directory and avoid persistent master-password exports for encrypted token storage. <br>


## Reference(s): <br>
- [AI Guardian ClawHub page](https://clawhub.ai/zw008/skills/ai-guardian) <br>
- [AI Guardian homepage](https://github.com/AIops-tools/AI-Guardian) <br>
- [Capabilities reference](references/capabilities.md) <br>
- [CLI reference](references/cli-reference.md) <br>
- [Setup and security guide](references/setup-guide.md) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands and MCP tool-call recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference local configuration, audit, usage, and undo records; artifact evidence says raw prompts are not stored.] <br>

## Skill Version(s): <br>
0.6.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
