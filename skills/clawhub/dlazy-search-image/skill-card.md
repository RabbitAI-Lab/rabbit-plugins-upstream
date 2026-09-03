## Description:

Image search tool: queries Pixabay image API by keywords and returns image URLs and metadata for references, backgrounds, and design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and content creators use this skill to search for image references, backgrounds, and design assets by keyword and receive image URLs with metadata for downstream agent workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image search terms are sent through dLazy services rather than directly to Pixabay.

Mitigation: Avoid submitting confidential or sensitive search terms unless the user accepts dLazy service handling.

Risk: The dLazy API key may be stored in the local CLI configuration.

Mitigation: Protect the local config file and rotate or revoke the organization API key if it may have been exposed.

Risk: The --save option can download assets to a local path.

Mitigation: Use --save only with paths intentionally chosen by the user.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-image)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [JSON containing image result URLs and metadata; optional downloaded asset files when --save is used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports image type, orientation, page, per-page count, language, dry-run, asynchronous execution, timeout, and save-path options.]

## Skill Version(s):

1.3.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
