## Description:

Design and compose runtime-neutral multi-agent graphs for correctness, coverage, or creativity using isolated proposals, arbitration, adversarial verification, committees, recursive review, cross-modal checks, and saturation loops.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antreasantoniou](https://clawhub.ai/user/antreasantoniou)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use Agent Orchestra to design collaboration graphs for multi-agent work, including independent proposals, arbitration, adversarial review, cross-modal checking, recursive review, and bounded improvement loops.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide high-authority orchestration of agents that read repositories and produce patches.

Mitigation: Supervise use, prefer review mode unless edits are authorized, and treat all generated outputs as untrusted until reviewed.

Risk: Example or generated workflows may perform unsafe processing of user-controlled artifacts or destructive workspace operations.

Mitigation: Run examples only in disposable sandboxes with no sensitive credentials, avoid URL inputs unless needed, and replace destructive workspace templates with validated temporary-directory workflows before code changes.

## Reference(s):

- [README.md](README.md)
- [PLAYBOOK.md](PLAYBOOK.md)
- [Saturating review workflow example](examples/saturating-review-engine.workflow.js)
- [Token-efficient orchestra variant](variants/token-efficient/SKILL.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with JavaScript workflow examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provider-neutral graph patterns; the example workflow depends on a compatible host that supplies agents, tools, models, and isolation.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
