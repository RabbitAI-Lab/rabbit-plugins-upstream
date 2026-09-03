## Description:

Video search tool: queries Pixabay video API by keywords and returns stock video URLs and metadata for footage sourcing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, content creators, and agent users use this skill to search for stock video footage by keyword and retrieve video URLs and metadata for sourcing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence marks the release suspicious because it advertises a narrow Pixabay video search while installing a broader dLazy CLI.

Mitigation: Install only when broader dLazy CLI use is acceptable, prefer npx for per-run execution, and review the package or source before using additional dlazy commands.

Risk: Search parameters are sent to dLazy services and a dLazy API key may be stored in local CLI configuration.

Mitigation: Avoid sensitive search parameters, prefer per-run DLAZY_API_KEY when persistence is not wanted, and rotate or revoke the API key from the dLazy dashboard if needed.

Risk: dLazy file storage or local downloads may be used when save options or broader CLI behaviors are invoked.

Mitigation: Avoid passing local files unless explicitly needed and choose local download paths deliberately.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON responses with video URLs and metadata, plus optional Markdown command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async runs can return a task identifier; save options may download result assets to a local path.]

## Skill Version(s):

1.3.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
