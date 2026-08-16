## Description: <br>
Story creation and translation AI agent with Studio Chat, CLI, and TUI support for long-form novels, short fiction, scripts, storyboards, interactive-film projects, open-world or branching play, fan fiction, spinoffs, style imitation, continuations, covers, and multilingual EPUB/PDF/TXT/Markdown translation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[narcooo](https://clawhub.ai/user/narcooo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, writers, and creative teams use InkOS to guide agents through writing, translation, research, cover generation, interactive fiction, and project workflow tasks. It is intended for local creative project work where generated files, story state, and provider configuration remain under user control. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Creative content and project memory can persist locally after generation. <br>
Mitigation: Review the selected project directory before sharing or committing files, and delete the book or project when its manuscripts, logs, state, and memory are no longer needed. <br>
Risk: Content and API keys can be exposed to configured LLM, image, web-search, aggregator, or custom provider endpoints. <br>
Mitigation: Use environment-backed or Studio-managed secrets, review provider data policies, and only configure custom base URLs that the user trusts. <br>


## Reference(s): <br>
- [ClawHub Skill Listing](https://clawhub.ai/narcooo/skills/inkos) <br>
- [InkOS Homepage](https://github.com/Narcooo/inkos) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, configuration guidance, and generated project files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the inkos and node binaries plus a user-supplied OPENAI_API_KEY. Generated manuscripts, translations, research reports, cover prompts, logs, story state, and memory can persist in the selected project until the user deletes the project or book.] <br>

## Skill Version(s): <br>
2.8.3 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
