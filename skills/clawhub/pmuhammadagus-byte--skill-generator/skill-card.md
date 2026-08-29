## Description:

Transforms unstructured ideas, notes, workflows, and repeated procedures into structured OpenClaw SKILL.md guidance with validation, error handling, and safety checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent builders use this skill to convert rough requirements, operational notes, or repeated workflows into reusable OpenClaw skills. It is most useful when the desired skill needs clear triggers, inputs, workflow steps, validation, recovery behavior, and security guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated skills may include workflows involving credentials, network services, scheduled tasks, or destructive commands.

Mitigation: Review and scan each generated skill before publishing or running it, and require confirmation before any high-impact operation.

Risk: A generated skill could expose or mishandle secrets if raw user material includes real tokens or keys.

Mitigation: Use placeholders for credentials and remove any real secrets from skill text, examples, and configuration snippets.

Risk: Generated instructions can be incorrect when the input lacks platform, tool, or dependency details.

Mitigation: Mark assumptions clearly and verify commands, paths, tools, and environment constraints before treating the generated skill as ready.

## Reference(s):

- [Source Skill Definition](artifact/SKILL.md)
- [README](artifact/README.md)
- [ClawHub Skill Page](https://clawhub.ai/pmuhammadagus-byte/skills/skill-generator)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance and generated SKILL.md content, with optional command and configuration examples when supported by the input.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated content should identify assumptions, avoid unsupported technical claims, and include validation and recovery notes.]

## Skill Version(s):

1.0.0 (source: release metadata, _meta.json, SKILL.md metadata.openclaw.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
