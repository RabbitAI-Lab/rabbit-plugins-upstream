## Description:

Fully automated multi-round code iteration with configurable N-dimension parallel review, onboarding/personalization, and a cross-assistant installer/update system with mandatory SHA256 checksum verification. v3.0 adds a dual-mode (the original iterate mode plus a defensive-programming mode via /iterate defensive) that performs normal incremental coding tasks with defensive discipline end-to-end.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use Iterate to have an AI coding assistant run multi-round code reviews, fix scoped issues, validate changes, and produce convergence summaries. They can use defensive mode for incremental coding tasks with pre-checks, post-checks, and an invariant delivery gate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform autonomous file edits, git operations, and configured validation commands.

Mitigation: Use it only on trusted repositories, review proposed changes before merging, and inspect iterate.config.yaml validation commands before running.

Risk: The security evidence flags possible remote publishing behavior despite push being described as disabled by default.

Mitigation: Keep merge and push settings disabled unless explicitly intended, and remove or override final-session/resume git push behavior before use.

Risk: Installer and update paths can replace assistant skill files or fetch remote release artifacts.

Mitigation: Avoid curl|bash install paths, rely on checksum-verified artifacts, and use --force or update only when replacement is intended.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jingzhao-l/skills/iterate-skill)
- [Agents Skills Specification](https://agentskills.io/)
- [npm Installer Package](https://www.npmjs.com/package/iterate-skill-installer)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, code edits, configuration updates, and review/convergence summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May edit repository files, run configured validation commands, and create or update project knowledge files depending on mode and user approval.]

## Skill Version(s):

3.4.2 (source: SKILL.md frontmatter and pyproject.toml; ClawHub release evidence agrees)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
