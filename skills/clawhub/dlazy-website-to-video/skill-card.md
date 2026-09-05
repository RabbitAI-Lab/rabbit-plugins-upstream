## Description:

website to video, url to video, landing page to video, link to ad, web promo video: capture the site, derive brand, storyboard, voiceover, build, and validate on a Remotion template for promo, social ad, or product demo requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and content teams use this skill to turn a website or landing-page URL into a promotional video, social ad, or product demo through the dLazy hosted website-to-video workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, URLs, selected project context, and attached files may be sent to dLazy's hosted API and media storage.

Mitigation: Use only data intended for upload to dLazy, and avoid attaching private or sensitive files unless that upload is approved.

Risk: A dLazy API key may be stored locally for future CLI use or supplied through an environment variable.

Mitigation: Protect the local CLI config and environment, and rotate or revoke the key from the dLazy dashboard if exposure is suspected.

Risk: A global npm install persists the dLazy CLI binary on the system.

Mitigation: Use the pinned npx command when a non-persistent invocation is preferred.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-website-to-video)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include project-scoped commands for starting or continuing dLazy website-to-video sessions.]

## Skill Version(s):

1.3.12 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
