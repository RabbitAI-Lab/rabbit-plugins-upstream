## Description:

Reverse-imports an existing novel into a standard writing project by analyzing completed or partial manuscript text, routing long and short works through the appropriate analysis pipeline, and preparing the result for continued writing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Authors and writing-agent users use this skill to convert an existing long-form or short-form Chinese novel manuscript into a resumable writing project with source text, analysis assets, outlines, settings, and tracking state. It is intended for explicit invocation when the user wants to continue or rebuild a manuscript project rather than only produce a one-off analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can cause an agent to read manuscript content and create or update persistent local writing-project files.

Mitigation: Invoke it explicitly, verify the selected manuscript path and project directory before execution, and keep a backup before allowing generated tracking, outline, and project files to be written.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-import)
- [OpenClaw source metadata](https://github.com/zenstory-ai/oh-story-claudecode)
- [Length routing rules](references/length-routing.md)
- [Long-form structure mapping](references/structure-mapping-long.md)
- [Short-form structure mapping](references/structure-mapping-short.md)
- [Tracking transaction protocol](references/tracking-transaction.md)
- [Character state reverse rules](references/character-state-reverse.md)
- [State tracking protocol](references/state-tracking.md)
- [Format and structure guidance](references/format-and-structure.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with file-structure instructions, JSON transaction examples, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces persistent local writing-project files and tracking state when followed by an agent.]

## Skill Version(s):

1.0.19 (source: ClawHub release metadata; artifact frontmatter declares 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
