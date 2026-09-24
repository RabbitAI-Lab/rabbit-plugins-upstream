## Description:

Note helps agents capture, organize, retrieve, and connect local notes by topic, project, context, and related ideas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticio](https://clawhub.ai/user/agenticio)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use Note to persist local notes, retrieve previous context, prepare from stored notes, and synthesize related ideas across topics and projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Notes are saved locally in plaintext and may contain sensitive personal or work information.

Mitigation: Avoid storing secrets or highly sensitive data, and manage retention and deletion in the local notes directory.

Risk: Ordinary conversation could be persisted if the agent treats ambiguous wording as a note-taking request.

Mitigation: Use explicit note-taking commands and confirm intent before capturing potentially sensitive content.

Risk: Captured note previews may appear in command output or logs.

Mitigation: Review logs and command output handling when capturing private content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/agenticio/skills/note)
- [Publisher profile](https://clawhub.ai/user/agenticio)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell command examples and local JSON note files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stores note data locally in plaintext under the user's OpenClaw workspace.]

## Skill Version(s):

2.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
