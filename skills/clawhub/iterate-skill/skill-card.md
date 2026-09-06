## Description:

Fully automated multi-round code iteration with configurable N-dimension parallel review, onboarding/personalization, a cross-assistant installer/update system with mandatory SHA256 checksum verification, and a dual mode for normal incremental coding tasks with defensive discipline end-to-end.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use Iterate to have an AI assistant review, fix, validate, and re-review codebases over multiple rounds until findings converge or a configured limit is reached. Its defensive mode supports normal incremental coding tasks with pre-checks, post-checks, and delivery-gate validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can exercise broad codebase edit, shell, and git authority, including repository-configured validation and invariant commands.

Mitigation: Install it project-scoped, run it only in trusted repositories, and review iterate.config.yaml before every run, especially validation.commands and invariants.commands.

Risk: Installation guidance includes a curl-to-shell path for the related harness.

Mitigation: Avoid piping remote scripts directly to a shell; prefer package-manager or source-based installation paths with checksum verification.

Risk: Automatic merge or push settings can publish changes before manual review if enabled.

Mitigation: Keep auto_merge and push_per_round disabled unless the diffs and target branch protections have been reviewed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jingzhao-l/skills/iterate-skill)
- [README](artifact/README.md)
- [Agent Skills](https://agentskills.io/)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown summaries, code changes, shell command proposals or executions, and configuration updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May edit repository files and run configured validation commands when invoked outside review-only mode.]

## Skill Version(s):

3.2.0 (source: frontmatter, pyproject.toml, CHANGELOG, ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
