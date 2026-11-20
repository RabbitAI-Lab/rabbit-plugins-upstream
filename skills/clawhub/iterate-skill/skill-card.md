## Description:

Guides coding assistants through iterative code review and repair, with parallel review dimensions and a defensive programming mode.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use Iterate to review and improve code across multiple dimensions, or to complete incremental coding tasks with defensive checks and validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The available security assessment rates this release suspicious with high confidence, citing concerns about scope, network and installation paths, credential handling, persistent changes, and a path-deletion flaw; scan coverage is partial.

Mitigation: Before installing, review the verdict and partial scan; inspect signing-key and secret-provisioning behavior, installer and update verification, network destinations, sensitive-file handling, and uninstall path behavior.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/jingzhao-l/skills/iterate-skill)

## Skill Output:

**Output Type(s):** [Code, Markdown, Shell commands, Configuration]

**Output Format:** [Code changes, shell commands, and Markdown reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read and modify project files; review-only mode is read-only.]

## Skill Version(s):

3.16.0 (source: release metadata, SKILL.md frontmatter, pyproject.toml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
