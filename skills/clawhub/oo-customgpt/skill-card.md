## Description: <br>
CustomGPT.ai helps agents read, create, and update CustomGPT.ai data through the OOMOL connector instead of direct API calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent inspect CustomGPT.ai agents, conversations, documents, and messages, and to create conversations or send non-streaming prompts after confirming write actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create CustomGPT.ai conversations and send messages that change account state. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running write actions. <br>
Risk: The skill depends on OOMOL account access and the oo CLI to operate a CustomGPT.ai account. <br>
Mitigation: Install or authenticate the oo CLI only when the user intends to use this connector and trusts OOMOL for the connection. <br>
Risk: Connector action schemas may change over time. <br>
Mitigation: Inspect the live connector schema before constructing every action payload. <br>


## Reference(s): <br>
- [CustomGPT.ai homepage](https://customgpt.ai) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-customgpt) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection before each action payload.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
