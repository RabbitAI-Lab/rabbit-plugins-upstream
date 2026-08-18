## Description:

Marketing Video creates marketing, promotional, advertising, and ecommerce shopping videos from a product, brand, brief, or product listing for social media and campaign use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and marketing teams use this skill to start or continue dLazy projects that generate ecommerce and campaign videos from product information, storefront listings, briefs, and optional reference files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and files passed with --files are sent to dLazy services.

Mitigation: Avoid sending sensitive or restricted material unless the user accepts dLazy processing; use fresh projects or --clear for sensitive work.

Risk: API keys and project session state can persist in the local dLazy CLI configuration.

Mitigation: Use DLAZY_API_KEY or npx for less persistent operation, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill depends on a third-party dLazy account, hosted service, network access, and available credits.

Mitigation: Install and run it only when the user is comfortable using dLazy; surface authentication or insufficient-balance errors with the relevant dLazy dashboard action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-marketing-video)
- [dLazy homepage](https://github.com/dlazyai/cli)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and CLI output from the dLazy service]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference generated video assets, uploaded input files, dLazy project ids, and streamed service responses.]

## Skill Version(s):

1.0.5 (source: server release metadata; artifact frontmatter shows 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
