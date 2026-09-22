## Description:

Website to Video helps an agent turn a supplied URL into a promotional, social ad, or product demo video workflow by capturing the site, deriving brand signals, storyboarding, adding voiceover, building, and validating with a Remotion template.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and marketing operators use this skill to ask a hosted dLazy agent to convert a website URL into a promo video, social ad, or product demo. It is suited for URL-driven video creation tasks that may include uploaded brand or reference assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, options, and files passed with --files are sent to dLazy services.

Mitigation: Use this skill only with content approved for third-party processing, and review dLazy terms before using private website content or brand assets.

Risk: Authentication stores or uses a dLazy API key on the local machine.

Mitigation: Store keys only in the OS-user-restricted CLI config or pass them per invocation with DLAZY_API_KEY, and rotate or revoke exposed keys from the dLazy dashboard.

Risk: The workflow executes a third-party CLI package through npm or npx.

Mitigation: Use the pinned @dlazy/cli@1.2.3 install command or npx form, and review the linked source or npm package before installation in sensitive environments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-website-to-video)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown or terminal text from the dLazy CLI, with inline shell commands when setup or continuation is needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may reference hosted project sessions; attached files are uploaded to dLazy storage before use.]

## Skill Version(s):

1.3.19 (source: server release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
