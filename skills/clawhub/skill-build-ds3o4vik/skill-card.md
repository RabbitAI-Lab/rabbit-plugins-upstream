## Description:

Find Skills is a scenario- and keyword-driven skill discovery assistant that recommends and helps install matching skills from built-in, local, marketplace, GitHub, and ClawHub sources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guipi888](https://clawhub.ai/user/guipi888)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and WorkBuddy users use this skill to describe a task in natural language, discover relevant skills across local and remote sources, compare recommendations, and install a selected skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform broad remote skill searches and recommend installation actions.

Mitigation: Require explicit user confirmation before remote searches or installs, and review the recommended skill source before installation.

Risk: GitHub search behavior may use GITHUB_TOKEN when present.

Mitigation: Expose GITHUB_TOKEN only when needed and prefer least-privilege tokens for search-only workflows.

Risk: Artifact behavior requires a promotional footer in every response.

Mitigation: Remove or ignore forced promotional output before deployment in controlled or enterprise environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/guipi888/skills/skill-build-ds3o4vik)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown recommendations with command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include recommended skill sources, ranking rationale, install commands, and source links.]

## Skill Version(s):

1.7.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
