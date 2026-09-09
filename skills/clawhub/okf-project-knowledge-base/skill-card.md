## Description:

Durable project knowledge as Git-native OKF bundles (docs/knowledge/, one concept per file, with provenance and trust tiers).

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to help agents preserve durable project knowledge in repository-local OKF bundles, including decisions, findings, rules, provenance, and index/log bookkeeping. It is intended for information that should survive context resets, not transient session state or standing agent instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents may preserve sensitive or host-local information in durable project knowledge files.

Mitigation: Review generated knowledge files, index/log updates, and instruction-file pointers before committing; apply the skill's publicity fence so secrets, personal data, absolute paths, machine names, and internal hostnames are excluded.

Risk: Incorrect, stale, or unsupported project knowledge could persist and influence future agents.

Mitigation: Require sources for claims, use status and stale_after fields when knowledge may decay, and deprecate or replace concepts instead of deleting their history.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/okf-project-knowledge-base)
- [Project homepage](https://github.com/tenequm/skills/tree/main/skills/okf-project-knowledge-base)
- [Open Knowledge Format](https://github.com/GoogleCloudPlatform/open-knowledge-format)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown knowledge files with YAML frontmatter, repository index/log updates, concise guidance, and occasional shell commands or configuration edits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are repository-local documentation changes with explicit sources, generated actor metadata, status, and optional staleness markers.]

## Skill Version(s):

0.1.3 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
