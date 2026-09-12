## Description:

Git-based version control for AI Agent Skills - detect, review, save, and restore Skill changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[johnsonbuilds](https://clawhub.ai/user/johnsonbuilds)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and agent operators use SkillSync to review, snapshot, synchronize, and restore AI Agent Skill directories with Git-centered workflows before or after agents modify them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer and installation flows can create supply-chain exposure or elevated local package changes.

Mitigation: Review before installing, prefer a pinned package or audited local checkout, and avoid granting sudo during install.

Risk: Snapshot or sync workflows can commit and upload sensitive or unrelated files from the Skills directory.

Mitigation: Use only a private remote and inspect the Skills directory for tokens and unrelated files before snapshot or sync.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/johnsonbuilds/skills/skillsync)
- [Server-resolved GitHub Provenance](https://github.com/johnsonbuilds/skillsync)
- [Skill Definition](https://github.com/johnsonbuilds/skillsync/blob/main/SKILL.md)
- [Product Overview](docs/product.md)
- [Functional Design](docs/functional-design.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and command output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user confirmation before any skillsync command; requires git and skillsync, with optional SKILLSYNC_SKILLS_DIR configuration.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact SKILL.md and pyproject.toml declare 0.3.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
