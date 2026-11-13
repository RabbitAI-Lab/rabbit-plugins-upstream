## Description:

Turn your agent skill into a varg how to listing: reads a skill folder or repo, checks it against the varg media skill standard, fills the one card format every listing on varg how to (varg.ai/how-to) uses — name, one-line summary, use-when triggers, category, install command, a real example of the output — shows it to the person and publishes it for review through the varg MCP publish_skill tool (or the API with a varg key). Use when someone says "publish my skill", "list this skill on varg", "submit my skill to varg how to", "add my skill to the catalog", "how do I get my skill found by agents", or the same in any language. Not for finding a skill (use how-to-make-ai-video), not for writing the skill itself, and not for contributing to the vargHQ/skills repo (that is a pull request).

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers who maintain agent skills use this to turn a skill folder or repository into a varg how-to listing and submit it for review after approving the exact card.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented npx skills add command is unpinned, so a future install may retrieve changed content.

Mitigation: Review the package before installing and pin a version when the installer supports it.

Risk: Scanner coverage is incomplete because a local reference was unresolved.

Mitigation: Review the skill files and required permissions before installing, including whether its skill-search capability is appropriate.

## Reference(s):

- [Varg publish guide](https://varg.ai/how-to/publish)
- [Varg Publish Skill page](https://clawhub.ai/vargai/skills/varg-publish-skill)
- [Publisher profile: vargai](https://clawhub.ai/user/vargai)
- [Skill instructions](artifact/SKILL.md)
- [Varg how-to card format](artifact/references/card.md)
- [Varg standard checklist](artifact/references/standard-checklist.md)

## Skill Output:

**Output Type(s):** [Markdown, API Calls, Guidance]

**Output Format:** [Markdown listing card and submission request]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Publishing requires a varg account through the MCP or a VARG_API_KEY for API submission; publishing is free.]

## Skill Version(s):

1.0.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
