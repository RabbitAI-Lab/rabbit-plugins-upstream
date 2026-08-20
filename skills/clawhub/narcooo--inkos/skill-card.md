## Description:

Story Creation and Translation AI Agent with Studio Chat, CLI, and TUI - use for long-form novels, short fiction, scripts, storyboards, interactive-film projects, open-world / branching play, fan fiction, spinoffs, style imitation, continuations, covers, and multilingual EPUB/PDF/TXT/Markdown translation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[narcooo](https://clawhub.ai/user/narcooo)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, writers, and creative teams use InkOS to drive long-form story creation, translation/localization, scripts, storyboards, interactive fiction, cover workflows, research reports, and project state through Studio Chat, CLI, or TUI workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: InkOS can store large creative projects, story state, memory, logs, and generated artifacts in the selected project directory.

Mitigation: Use project-scoped directories, review stored files, export backups intentionally, and delete books or projects when retention is no longer desired.

Risk: Selected content can leave the machine when users configure LLM, image, web-search, aggregator, or custom provider endpoints.

Mitigation: Use environment-backed secrets, configure only trusted provider URLs, and review each provider's data policy before enabling it.

Risk: Studio and daemon workflows can run local services, with Studio defaulting to a localhost listener.

Mitigation: Start local services only when needed, bind them to trusted local ports, and stop daemon or Studio sessions when work is complete.

Risk: Imported project-local skills can influence agent behavior for creative and production workflows.

Mitigation: Review imported skills before use and keep normal host confirmation gates for file edits, exports, network use, and image generation.

## Reference(s):

- [ClawHub InkOS skill page](https://clawhub.ai/narcooo/skills/inkos)
- [InkOS homepage](https://github.com/Narcooo/inkos)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can guide creation of project files such as manuscripts, translations, scripts, storyboards, covers, research reports, and story-state artifacts when the host confirms and executes matching tools.]

## Skill Version(s):

2.9.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
