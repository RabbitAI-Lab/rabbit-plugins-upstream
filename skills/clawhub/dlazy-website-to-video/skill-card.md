## Description:

Helps turn a website URL into a promotional video, social ad, or product demo using dLazy's hosted website-to-video service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and developers use this skill to request website-based promotional videos, social ads, and product demos and to continue work on existing projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and options are sent to dLazy's hosted API, and attached files are uploaded to dLazy storage.

Mitigation: Review prompts and attachments for sensitive information before submitting them.

Risk: Authentication stores a dLazy API key locally.

Mitigation: Protect local credentials and rotate or revoke the key if it is exposed.

Risk: Using the third-party CLI installs or runs external package code.

Mitigation: Review the linked CLI source or package as required by your organization; use the pinned npx invocation to avoid a persistent global install.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-website-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Text with optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Streams responses from a hosted website-to-video service; work can continue within a project.]

## Skill Version(s):

1.3.31 (source: ClawHub release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
