## Description: <br>
A professional product image generation skill for Amazon product detail pages, covering main images, secondary images, and A+ modules. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, marketplace operators, and ecommerce designers use this skill to plan and generate Amazon product image suites. It guides the agent through main-image baselining, secondary image selection, A+ module planning, and one-at-a-time image generation via the dLazy CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Use of the third-party dLazy CLI may send prompts and supplied local media to dLazy services. <br>
Mitigation: Install only if the user accepts dLazy hosted processing, and avoid sending sensitive product data or media unless approved for that service. <br>
Risk: The CLI may store or use a dLazy API key on the local system. <br>
Mitigation: Prefer npx or the DLAZY_API_KEY environment variable for temporary use, and rotate or revoke keys from the dLazy dashboard when no longer needed. <br>
Risk: Some runtime instructions and disclosures are Chinese-only metadata. <br>
Mitigation: Review the Chinese instructions before use, especially command execution and API-key handling guidance. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-amazon-product-image-suite) <br>
- [dLazy CLI repository](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated image URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires dLazy CLI authentication and user confirmation before each generation command.] <br>

## Skill Version(s): <br>
1.3.6 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
