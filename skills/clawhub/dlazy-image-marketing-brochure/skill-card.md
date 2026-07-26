## Description: <br>
Guides agents through a layout-first marketing brochure workflow that gathers requirements, drafts layouts, waits for confirmation, and uses the dLazy CLI to generate brochure mock-ups. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Designers, marketers, and agents use this skill to plan brochure content, create confirmed brochure layouts, and generate folded and lifestyle mock-ups through the dLazy cloud image-generation service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and attached reference files are sent to dLazy cloud endpoints for generation. <br>
Mitigation: Review prompts and attachments before generation and avoid sending material that should not be processed by the dLazy service. <br>
Risk: The workflow stores or uses a dLazy API key for CLI authentication. <br>
Mitigation: Use the documented dLazy login or environment-variable flow, keep the local configuration file protected, and rotate or revoke keys from the dLazy dashboard when needed. <br>
Risk: Some workflow instructions are in Chinese, which can make prompt or layout confirmation harder for non-Chinese readers. <br>
Mitigation: Confirm each prompt, layout, and mock-up step in a language the reviewer understands before allowing generation. <br>


## Reference(s): <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-marketing-brochure) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated image URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires dLazy CLI authentication and explicit user confirmation before image-generation commands.] <br>

## Skill Version(s): <br>
1.3.6 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
