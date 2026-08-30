## Description:

元造 yotta-skill-creator helps agents create Yotta skill scaffolds with naming validation, embedded templates, placeholder replacement, and a structure self-check.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gon-kvs](https://clawhub.ai/user/gon-kvs)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to start new yotta- skills from a compliant scaffold, including release files, bilingual README templates, install scripts, references, and optional Python CLI/test skeletons. It is also useful for self-use skills that should generate only the skill body before manual development.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad installation modes can copy the skill into multiple agent skill directories.

Mitigation: Prefer a specific --agent value or a carefully chosen --dir path; use -g only when installation across all listed agents is intentional.

Risk: Generated scaffolds are templates and can still contain author-editing placeholders or unfinished skill logic.

Mitigation: Review and complete generated SKILL.md, references, scripts, and tests before publishing or deploying the generated skill.

Risk: The submitted artifact appears to be missing files that its own full-release self-check expects, including .gitignore, .npmignore, and .github/workflows/publish.yml.

Mitigation: Verify generated full-release scaffolds with the self-check and add any missing release files before relying on the scaffold for publication.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gon-kvs/skills/yotta-skill-creator)
- [CLI Reference](references/cli-reference.md)
- [Scaffold Structure](references/scaffold-structure.md)
- [Tutorial](references/tutorial.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated scaffold files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated directory trees may include SKILL.md, README files, package metadata, install scripts, references, assets, and optional Python CLI/test skeletons.]

## Skill Version(s):

0.1.0 (source: SKILL.md frontmatter, package.json, CHANGELOG, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
