## Description:

Identifies and removes supported AI watermarks and provenance marks in images, video, audio, and text the user generated or edited, excluding marks on third-party paid assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wiltodelta](https://clawhub.ai/user/wiltodelta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use the skill to inspect files for supported AI provenance signals and, when appropriate, remove supported marks from content they generated or edited. It guides them to preserve accurate origin claims and avoid removing marks that protect third-party paid assets.

### Deployment Geography for Use:

Global; the skill documentation states that use is prohibited in mainland China.

## Known Risks and Mitigations:

Risk: Scanner confidence is medium and coverage is incomplete; the probe script was only partially inspected, and the security guidance notes undeclared file and shell capabilities.

Mitigation: Review the uninspected probe code and confirm its file and shell access fits your environment before installing or using the skill.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wiltodelta/skills/remove-ai-watermarks)
- [Project homepage (metadata link)](https://raiw.cc)
- [Project repository (metadata link; provenance unavailable)](https://github.com/wiltodelta/remove-ai-watermarks)
- [Command reference](references/commands.md)
- [Installation guide](references/install.md)
- [Python API guide](https://github.com/wiltodelta/remove-ai-watermarks/blob/main/docs/python-api.md)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Shell commands, Files]

**Output Format:** [Markdown guidance and shell command examples; processed media files when a CLI command is run]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output files vary by input media and selected operation.]

## Skill Version(s):

1.0.23 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
