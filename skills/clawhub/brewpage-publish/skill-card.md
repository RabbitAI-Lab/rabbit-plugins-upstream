## Description:

Publish HTML, markdown, text, files, or multi-file sites to brewpage.app and return an instant public URL with optional namespace and password choices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kochetkov-ma](https://clawhub.ai/user/kochetkov-ma)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users invoke this skill when they need to publish local text, markdown, files, or built static sites to brewpage.app for temporary sharing through a public URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish arbitrary selected local content to a public hosting service.

Mitigation: Use explicit invocations, review the exact file or directory before upload, avoid sensitive or source directories, and prefer password protection when appropriate.

Risk: Deletion owner tokens are stored in ./brewpage-history.md.

Mitigation: Keep the history file private and out of version control, and do not share token contents in conversation or public artifacts.

Risk: Shell-based publishing templates may run upload commands against unintended paths or parameters if invoked carelessly.

Mitigation: Review the resolved path, namespace, TTL, entry file, and password choice before execution.

## Reference(s):

- [BrewPage homepage](https://brewpage.app)
- [ClawHub skill page](https://clawhub.ai/kochetkov-ma/skills/brewpage-publish)
- [OpenClaw skills documentation](https://docs.openclaw.ai/tools/skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command blocks and public URL output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May append private deletion tokens to ./brewpage-history.md; conversation output should contain only the public URL.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
