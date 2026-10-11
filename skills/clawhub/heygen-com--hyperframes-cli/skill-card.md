## Description:

Guides developers through building, checking, previewing, and rendering HyperFrames video projects locally or through supported cloud services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams use this skill to scaffold and edit video compositions, diagnose build and render issues, review previews, and render or publish projects with the HyperFrames CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running an unpinned external CLI or project-local executables can execute code with local permissions.

Mitigation: Use a trusted project wrapper or pin the HyperFrames package version; avoid untrusted projects containing .hyperframes/bin executables.

Risk: Cloud renders, publishing, and feedback can transmit project content or incur charges.

Mitigation: Review the destination, uploaded files, and costs before running cloud render, publish, or feedback commands.

Risk: Deploy, destroy, or skill-install commands can change infrastructure or the local environment.

Mitigation: Review the exact command and target resources before execution, and require user approval for consequential changes.

## Reference(s):

- [HyperFrames CLI on ClawHub](https://clawhub.ai/heygen-com/skills/hyperframes-cli)
- [HyperFrames catalog search documentation](https://hyperframes.heygen.com/developers/catalog-search)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with commands and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide creation of project files and video renders.]

## Skill Version(s):

1.0.63 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
