## Description:

Fully automated multi-round code iteration with configurable N-dimension parallel review, onboarding/personalization, and a cross-assistant installer/update system with mandatory SHA256 checksum verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use Iterate to have an AI assistant run multi-round code review, fix eligible issues, verify changes, and converge on a cleaner codebase. It also supports defensive-programming mode for normal coding tasks that need pre-checks, post-checks, invariant checks, and a final review gate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can drive automated code changes, shell commands, and git workflows in a repository.

Mitigation: Use it only in repositories you trust, review proposed changes before merging, and keep git.auto_merge and git.push_per_round disabled unless automated propagation is intentional.

Risk: The installer can place a persistent iterate command on PATH.

Mitigation: Use --no-cli if a persistent CLI install is not desired, or choose a manual install path that fits the environment.

Risk: The README includes a curl-to-bash harness install path.

Mitigation: Avoid that install path unless it has been reviewed and trusted for the target environment.

Risk: Validation commands are configurable and may execute project-specific tools.

Mitigation: Review iterate.config.yaml before use and keep validation commands limited to exact trusted commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jingzhao-l/skills/iterate-skill)
- [Skill instructions](artifact/SKILL.md)
- [Project README](artifact/README.md)
- [Configuration schema](artifact/config/config.schema.json)
- [Default configuration](artifact/config/iterate.config.yaml)
- [License](artifact/LICENSE)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline code blocks, command proposals, review findings, configuration edits, and implementation summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May modify files and propose or run validation commands depending on mode and configuration.]

## Skill Version(s):

3.2.2 (source: SKILL.md frontmatter, pyproject.toml, npm package.json, CHANGELOG, ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
