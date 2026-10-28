## Description:

Use when creating a Hindsight-docs-style local documentation skill for another tool, SDK, API, or docs repository.

This skill is ready for commercial/non-commercial use.

## Publisher:

[theangrypit](https://clawhub.ai/user/theangrypit)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to create and refresh local documentation skills for a tool, SDK, API, or documentation repository. It guides them to map the source documentation and generate a Hindsight-style skill with local references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Upstream documentation may change or contain misleading guidance that is copied into a generated skill.

Mitigation: Choose official HTTPS sources and review and scan generated content before installing or publishing it.

Risk: Refreshing a generated skill replaces its generated files and normally fetches the latest documentation.

Mitigation: Use a dedicated output folder and review the refreshed files before relying on them.

Risk: Hash manifests confirm copying accuracy but do not establish that upstream content is trustworthy.

Mitigation: Assess the source itself; do not treat matching hashes as a trust check.

## Reference(s):

- [Docs Skill Model](references/docs-skill-model.md)
- [ClawHub skill release](https://clawhub.ai/theangrypit/skills/docs-skill-builder)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration, Guidance]

**Output Format:** [Shell script and Markdown skill files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a local docs-skill source bundle with a generator, a skill guide, and mirrored references.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
