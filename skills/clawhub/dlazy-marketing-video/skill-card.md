## Description: <br>
Creates marketing, promotional, advertising, and ecommerce product videos from a product, brand, listing, or brief through the dLazy hosted service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to start or continue dLazy product-to-ecommerce-video projects that turn product details, storefront listings, briefs, and optional reference files into marketing videos for social, ecommerce, or campaign use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, product details, and attached files may be sent to dLazy's hosted API and file storage. <br>
Mitigation: Use the skill only with data appropriate for the dLazy service, avoid confidential attachments unless approved, and review service terms before use. <br>
Risk: API keys are required and may be stored in the local dLazy CLI config. <br>
Mitigation: Prefer per-invocation credentials when needed, protect the local config, and rotate or revoke organization-scoped keys from the dLazy dashboard if exposure is suspected. <br>
Risk: Continuing the wrong project id may send prompts into an unintended existing project session. <br>
Mitigation: List and verify project ids before continuing prior work, and clear or compact sessions when needed. <br>
Risk: A global CLI install persists the dLazy binary on the machine. <br>
Mitigation: Use the pinned npx command for on-demand execution when a persistent global install is not desired. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-marketing-video) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and streamed CLI text from the hosted service.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference generated video project state and uploaded-file URLs managed by the dLazy service.] <br>

## Skill Version(s): <br>
1.0.2 (source: SKILL.md frontmatter and server release evidence, created 2026-07-21T02:25:12Z) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
