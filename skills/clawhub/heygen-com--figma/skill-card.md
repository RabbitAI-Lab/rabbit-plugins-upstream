## Description:

Figma helps agents import Figma content into HyperFrames compositions, including rendered assets, brand tokens, components, storyboard motion, connector-assisted motion, and shader assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and designers use this skill to bring Figma designs, frames, logos, brand tokens, components, animations, shaders, and storyboard sections into HyperFrames video or composition projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to run unpinned HyperFrames update and telemetry commands that may execute registry code or change reviewed tooling at runtime.

Mitigation: Review and pin the `hyperframes` package version before installation or execution, and approve update or telemetry commands only after understanding what they run or send.

Risk: The workflow requires access to Figma content through a personal access token.

Mitigation: Use a read-only Figma token scoped only to the files and permissions needed for the import, and store it outside the conversation in the shell environment or project `.env`.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/figma)
- [Publisher profile](https://clawhub.ai/user/heygen-com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may lead an agent to create local frozen media files, component files, token sidecars, manifests, and motion verification output.]

## Skill Version(s):

1.0.14 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
