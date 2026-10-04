## Description:

Helps creators plan, script, and generate cinematic or narrative storyboards with approval checkpoints before rendering images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Filmmakers, advertisers, educators, and other creators use this skill to turn a brief into character references, shot-by-shot scripts, and storyboard images, confirming each stage before proceeding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The networked dLazy CLI sends prompts and parameters to its cloud API and uploads referenced media files.

Mitigation: Use only media intended for upload and review prompts and file paths before generating images.

Risk: Installing the third-party CLI or retaining an API key adds supply-chain and credential exposure.

Mitigation: Review the CLI before installation; consider the on-demand npx option and a per-session DLAZY_API_KEY instead of persistent setup.

## Reference(s):

- [dLazy CLI source (linked in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Markdown, Image URLs, Shell commands, Guidance]

**Output Format:** [Markdown shot lists and visual prompts, with generated image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires confirmation at planning, character, script, and image-delivery stages; specifies an A4 landscape storyboard layout for print or PDF export.]

## Skill Version(s):

1.3.26 (source: server-resolved release; skill frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
