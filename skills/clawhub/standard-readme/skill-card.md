## Description:

Writes or audits README files following the Standard Readme specification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and documentation maintainers use this skill to create, rewrite, improve, or audit README files against the Standard Readme structure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated README content or audit guidance can be inaccurate if project metadata, license files, or source layout are incomplete or stale.

Mitigation: Review generated README sections, install commands, usage examples, and license statements against the repository before publishing.

Risk: README rewriting may require reading project files that contain internal implementation details.

Mitigation: Use the skill only in workspaces where repository inspection is acceptable, and avoid including secrets or unrelated sensitive files in the prompt context.

## Reference(s):

- [Standard Readme specification](https://github.com/RichardLitt/standard-readme)
- [ClawHub skill page](https://clawhub.ai/tenequm/skills/standard-readme)
- [Project homepage](https://github.com/tenequm/skills/tree/main/skills/standard-readme)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown README content or concise audit findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May inspect project files such as manifests, license files, contributing docs, CI config, and source layout to avoid inventing details.]

## Skill Version(s):

0.1.4 (source: evidence release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
