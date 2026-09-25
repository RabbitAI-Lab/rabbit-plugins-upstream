## Description:

Knowledge capture and connection system for organizing, connecting, and retrieving notes from provided content, tags, keywords, and filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use this skill to capture note content, apply tags, connect related notes, and retrieve matching notes through an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review marks this release suspicious because it requests command execution and broad local search/read capabilities while its note workflows are only loosely scoped.

Mitigation: Review before installing, run only in a sandboxed agent environment, and restrict command execution and file access to the specific note-management task.

Risk: The artifact includes API key configuration examples and describes API integration, which can expose credentials if copied into logs, prompts, or version-controlled files.

Mitigation: Store credentials only in environment variables or a secrets manager, avoid hardcoding keys, and redact credentials from generated notes, logs, and shared outputs.

Risk: The skill is intended to process note content that may contain sensitive personal, business, or research information.

Mitigation: Limit input data to information appropriate for the active agent session, apply access controls to stored notes, and review retrieved content before sharing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/note)
- [SkillHub page](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with JSON examples and occasional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce structured note records, classifications, retrieval results, troubleshooting guidance, and configuration snippets.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
