## Description:

Story Creation and Translation AI Agent with Studio Chat, CLI, and TUI - use for long-form novels, short fiction, scripts, storyboards, interactive-film projects, open-world / branching play, fan fiction, spinoffs, style imitation, continuations, covers, and multilingual EPUB/PDF/TXT/Markdown translation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT-0

## Use Case:

External authors, translators, and agent developers use InkOS to guide story creation, long-document localization, interactive narrative projects, traceable research, and related CLI, TUI, and Studio workflows. The skill helps agents select the right InkOS workflow and preserve project state, review status, source languages, target languages, provider choices, and generated files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: InkOS stores manuscripts, story state, memory, logs, and imported materials in project files.

Mitigation: Use project directories appropriate for the sensitivity of the manuscript, inspect generated files, and delete project or book data when retention is no longer wanted.

Risk: Selected content may be sent to configured LLM, image, search, aggregator, or custom providers.

Mitigation: Review each provider endpoint and data policy before enabling it, and use external research or image generation only when the user explicitly wants those capabilities.

Risk: Custom provider base URLs can receive the configured API key and submitted content.

Mitigation: Use only trusted or audited provider endpoints and avoid untrusted custom base URLs.

Risk: Credentials may be exposed if they are pasted into prompts, files, exports, or shell history.

Mitigation: Use environment-backed or Studio-managed secrets, avoid literal API keys in commands, and do not ask agents or imported skills to read, print, summarize, or transmit credentials.

Risk: The ClawHub skill descriptor is MIT-0, while the installed InkOS npm packages are described by the artifact as AGPL-3.0-only.

Mitigation: Verify the npm package and version before installation and review package license obligations before running, modifying, or distributing InkOS.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zuoyunlai/skills/inkos)
- [InkOS homepage](https://github.com/Narcooo/inkos)
- [kkaiapi documentation](https://kkaiapi.com/docs)
- [kkaiapi English documentation](https://en.kkaiapi.com/docs)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Text, JSON]

**Output Format:** [Markdown guidance with inline shell commands, configuration examples, workflow steps, and expected file or JSON outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents that use InkOS to create manuscripts, translations, scripts, storyboards, research reports, cover prompts, optional images, exports, and project files.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
