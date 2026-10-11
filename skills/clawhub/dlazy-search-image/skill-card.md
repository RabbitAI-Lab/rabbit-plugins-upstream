## Description:

Helps agents search for image URLs and metadata by keyword using the dLazy image-search service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, developers, and other agents use this skill to find reference images, backgrounds, and design assets from keyword searches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search prompts and parameters are sent to dLazy services rather than directly to Pixabay.

Mitigation: Avoid sensitive searches and confirm dLazy service use is acceptable before invoking the skill.

Risk: Provided local media paths may cause files to be uploaded to dLazy storage.

Mitigation: Do not pass sensitive local files; review inputs before submission.

Risk: The CLI may save an API key locally, and its global installation executes a third-party package.

Mitigation: Prefer per-invocation API keys or review local key storage, and review @dlazy/cli@1.2.3 before global installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-search-image)
- [dLazy CLI package (listed in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (listed in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown instructions and shell commands; the CLI returns JSON search results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results may include image URLs and metadata; optional local download.]

## Skill Version(s):

1.3.28 (source: server-resolved ClawHub release; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
