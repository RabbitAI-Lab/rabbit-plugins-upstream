## Description: <br>
Skill Publisher 技能发布 helps agents publish completed skills to GitHub, ClawHub, and SkillHub with safety checks, version checks, repository structure generation, file exclusion, and dry-run validation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardwason](https://clawhub.ai/user/edwardwason) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill maintainers use this agent skill to prepare, scan, version, and publish existing skills across GitHub, ClawHub, and SkillHub. It is intended for user-confirmed publishing workflows, not for creating new skill content or general coding tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can publish code and metadata to external platforms using GitHub, ClawHub, and SkillHub credentials. <br>
Mitigation: Use it only for intentional public skill releases, review the target skill and version before confirming, and keep required tokens scoped and stored in environment variables. <br>
Risk: The workflow may synchronize to a local TRAE installation directory and overwrite an existing local version. <br>
Mitigation: Confirm the target path before local sync and follow the documented dry-run and backup guidance. <br>
Risk: SkillHub login exposes a token as a command argument in the CLI workflow. <br>
Mitigation: Run SkillHub login only on a controlled machine and avoid shared shells or logging around authentication commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/edwardwason/skills/skill-publisher-ai) <br>
- [Project homepage](https://github.com/EdwardWason/skill-publisher) <br>
- [Publishing Guide](references/publishing-guide.md) <br>
- [Publish Procedures Reference](references/publish-procedures.md) <br>
- [Security Audit Reference](references/security-audit.md) <br>
- [SkillHub Publishing Guide](references/skillhub-publishing.md) <br>
- [Repo Structure Reference](references/repo-structure.md) <br>
- [Change Detection and Version Bump Reference](references/change-detection.md) <br>
- [Changelog Generation Reference](references/changelog-generation.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown reports with command snippets, tables, file paths, and release status summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update repository files, release notes, ignore files, and local publishing logs when the user confirms publication.] <br>

## Skill Version(s): <br>
5.22.1 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
