## Description: <br>
OpenClaw prompt-layer Freedom Preserving Protocol for voluntary constitutional agent self-governance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ovrsr](https://clawhub.ai/user/ovrsr) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and OpenClaw operators use this skill when they want an agent to review, voluntarily adopt, verify, audit, and revoke a prompt-layer constitutional governance framework with explicit user consent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is prompt-layer governance and cannot mechanically veto tool calls by itself. <br>
Mitigation: Treat it as a reasoning and adoption framework; use the separate dispatcher enforcement plugin only when runtime-level tool gating is required. <br>
Risk: Adoption appends persistent local agent state and audit records. <br>
Mitigation: Install only after explicit user consent, review package.json first, run installs from the lockfile when possible, and use the bundled revoke flow to stop adoption while preserving an auditable history. <br>
Risk: Server-resolved import provenance is unavailable for this release. <br>
Mitigation: Do not infer provenance from artifact text; verify the bundled constitution hash and Ed25519 signature before adopting. <br>
Risk: Optional enforcement and trust plugins are separate packages with their own risk surfaces. <br>
Mitigation: Review and install those plugins separately only when their added enforcement or trust behavior is needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ovrsr/skills/freedom-preserving-protocol) <br>
- [README](README.md) <br>
- [Revocation guide](docs/REVOCATION.md) <br>
- [Constitution JSON](constitution.json) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented verification output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local SOUL, MEMORY, adoption-state, audit, and revocation files only after explicit user-directed adoption or revocation.] <br>

## Skill Version(s): <br>
1.3.9 (source: frontmatter, package.json, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
