## Description:

Yotta-learn helps agents capture mistakes, user corrections, and useful insights as reusable project-local .learnings entries for later review, promotion, and skill improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to maintain a reusable learning log across agent sessions, especially after command failures, user corrections, stale knowledge, external-interface failures, or missing capability requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional hooks and installers can persist agent behavior more broadly than users may expect.

Mitigation: Install only for the intended agent or directory, avoid global installation unless broad activation is desired, and review hook configuration before merging it.

Risk: .learnings content is persistent workspace memory and may capture sensitive, proprietary, or untrusted text if used carelessly.

Mitigation: Review and sanitize entries before promote, extract, or --remember, and avoid recording secrets or full confidential content unless explicitly required.

## Reference(s):

- [Examples and Field Reference](references/examples.md)
- [Hook Setup Reference](references/hooks-setup.md)
- [Hook Integration Guide](hooks/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown entries, concise command guidance, and optional code or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes project-local .learnings files and can optionally produce promoted guidance or skill skeletons from selected entries.]

## Skill Version(s):

0.1.4 (source: SKILL.md frontmatter, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
