## Description:

Add, remove, or rename OpenClaw model IDs by reconciling provider catalogs, policy, fallbacks, and per-agent references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nextaltair](https://clawhub.ai/user/nextaltair)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to update OpenClaw model catalogs while preserving policy, fallback, and per-agent references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A model catalog update can change which models OpenClaw agents use.

Mitigation: Review proposed model replacements before applying the configuration patch.

Risk: Removing a model ID before replacing every primary or fallback reference can leave stale or broken configuration.

Mitigation: Audit registry, policy, defaults, and per-agent primary and fallback references, then validate parsing, schema checks, effective model availability, and reload logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nextaltair/skills/model-catalog-migration)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with proposed diffs, validation steps, and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce an exact proposed configuration diff when no authorized config writer is available.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
