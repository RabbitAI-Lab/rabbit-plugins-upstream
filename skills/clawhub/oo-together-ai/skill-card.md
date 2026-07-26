## Description: <br>
Together AI helps agents work with Together AI through an OOMOL-connected account for chat completions, embeddings, and model discovery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to operate Together AI from an agent session through an OOMOL-connected account. It supports non-streaming chat completions, embedding generation, and model discovery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and requested inputs may be sent to Together AI and may incur Together AI or OOMOL costs. <br>
Mitigation: Review the intended payload and cost impact before approving write-tagged actions. <br>
Risk: Chat completion and embedding actions are write-tagged and can create provider-side activity. <br>
Mitigation: Confirm the exact action, schema-derived payload, and expected effect before execution. <br>


## Reference(s): <br>
- [Together AI homepage](https://www.together.ai) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-together-ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Actions may return JSON data with execution metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
