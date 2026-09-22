## Description:

Find Skills++ helps agents discover, compare, vet, install, update, and govern skills with local static security scans, offline catalog search, quality scoring, and lifecycle commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cdhewei](https://clawhub.ai/user/cdhewei)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to find relevant skills, review their quality and security posture, and manage installation, updates, removal, duplicates, and local skill inventory across supported agent environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The authoritative security review reports serious implementation bugs that can bypass the update safety gate and remove more skills than the user selected.

Mitigation: Review the package carefully before installation, avoid update and uninstall workflows until those bugs are fixed and tested, and exercise the skill first in a disposable agent profile.

Risk: The skill manages installation, update, and removal of other skills, so mistakes or misuse can affect a user's local skill inventory.

Mitigation: Use explicit targets, inspect proposed actions before confirming, keep backups or trash-based recovery enabled, and prefer read-only audit, quality, and search commands before lifecycle changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cdhewei/skills/find-skills-plusplus)
- [Server-resolved GitHub provenance](https://github.com/cdhewei/find-skills-plusplus)
- [CLI reference](references/cli.md)
- [Security review reference](references/security.md)
- [Ranking reference](references/ranking.md)
- [Enhancements reference](references/enhancements.md)
- [Roadmap and limitations](references/roadmap.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional local CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce ranked skill recommendations, safety review summaries, lifecycle commands, local registry updates, and generated promotional or diagnostic text.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter reports 5.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
