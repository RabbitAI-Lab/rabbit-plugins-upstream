## Description:

Turns a website or URL into a promo, social ad, or product demo video by using the dLazy website-to-video workflow to capture the site, derive brand elements, storyboard, add voiceover, build, and validate a Remotion template.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and marketing teams use this skill when they have a URL or landing page and want an agent to generate a promo, social ad, or product demo video through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: URLs, prompts, and attached files are sent to dLazy services.

Mitigation: Use the skill only for explicit website-to-video tasks where sending that data to dLazy is acceptable.

Risk: A dLazy API key may be stored in ~/.dlazy/config.json, and security evidence reports that inspected CLI code did not enforce the promised private file permissions.

Mitigation: Prefer DLAZY_API_KEY per invocation when possible, verify local config permissions after login, and rotate or revoke exposed keys.

Risk: The workflow depends on third-party npm/npx CLI execution and hosted dLazy API endpoints.

Mitigation: Use the pinned @dlazy/cli version declared by the release and review the dependency before installing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-website-to-video)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May request or reference dLazy project ids, API-key setup, and uploaded file URLs through the dLazy CLI.]

## Skill Version(s):

1.3.8 (source: server release evidence; artifact frontmatter states 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
