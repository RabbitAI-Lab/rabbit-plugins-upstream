## Description: <br>
AI Guardian helps agents observe and govern on-endpoint local LLM runtimes by inventorying models, checking policy and provenance, scanning prompts for sensitive content, routing guarded requests, and reporting anomalies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect local LLM endpoints, detect unsanctioned or drifted models, scan prompts for secrets or PII, and route approved requests through a local guard. It is intended for single-endpoint local LLM governance rather than multi-node inference clusters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent write-level control over local LLM models, including model pull, unload, removal, policy writes, digest pinning, and guarded generation. <br>
Mitigation: Install it only where the agent is meant to administer local LLMs; for observe-only use, expose only scan and read tools or run against an account or runtime that cannot modify the model store. <br>
Risk: Local state, audit logs, usage logs, and optional secrets can contain sensitive operational information. <br>
Mitigation: Protect the ~/.ai-guardian state directory, treat audit and usage logs as sensitive, and safeguard any master password used for the encrypted secret store. <br>
Risk: Package-name confusion could result in installing a different package than intended. <br>
Mitigation: Verify the intended package name and publisher before installation. <br>


## Reference(s): <br>
- [AI Guardian homepage](https://github.com/AIops-tools/AI-Guardian) <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/ai-guardian) <br>
- [capabilities.md](references/capabilities.md) <br>
- [cli-reference.md](references/cli-reference.md) <br>
- [setup-guide.md](references/setup-guide.md) <br>
- [agent-guardrails.md](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and structured tool guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include model inventory findings, prompt risk bands, policy status, provenance drift status, and operational next steps.] <br>

## Skill Version(s): <br>
0.8.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
