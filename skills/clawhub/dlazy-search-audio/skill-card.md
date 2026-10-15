## Description:

Searches Pixabay Music for royalty-free background music and returns track links and metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and agents search for background music using short style keywords and review track links and metadata before selection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms are sent to dLazy's hosted service.

Mitigation: Avoid sensitive queries and use the service only if its data handling is acceptable.

Risk: The CLI stores an API key locally; local file paths passed to the CLI may trigger uploads to dLazy storage.

Mitigation: Protect the API key and pass local file paths only when an upload is intended.

Risk: Installing a third-party CLI runs external package code.

Mitigation: Review the package before use and prefer the documented version-pinned npx invocation when a global installation is unnecessary.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-search-audio)
- [dLazy CLI source (package metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Track links and metadata in agent responses; JSON from the CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Track links appear in the url field; searches accept keyword and duration filters.]

## Skill Version(s):

1.3.30 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
