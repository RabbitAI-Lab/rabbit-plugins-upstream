## Description: <br>
Publishes completed agent skills to GitHub, ClawHub, and SkillHub with safety checks, privacy cleanup, version checks, repository packaging, file exclusion handling, and dry-run validation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardwason](https://clawhub.ai/user/edwardwason) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill maintainers use this skill to prepare and publish completed agent skills across GitHub, ClawHub, and SkillHub. It is intended for release workflows that need pre-publish security scanning, privacy scrubbing, version conflict checks, platform-specific packaging, and explicit user confirmation before external publication. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: External publishing can make repository, ClawHub, and SkillHub changes public and difficult to reverse. <br>
Mitigation: Review the target repository, slug, version, changelog, and platform destination before confirming publication. <br>
Risk: Publishing requires access tokens for GitHub, ClawHub, and SkillHub. <br>
Mitigation: Use least-privilege tokens from environment variables, avoid hardcoding secrets, and avoid shared machines for SkillHub login where CLI tokens may be exposed in process listings. <br>
Risk: Local TRAE synchronization can overwrite installed skill files. <br>
Mitigation: Back up or dry-run before local sync and confirm the target installation path before allowing overwrites. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/edwardwason/skills/skill-publisher-ai) <br>
- [Project Homepage](https://github.com/EdwardWason/skill-publisher) <br>
- [Publishing Guide](references/publishing-guide.md) <br>
- [Publish Procedures Reference](references/publish-procedures.md) <br>
- [Security Audit Reference](references/security-audit.md) <br>
- [SkillHub Publishing Guide](references/skillhub-publishing.md) <br>
- [ClawHub Skill Format Documentation](https://github.com/openclaw/clawhub/blob/main/docs/skill-format.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown reports, tables, command snippets, generated or updated repository files, and publishing status summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires explicit user confirmation before external publishing and relies on platform tokens supplied through environment variables.] <br>

## Skill Version(s): <br>
5.21.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
