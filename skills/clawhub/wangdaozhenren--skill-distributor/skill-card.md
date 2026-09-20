## Description:

Skill Distributor helps agents run preflight checks on local skill packages and publish approved releases to GitHub-backed registries and mirror platforms only when explicitly triggered.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangdaozhenren](https://clawhub.ai/user/wangdaozhenren)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill maintainers use this skill to validate SKILL.md packages, catch blocking publishing issues, and control multi-platform distribution for versioned skill releases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing tokens and local configuration can authorize high-impact release actions, including repository creation, forced branch pushes, tag publication, registry publishing, and mirror pushes.

Mitigation: Use narrowly scoped tokens, run dry-run first, verify the target GitHub repository and branch, and confirm each enabled platform before executing a release.

Risk: Untrusted local configuration may redirect publication through custom SkillHub commands or mirror URLs.

Mitigation: Inspect .skill-distributor/config.json in the target skill and avoid custom commands or mirror URLs from packages you do not control.

## Reference(s):

- [Platform Publishing Manual](artifact/references/platforms.md)
- [ClawHub Skill Page](https://clawhub.ai/wangdaozhenren/skills/skill-distributor)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown guidance with shell commands and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke local publishing scripts that create repositories, push Git tags, publish to registries, and mirror releases when explicitly run.]

## Skill Version(s):

1.1.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
