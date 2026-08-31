## Description:

Creates promo, social ad, and product demo videos from website URLs by capturing the site, deriving brand context, storyboarding, adding voiceover, building, and validating output on a Remotion template.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn a website URL into a promotional, social advertising, or product demonstration video through dLazy's hosted website-to-video template.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, website URLs, and files attached with --files are sent to dLazy's hosted service.

Mitigation: Use only URLs and files approved for upload to dLazy; avoid sensitive local files unless that transfer is intended.

Risk: The skill requires a dLazy API key stored in local CLI configuration or supplied through DLAZY_API_KEY.

Mitigation: Authenticate only on trusted machines and rotate or revoke the dLazy API key if exposure is suspected.

Risk: A global npm installation persists the dLazy CLI on the system.

Mitigation: Use the pinned npx invocation when a non-persistent CLI run is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-website-to-video)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and terminal-oriented text with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke dLazy SaaS via the pinned @dlazy/cli package and may upload user-selected files when --files is used.]

## Skill Version(s):

1.3.10 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
