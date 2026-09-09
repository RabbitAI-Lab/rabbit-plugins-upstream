## Description:

Creates marketing, promotional, advertising, and ecommerce product videos from a product, brand, listing, or brief for social media and campaign use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, ecommerce operators, and agents use this skill to create conversion-oriented marketing or product videos from product details, storefront listings, catalogs, manuals, or brand briefs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running a third-party CLI can expose the environment to package or source-code risk.

Mitigation: Review the dLazy CLI source or npm package before installing, and prefer npx or an isolated non-privileged environment when avoiding a persistent global binary.

Risk: Prompts, selected files, API credentials, and project history are handled by the dLazy service.

Mitigation: Attach only files intended for upload, avoid sensitive content where possible, and rotate or revoke the dLazy API key when needed.

Risk: Project-scoped chat history can retain prior context across follow-up requests.

Mitigation: Use the documented clear or compact controls when project context should be reset or reduced.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-marketing-video)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Files]

**Output Format:** [Markdown or terminal text with dLazy CLI commands and generated marketing video outputs or links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require a dLazy API key and may upload selected local files through the dLazy CLI.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter says 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
