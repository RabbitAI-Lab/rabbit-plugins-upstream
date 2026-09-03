## Description:

URL to video, link to video, webpage to video, and landing page to video: paste a URL to turn a page into a promo, ad, or demo video with capture, brand derivation, storyboard, voiceover, and build steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and content teams use this skill to give an agent a URL and generate a promo, social ad, or product demo video through dLazy's URL-to-video workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, target URLs, and explicitly attached files are sent to dLazy for video generation.

Mitigation: Use the skill only for URLs and files that may be shared with dLazy, and avoid sensitive or confidential inputs.

Risk: A persistent global CLI install leaves the dLazy CLI available on the system after the task.

Mitigation: Use the pinned npx invocation when a temporary execution path is preferred.

Risk: Attached local files are uploaded to dLazy media storage before they are referenced by the hosted workflow.

Mitigation: Review attachments before use and include only files needed for the requested video.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-url-to-video)
- [ClawHub publisher profile](https://clawhub.ai/user/dlazyai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides an agent to use the pinned dLazy CLI flow and may reference project ids for follow-up turns.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
