## Description:

Helps users plan skill combinations, route requests, inventory installed skills, and manage installations and distribution across local agent environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to choose and inventory skills, then preview and manage their installation, updates, and distribution across local agent hosts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Install, update, migration, and linking operations can change skills across multiple local agent directories.

Mitigation: Review target directories and preview planned changes with dry-run or equivalent confirmation before applying them.

Risk: Registry downloads and optional local providers can introduce untrusted code.

Mitigation: Prefer pinned versions and trusted providers, retain the pre-install scan, and avoid bypassing it except for emergencies.

## Reference(s):

- [Project homepage](https://github.com/YottaMeta/yotta-skills)
- [Skill Hub guide](references/hub.md)
- [Skill orchestration guide](references/orchestration.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, JSON]

**Output Format:** [Text or JSON with suggested commands and skill routing results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Installation and hub commands can change local skill directories and configuration.]

## Skill Version(s):

0.30.3 (source: skill frontmatter, release metadata, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
