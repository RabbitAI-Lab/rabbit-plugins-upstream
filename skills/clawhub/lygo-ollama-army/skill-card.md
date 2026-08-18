## Description:

LYGO Ollama Army runs allowlisted local Ollama helper roles as in-process daemons that read JSON queue tasks and write local results without public network, subprocess shell, planting, social outbound, or desktop installer behavior.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deepseekoracle](https://clawhub.ai/user/deepseekoracle)

### License/Terms of Use:

LYGO Sovereign License v2.0

## Use Case:

Developers and operators use this skill to run local Ollama-backed helper roles for drafting, classification, memory triage, heartbeat checks, and champion chat through allowlisted queue tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Any local process with write access to the skill queue directories can submit allowlisted prompts to the local Ollama service.

Mitigation: Keep skill directory permissions appropriate for the machine and review queued task files before running long-lived daemons.

Risk: Queued prompts are sent to the local Ollama service for processing.

Mitigation: Avoid queueing sensitive text unless the local Ollama deployment and host environment are approved for that data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/deepseekoracle/skills/lygo-ollama-army)
- [Project Homepage](https://github.com/DeepSeekOracle/lygo-protocol-stack/tree/main/docs/skills/lygo-ollama-army)
- [Security Reference](references/SECURITY.md)
- [SkillSpector Audit Reference](references/SKILLSPECTOR_AUDIT.md)
- [Agent Contract](references/AGENT_CONTRACT.md)
- [Quickstart](examples/quickstart.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, Python entry points, JSON queue tasks, and JSON result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on the selected local Ollama model and allowlisted role.]

## Skill Version(s):

0.9.0 (source: frontmatter, claw.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
