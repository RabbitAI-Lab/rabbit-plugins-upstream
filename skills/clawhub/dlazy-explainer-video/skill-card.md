## Description:

Turns a document, topic, or brief into a narrated explainer video through outlining, storyboarding, voiceover, building, and validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and teams use this skill to turn documents or briefs into narrated explainer, courseware, or training videos using the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and user-selected attachments are sent to the third-party dLazy service.

Mitigation: Review content and files before sending; avoid sharing sensitive material without authorization.

Risk: Installing the third-party CLI and saving an API key may expose credentials or introduce supply-chain risk.

Mitigation: Review the pinned @dlazy/cli package before installation; use a revocable key or DLAZY_API_KEY to avoid storing a key locally.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-explainer-video)
- [dLazy CLI repository (listed in skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Plain text or Markdown with CLI commands and project updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The agent guides video creation through dLazy; the service handles the generated media.]

## Skill Version(s):

1.0.21 (source: server-resolved ClawHub release; artifact frontmatter says 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
