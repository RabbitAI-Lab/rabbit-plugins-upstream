## Description:

Converts PDFs and other documents into explainer, courseware, report, or training videos by using the dLazy CLI to parse, outline, storyboard, voice over, build, and validate the video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, educators, and business users use this skill to turn uploaded PDFs and related documents into narrated explainer, report, courseware, or training videos through the dLazy hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached documents may be sent to dLazy's hosted API and media storage.

Mitigation: Avoid uploading confidential documents unless the user's organization permits third-party processing.

Risk: The dLazy API key may be stored in a local CLI configuration file.

Mitigation: Use normal credential hygiene, restrict local config file access, and rotate or revoke the key from the dLazy dashboard when needed.

Risk: A global CLI install persists a third-party executable on the user's system.

Mitigation: Use the pinned npx invocation when a non-persistent install is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-pdf-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Invokes a pinned dLazy CLI that may stream hosted-agent responses and upload attached files to dLazy storage.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
