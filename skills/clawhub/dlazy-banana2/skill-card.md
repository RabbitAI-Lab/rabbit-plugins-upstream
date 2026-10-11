## Description:

Guides agents in generating and editing images with Nano Banana 2.0 from text prompts and reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide an agent in generating or editing images from prompts and optional reference images through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local images may be sent to dLazy's hosted service, and generated files are hosted on dLazy storage.

Mitigation: Share only content you are comfortable uploading to dLazy; avoid private local files unless their upload is intended.

Risk: The CLI can save an API key in local configuration.

Mitigation: Protect the local credential and use a per-invocation API key when persistent storage is not desired.

Risk: Installing a third-party CLI runs external software on the local machine.

Mitigation: Review the pinned npm package and its listed source before use; prefer on-demand npx when a persistent global install is unnecessary.

## Reference(s):

- [dLazy CLI source (listed in skill metadata; not verified import provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI results may include hosted image URLs or an asynchronous task identifier.]

## Skill Version(s):

1.3.26 (source: ClawHub release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
