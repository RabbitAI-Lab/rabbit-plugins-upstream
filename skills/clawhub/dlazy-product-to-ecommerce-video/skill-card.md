## Description: <br>
Turns product specifications, manuals, catalogs, or Amazon, Shopify, eBay, and Temu listings into conversion-focused ecommerce videos with multi-language voiceover and an optional virtual host. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, marketers, and ecommerce operators use this skill to drive the dLazy hosted product-to-video workflow from an agent or terminal. It is intended for producing product ads and cross-border selling videos from product links or supplied product materials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses dLazy's hosted service and stores a dLazy API key locally for authenticated CLI calls. <br>
Mitigation: Use the documented dLazy login or auth flow, keep the local config file limited to the current OS user, and rotate or revoke the API key from the dLazy dashboard when needed. <br>
Risk: Files attached with the CLI are uploaded to dLazy-managed storage before being referenced by the hosted agent. <br>
Mitigation: Attach only files that are appropriate to send to the dLazy service and review sensitive product materials before upload. <br>
Risk: A global CLI install persists the package on the user's system. <br>
Mitigation: Use the pinned npx command for one-off use when a persistent global install is not desired. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-product-to-ecommerce-video) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [npm package: @dlazy/cli](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>
- [ClawHub publisher profile: dlazyai](https://clawhub.ai/user/dlazyai) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Text] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the pinned @dlazy/cli 1.2.3 package and requires a dLazy API key; attached files are uploaded to dLazy-managed storage by the CLI.] <br>

## Skill Version(s): <br>
1.3.4 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
