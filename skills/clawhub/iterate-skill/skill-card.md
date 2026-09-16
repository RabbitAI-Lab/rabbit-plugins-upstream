## Description:

Fully automated multi-round code iteration with configurable N-dimension parallel review, onboarding/personalization, and a cross-assistant installer/update system with mandatory SHA256 checksum verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use Iterate to have an AI coding assistant run multi-round code review, apply approved fixes, verify changes, and repeat until the codebase converges or reaches a configured round limit. It also supports defensive-programming mode for normal incremental coding tasks with pre-checks, post-checks, and delivery gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Autonomous review and fixing can make unexpected code changes or publish Git history if merge or push settings are enabled.

Mitigation: Review the skill before use on sensitive or proprietary repositories, keep git.auto_merge and git.push_per_round disabled, and require explicit confirmation before any final push.

Risk: The release evidence flags an unsafe documented auxiliary curl-to-bash harness installer path.

Mitigation: Use the verified npx or source installation paths instead of the documented curl-to-bash harness installer.

Risk: Pinned build tooling may age and carry dependency risk when building from source.

Mitigation: Update and review pinned build tooling before source builds.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jingzhao-l/skills/iterate-skill)
- [README](artifact/README.md)
- [Skill Manifest](artifact/SKILL.md)
- [Release Notes](artifact/CHANGELOG.md)
- [Configuration Schema](artifact/config/config.schema.json)
- [Installer Package](https://www.npmjs.com/package/iterate-skill-installer)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries, code edits, shell command results, and configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or modify repository files, generate review reports, and run configured validation commands when invoked by an agent.]

## Skill Version(s):

3.4.0 (source: frontmatter, pyproject.toml, CHANGELOG, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
