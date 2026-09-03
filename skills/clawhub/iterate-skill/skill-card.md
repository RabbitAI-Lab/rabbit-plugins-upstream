## Description:

Fully automated multi-round code iteration with configurable N-dimension parallel review, onboarding/personalization, and a cross-assistant installer/update system with mandatory SHA256 checksum verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use Iterate to have an AI coding assistant review, fix, validate, and re-review code across multiple quality dimensions until the requested work converges or reaches a configured limit. It also supports defensive incremental coding tasks with pre-checks, post-checks, and final validation gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can review and modify project code and run configured build or test commands.

Mitigation: Install it only for projects where automated review and code changes are intended, and review validation.commands before use.

Risk: Automatic merge or push behavior could publish or integrate changes before a human review.

Mitigation: Keep auto_merge and push_per_round disabled unless the release workflow deliberately requires them.

Risk: The installer can add the iterate CLI to PATH.

Mitigation: Use --no-cli or manual copy installation when automatic CLI installation is not desired.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jingzhao-l/skills/iterate-skill)
- [GitHub Repository](https://github.com/jingzhao-l/iterate-skill)
- [GitHub Releases](https://github.com/jingzhao-l/iterate-skill/releases)
- [npm Installer Package](https://www.npmjs.com/package/iterate-skill-installer)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with code, shell commands, configuration changes, and validation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May modify project files, run configured validation commands, and create local git branches or commits when the user enables those workflows.]

## Skill Version(s):

3.0.0 (source: frontmatter, pyproject.toml, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
