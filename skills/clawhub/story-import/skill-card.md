## Description:

Imports an existing novel manuscript and rebuilds it into a structured writing project that can be continued with compatible long-form or short-form story workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Authors and agent operators use this skill to import an existing partial or completed novel, analyze it by length, and create a continuation-ready writing project with settings, outlines, manuscript files, tracking state, and analysis assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads manuscript files and creates or updates writing-project directories.

Mitigation: Run it from the intended project workspace and review the detected book title and paths before confirming.

Risk: Existing project tracking files may be updated or archived during import or migration.

Mitigation: Keep a backup when the project already has older tracking files.

## Reference(s):

- [OpenClaw source metadata](https://github.com/worldwonderer/oh-story-claudecode)
- [Character State Reverse](references/character-state-reverse.md)
- [Format and Structure](references/format-and-structure.md)
- [Length Routing](references/length-routing.md)
- [State Tracking](references/state-tracking.md)
- [Structure Mapping Long](references/structure-mapping-long.md)
- [Structure Mapping Short](references/structure-mapping-short.md)
- [Tracking Transaction](references/tracking-transaction.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown project files, JSON tracking state, shell commands, configuration updates, and concise agent guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates a writing-project directory from a user-provided manuscript and may use a bundled tracking script for state files.]

## Skill Version(s):

1.0.17 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
