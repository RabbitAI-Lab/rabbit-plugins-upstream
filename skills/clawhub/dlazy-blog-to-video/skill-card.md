## Description:

Converts blog posts or documents into narrated videos by invoking dLazy's hosted file-to-video workflow for storyboard, voiceover, and video build.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn blog posts, articles, or uploaded documents into narrated videos for social, YouTube, training, or report-style delivery. It delegates generation to the dLazy CLI and hosted file-to-video service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The advertised blog-to-video purpose does not match the broader file/document-to-video workflow the skill invokes.

Mitigation: Review prompts and attached content before use, and treat the release as a general dLazy file/document-to-video integration.

Risk: Files attached with the CLI may be uploaded to dLazy media storage.

Mitigation: Attach only files intended for upload to dLazy and avoid sending confidential or regulated data unless approved for that service.

Risk: The skill requires a dLazy API key for hosted service access.

Mitigation: Use a revocable, limited dLazy API key and rotate or revoke it from the dLazy organization dashboard when needed.

Risk: The skill depends on executing the dLazy CLI through npm or npx.

Mitigation: Prefer the pinned npx invocation or another isolated execution method over a persistent global install when possible.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-blog-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI command examples and streamed dLazy agent responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference generated video workflow status, project identifiers, and follow-up commands from the dLazy CLI.]

## Skill Version(s):

1.0.14 (source: server release metadata; artifact frontmatter reports 1.0.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
