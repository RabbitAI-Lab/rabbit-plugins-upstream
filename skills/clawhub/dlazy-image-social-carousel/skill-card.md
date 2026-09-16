## Description:

A structured workflow skill dedicated to social-media carousel design. The core method is 'decide intent first, then execute,' using a 'single-confirmation + cover-first' two-phase flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and design agents use this skill to plan and produce social-media carousel image sets through a confirmed direction, cover-first generation, and matched remaining slides.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on installing and running the external dLazy CLI, which handles prompts, selected media files, and API credentials.

Mitigation: Install only after reviewing the dLazy CLI package and source, prefer npx or a local install over global installation, and avoid passing sensitive local files as media inputs.

Risk: The security summary flags a version-documentation mismatch for review before use.

Mitigation: Verify the intended @dlazy/cli package version and release metadata before deployment.

Risk: Generated prompts and selected media are processed through dLazy services.

Mitigation: Use only content approved for cloud processing and rotate or revoke the dLazy API key if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-social-carousel)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown text with confirmation tables, prompt drafts, CLI commands, and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user confirmation before generation steps; image results are returned as hosted URLs.]

## Skill Version(s):

1.3.17 (source: server release metadata; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
