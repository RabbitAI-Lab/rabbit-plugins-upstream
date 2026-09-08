## Description:

Starts and guides use of a local AI reading companion web app that connects WeRead book data with user-configured AI providers for book search, structure maps, highlight-based Socratic dialogue, reading summaries, and Markdown note export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

Developers and readers use this skill to launch a local WeRead companion app, configure required API keys, and work through book highlights with AI-generated maps, guided dialogue, summaries, and exportable notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local app uses the user's WeRead API key and may process selected highlights, personal thoughts, and chat answers.

Mitigation: Install only if comfortable with that access, keep the key local to the intended machine, and stop the local server when finished.

Risk: Selected reading content and chat answers can be sent to the AI provider configured by the user.

Mitigation: Review the chosen provider endpoint before generating maps, dialogue, or summaries, and clear saved AI keys from the settings panel when they are no longer needed.

Risk: The bundled Mermaid dependency is large and minified, which limits manual inspectability.

Mitigation: Rely on the ClawHub scan result, publisher trust, and package provenance before deployment.

Risk: Exported Markdown notes can contain copyrighted book excerpts.

Mitigation: Use exported notes for personal study and avoid public redistribution.

## Reference(s):

- [WeRead API reference](references/weread-api.md)
- [weread-socrates GitHub repository](https://github.com/bonniegeng-max/weread-socrates)
- [weread-socrates ClawHub listing](https://clawhub.ai/bonniegeng-max/skills/weread-socrates)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown, Files]

**Output Format:** [Markdown guidance with inline shell commands and locally generated Markdown note files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and WEREAD_API_KEY; AI provider keys are configured by the user in the local web app.]

## Skill Version(s):

1.2.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
