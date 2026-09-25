## Description:

Helps agents discover, assess, install, and manage skills across marketplaces and local catalogs, with offline search and pre-install scanning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cdhewei](https://clawhub.ai/user/cdhewei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to find and compare agent skills, review candidates before installation, and manage installed skills through updates, removal, and duplicate detection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The community update and scanning paths can allow risky skill code to be installed despite the advertised safety gate.

Mitigation: Prefer the host's native marketplace; do not rely on this skill's community update or installation safety gate until the update force bypass and filename-based scanner exclusion are fixed.

Risk: Downloaded community archives may contain unsafe code, and updates may replace existing skill files.

Mitigation: Manually inspect downloaded archives, back up existing skill directories, and avoid routine community updates without explicit review.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/cdhewei/skills/find-skills-plusplus)
- [Security review guide](references/security.md)
- [CLI reference](references/cli.md)
- [Ranking reference](references/ranking.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown recommendations and CLI text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ranked candidates, quality and risk assessments, and installation or maintenance steps.]

## Skill Version(s):

5.3.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
