## Description:

Guides agents to identify or remove AI watermarks and provenance marks from user-owned images, video, and text, while excluding marks that protect third-party paid assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wiltodelta](https://clawhub.ai/user/wiltodelta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the skill to inspect user-owned images, video, and text for AI labels or provenance marks, then remove a specified mark when authorized and supported.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scan is partial and notes undeclared tool scope, file-write capability, and a subprocess call.

Mitigation: Review the skill’s command and tool scope before installation or execution, and use it only on content you generated or edited and are allowed to change.

## Reference(s):

- [ClawHub release](https://clawhub.ai/wiltodelta/skills/remove-ai-watermarks)
- [Project repository](https://github.com/wiltodelta/remove-ai-watermarks)
- [Python API guide](https://github.com/wiltodelta/remove-ai-watermarks/blob/main/docs/python-api.md)
- [Project homepage](https://raiw.cc)
- [Install extras](references/install.md)
- [Command recipes](references/commands.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Files]

**Output Format:** [Concise Markdown status and command guidance, with processed image, video, or text files when a requested operation succeeds.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports only actions supported by observed command results; local signal absence is not proof that content is clean or human-made.]

## Skill Version(s):

1.0.19 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
