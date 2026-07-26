## Description: <br>
Turns product photos, product details, or ecommerce listing links into polished product demo, showcase, or ad video workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, creators, ecommerce operators, and agents use this skill to route product-video requests through the dLazy CLI for product demos, shopping ads, and cross-border ecommerce videos. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and attached product files may be sent to dLazy hosted services for processing. <br>
Mitigation: Review product data before upload and avoid sending confidential or restricted files unless the user's dLazy account and service terms allow it. <br>
Risk: The dLazy CLI may store an organization-scoped API key in local user configuration. <br>
Mitigation: Use npx for non-persistent execution when appropriate, protect the local config file, and rotate or revoke the API key from dLazy if exposure is suspected. <br>
Risk: Generated product videos or ad concepts may contain inaccurate or non-compliant product claims. <br>
Mitigation: Review generated outputs against product specifications, advertising rules, and brand requirements before publication. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-product-video) <br>
- [dLazy CLI homepage](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy service homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and CLI guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference project-scoped dLazy chat sessions, attached product files, and hosted product-video generation results.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
