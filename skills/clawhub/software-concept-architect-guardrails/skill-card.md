## Description:

Creates, backfills, compares, and maps colocated software concept specifications when explicitly invoked.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to audit, create, backfill, and compare concept, synchronization, and pipeline specifications against code, or build derived architecture maps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional hooks can run automatically during editing and add repository specification text to agent context.

Mitigation: Inspect the hook scripts before enabling them, and install them only in trusted repositories.

Risk: Adversarial instructions in repository-controlled CONCEPT.md, PIPELINE.md, or SYNCS.md could influence an agent through the optional hooks.

Mitigation: Avoid enabling the hooks where untrusted contributors can edit these specification files.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/agenticweb4/skills/software-concept-architect-guardrails)
- [Project homepage (skill metadata)](https://github.com/ontology-of-everything/concept-skills)
- [Upstream wyx project](https://github.com/jlifyio/wyx)
- [Specification format](artifact/references/spec-format.md)
- [Optional hooks runtime](artifact/references/hooks-runtime.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown reports, specifications, and architecture maps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Audit and drift are read-only; writing specifications or maps requires authorization.]

## Skill Version(s):

1.1.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
