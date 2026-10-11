## Description:

Search the ElevenLabs voice library by keyword, source, and category to help choose a voice using preview samples.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers search for ElevenLabs voices by description, source, or category and review previews before choosing a voice for text-to-speech.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the third-party CLI and storing or passing its API key exposes credentials to a service outside the agent.

Mitigation: Review the pinned package before installing; use the on-demand npx form if a global installation is unnecessary, and handle the API key carefully.

Risk: Search prompts are sent to dLazy's hosted service, and local paths supplied to media fields may upload files.

Mitigation: Avoid sensitive prompts and provide local file paths only when an upload is intentional.

Risk: The voice-search purpose conflicts with artifact documentation describing generation, file uploads, and image output.

Mitigation: Check the command's actual behavior and returned data before relying on previews or sharing outputs.

## Reference(s):

- [dLazy CLI repository (publisher-provided link; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown guidance and JSON search results with preview links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search filters include keyword, voice source, category, and result count.]

## Skill Version(s):

1.3.27 (source: ClawHub release metadata; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
