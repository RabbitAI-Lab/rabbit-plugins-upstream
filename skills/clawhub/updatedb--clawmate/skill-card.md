## Description:

ClawMate helps agents manage local projects, generate file preview links, process feedback, and guide project initialization and planning workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[updatedb](https://clawhub.ai/user/updatedb)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use ClawMate to work with ClawMate-managed local projects: listing projects, linking files for preview, creating project structures, maintaining planning documents, and processing feedback through a trusted ClawMate service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can route actions through a configurable ClawMate service endpoint.

Mitigation: Install only when the configured CLAWMATE_URL points to a trusted service, preferably a loopback localhost endpoint; do not use an untrusted or plain remote host.

Risk: Project initialization, planning, and feedback handling can create directories, write files, and initialize Git repositories.

Mitigation: Review project paths, generated curl commands, and feedback items before approving file changes or repository initialization.

Risk: Shell command examples may handle project names, file paths, and feedback content supplied by users or projects.

Mitigation: Encode query parameters and JSON bodies, prefer quoted heredocs or argument-safe APIs, and inspect generated commands before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/updatedb/skills/clawmate)
- [Project homepage](https://github.com/updatedb/clawmate)
- [Packaged skill instructions](artifact/SKILL.md)
- [Packaged license text](artifact/LICENSE.txt)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration examples, and project-document templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ClawMate API calls, file paths, preview links, project planning documents, and feedback-processing steps.]

## Skill Version(s):

2.9.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
