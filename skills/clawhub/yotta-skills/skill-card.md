## Description:

元阁 yotta-skills is a Node.js CLI skill that lists, installs, updates, previews, and pins the YottaMeta yotta-* skill family into a selected agent or directory without bundling the skill bodies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to inspect, install, and update the YottaMeta skill family in supported agent environments or explicit skill directories. It is most useful when a user wants a repeatable bulk installation workflow with dry-run preview and optional pinned versions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bulk install or update can persistently modify many agent skill directories and replace existing yotta-* folders, which may remove local edits.

Mitigation: Run --dry-run first, choose an explicit --dir or --agent target, back up or review existing yotta-* folders before install/update, and use --pin for reproducible versions.

Risk: The installer downloads each selected skill from its own npm package, so users need to trust the YottaMeta skill family and the resolved package versions.

Mitigation: Install only when the publisher and skill family are trusted; prefer pinned versions for repeatability and review any yotta-verify pre-install summaries before using installed skills.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-skills)
- [npm package: @yottameta/yotta-skills](https://www.npmjs.com/package/@yottameta/yotta-skills)
- [Install flow reference](references/install-flow.md)
- [Yotta skill family list](references/skill-list.md)
- [Chinese tutorial](references/tutorial.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and install/update summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run plans, target-directory guidance, version strategy notes, and scan-summary prompts.]

## Skill Version(s):

0.1.2 (source: SKILL.md frontmatter, CHANGELOG.md, package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
