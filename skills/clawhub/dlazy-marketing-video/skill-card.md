## Description:

Creates marketing, promotional, advertising, or brand videos from a product, brand, or brief for social media and campaign use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, and commerce operators use this skill to start or continue dLazy projects that generate conversion-focused product and marketing videos from listings, product materials, brands, or briefs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to dLazy hosted services.

Mitigation: Use only prompts and files appropriate for dLazy processing; start a new project for unrelated work and continue a project ID only when prior context should be reused.

Risk: The CLI stores an API key in a local config unless DLAZY_API_KEY is used.

Mitigation: Use the environment variable option for per-run credentials when local persistence is undesirable, and rotate or revoke keys from dLazy when needed.

Risk: Installing the wrapper requires trusting dLazy and the pinned @dlazy/cli npm package.

Mitigation: Install only if you trust dLazy; review the pinned package or source before use and prefer npx for one-off execution when avoiding a global install.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-marketing-video)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with CLI command examples and streamed text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a pinned dLazy CLI template, can continue project-scoped sessions, and can reference uploaded local files.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact frontmatter reports 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
