## Description:

Paste a URL and use dLazy's URL-to-video workflow to turn a webpage or landing page into a promo, social ad, or product demo video with capture, brand extraction, storyboard, voiceover, and build steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and marketing teams use this skill to ask an agent to run dLazy's hosted URL-to-video workflow from a supplied webpage link and continue the generated project through follow-up CLI prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: URLs, prompts, and attached files are sent to dLazy's hosted service.

Mitigation: Use the skill only with content that is appropriate to process through dLazy, and avoid attaching sensitive local files unless that handling is acceptable.

Risk: The dLazy API key is stored locally for reuse.

Mitigation: Treat the key as a credential, restrict local file access, and rotate or revoke the key from dLazy if it may have been exposed.

Risk: A global npm install persists the dLazy CLI on the system.

Mitigation: Use the pinned npx invocation or review the CLI package source before choosing a persistent global installation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-url-to-video)
- [dLazy CLI Source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a pinned dLazy CLI invocation and streams responses from a project-scoped hosted service session.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
