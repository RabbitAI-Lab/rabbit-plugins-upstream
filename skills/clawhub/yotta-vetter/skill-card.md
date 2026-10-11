## Description:

Reviews agent skills before installation using a four-stage checklist covering source, code, permissions, and risk, with a lightweight checker and optional guidance for deeper scanning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users review skills from marketplaces, repositories, or collaborators before installation and record findings for a human installation decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation can persist this skill across multiple agent skill directories.

Mitigation: Install only into the specific trusted agent or skills directory needed; avoid global installation unless intended.

Risk: The npm installer has a verified symlink-handling weakness in shared or untrusted workspaces.

Mitigation: Avoid installing into shared or untrusted workspaces where another user can pre-create symlinks in the target skills directory.

Risk: Running an unpinned npm release through npx can install an unreviewed version.

Mitigation: Review the package or pin its npm version before running npx.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/yottameta/skills/yotta-vetter)
- [Project homepage (listed in skill metadata)](https://github.com/YottaMeta/yotta-vetter)
- [Four-stage vetting checklist](references/checklist.md)
- [Vetting report template](references/vetting-report-template.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands]

**Output Format:** [Markdown vetting report or JSON findings, with optional follow-up scan command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Risk ratings and findings are preliminary; the final installation decision requires human confirmation.]

## Skill Version(s):

0.2.7 (source: release evidence, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
