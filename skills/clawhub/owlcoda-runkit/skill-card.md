## Description:

OwlCoda RunKit guides Codex through receipt-backed, project-owned execution workflows for coordinating multi-agent work, recording durable project state, and capturing verification evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yeemio](https://clawhub.ai/user/yeemio)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to coordinate large, receipt-backed agent work in a project workspace, track ownership and verification, manage handoffs, rework, and decisions, and produce ready-for-commit evidence without granting Git or deployment authority by default.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to create durable project coordination artifacts and run verification or deployment-related commands when separately authorized.

Mitigation: Review the RunKit workflow before installing, keep generated project records under the intended workspace, and grant Git, deployment, credential, destructive, or foreign-write authority only when those actions are intended.

Risk: The skill depends on an external owlrunkit CLI and the artifact notes fail-closed registry adoption for the bundled Core until exact official npm registry provenance is independently verified.

Mitigation: Keep the owlrunkit dependency pinned and local, use the disclosed Core identity and manifest when operating the skill, and verify official registry provenance before adopting a registry-sourced Core.

## Reference(s):

- [OwlCoda RunKit homepage](https://owlcoda.com/#start)
- [OwlCoda RunKit Contract v0.2](references/contract-v0.2.md)
- [OwlCoda RunKit Contract v0.1](references/contract-v0.1.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON files, markdown]

**Output Format:** [Markdown guidance with inline shell commands and JSON template references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 20 or later and a pinned local owlrunkit CLI; project coordination artifacts are durable local files.]

## Skill Version(s):

0.23.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
