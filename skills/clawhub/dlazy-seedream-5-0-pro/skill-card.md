## Description:

Professional tier of Seedream 5.0, stronger on fine detail, typography and complex composition, suited to commercial key visuals and demanding brand assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creative production teams use this skill to generate commercial-grade images from text prompts, with optional reference images, through the dLazy Seedream 5.0 Pro CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on trusted third-party dLazy CLI code and hosted API services.

Mitigation: Prefer npx for one-off use if a global binary is not desired, review the linked source or package before installation, and use the pinned @dlazy/cli version declared by the skill.

Risk: Prompts, parameters, and referenced local media files are sent to dLazy API and media storage for generation.

Mitigation: Provide only intended media and prompts, avoid sensitive files unless the user has approved dLazy processing, and use dry-run behavior when reviewing request payloads.

Risk: A compromised dLazy API key could allow unwanted use of the user's dLazy organization account.

Mitigation: Authenticate only on trusted machines and rotate or revoke the API key from the dLazy dashboard if the CLI or environment may be compromised.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-pro)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces image-generation guidance and dLazy CLI invocations; successful CLI calls return JSON containing generated image URLs, and asynchronous calls may return a task identifier for polling.]

## Skill Version(s):

1.2.10 (source: ClawHub release metadata; artifact frontmatter is 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
