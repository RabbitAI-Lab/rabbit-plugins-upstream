## Description:

Image search tool: queries Pixabay image API by keywords and returns image URLs and metadata for references, backgrounds, and design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative agents use this skill to search for image URLs and metadata by keyword when selecting references, backgrounds, or design assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, parameters, and explicitly referenced local media files may be sent to dLazy services.

Mitigation: Use the skill only when that service boundary is acceptable, and avoid passing local file paths unless upload is intended.

Risk: The skill is described as Pixabay search, but execution is routed through dLazy API and file services.

Mitigation: Review dLazy service behavior and terms before deployment, and make the dLazy operational boundary clear to users.

Risk: A global CLI install persists executable tooling on the host environment.

Mitigation: Prefer the pinned npx invocation or another isolated execution path, and review the pinned package before use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-search-image)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON responses with image URLs and metadata, plus Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async invocations may return a generateId for later polling; --save can download a returned asset to a local path.]

## Skill Version(s):

1.3.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
