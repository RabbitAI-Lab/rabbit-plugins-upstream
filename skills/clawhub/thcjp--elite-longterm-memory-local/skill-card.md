## Description: <br>
Elite Longterm Memory Local helps agents keep durable local memories across sessions using LanceDB vectors, Ollama embeddings, and local files without external API keys. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to add privacy-focused, single-user long-term memory, semantic recall, and local memory maintenance to agents. It is most relevant when durable local context is desired and retention practices can be reviewed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Durable local memory can retain conversation details longer than users expect. <br>
Mitigation: Avoid storing secrets, credentials, regulated data, or sensitive personal and business details unless strict retention and review practices are configured. <br>
Risk: The artifact includes a callback_url input despite privacy-first claims. <br>
Mitigation: Leave callback_url unused unless the destination and transmitted data are explicitly understood and approved. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/elite-longterm-memory-local) <br>
- [Publisher Profile](https://clawhub.ai/user/thcjp) <br>
- [Skill Homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration values] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local memory files and vector storage when the agent follows the skill workflow.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
