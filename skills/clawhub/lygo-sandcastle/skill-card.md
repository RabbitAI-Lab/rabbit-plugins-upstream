## Description: <br>
LYGO Sovereign Workflow Orchestrator helps agents validate and run YAML-defined local workflows with input gating, memory recall, optional consensus, run identity, and consent-gated kernel behavior. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to coordinate local-first sovereign workflows, validate untrusted YAML before execution, and keep workflow runs auditable. It is intended for controlled environments where users can review workflow definitions, upstream integrations, and consent-gated actions before enabling them. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Workflow execution can act on untrusted YAML or user-provided prompts. <br>
Mitigation: Validate YAML before running it, keep the default dry-run mode for first use, and avoid storing secrets in workflow files. <br>
Risk: Optional upstream, container, and kernel-related modes expand execution trust boundaries. <br>
Mitigation: Enable sandcastle-ai, Docker or Podman execution, and kernel planting only after explicit review and user consent. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/deepseekoracle/skills/lygo-sandcastle) <br>
- [Security Guidance](artifact/references/SECURITY.md) <br>
- [Agent Contract](artifact/references/AGENT_CONTRACT.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code] <br>
**Output Format:** [Markdown guidance with inline shell commands and command tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Emphasizes dry-run first use, explicit consent for publishing or kernel actions, and validation before running untrusted workflows.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
