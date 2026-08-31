## Description:

Launches and guides use of a local AI reading companion web app that connects to WeRead APIs, generates whole-book Mermaid diagrams, supports selection of popular highlights, runs a five-round Socratic reading dialogue, and exports Markdown notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

Readers and developers use this skill to run a local reading coach that searches WeRead, summarizes book structure into diagrams, helps users reflect on selected highlights through Socratic dialogue, and exports personal study notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local app uses a WeRead API key and selected reading text to provide search, highlight, diagram, and dialogue features.

Mitigation: Use the skill only on a trusted local machine, keep the WeRead key revocable, and avoid selecting sensitive private text.

Risk: Selected highlights and chat answers are sent to the AI provider configured by the user.

Mitigation: Choose an acceptable provider endpoint, use a limited or revocable LLM API key, and clear saved keys from the app settings when finished.

Risk: Exported Markdown notes can contain copyrighted book highlights.

Mitigation: Keep exported notes for personal study unless the user has rights to redistribute the source text.

## Reference(s):

- [WeRead Agent API Reference](references/weread-api.md)
- [ClawHub Skill Page](https://clawhub.ai/bonniegeng-max/skills/weread-socrates)
- [Project Homepage](https://github.com/bonniegeng-max/weread-socrates)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown, Code, Files]

**Output Format:** [Markdown guidance with inline shell commands; the local app can export Markdown notes, Mermaid diagram code, and PNG diagram files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and WEREAD_API_KEY for WeRead access; diagram and dialogue features require a user-configured AI provider API key.]

## Skill Version(s):

1.1.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
