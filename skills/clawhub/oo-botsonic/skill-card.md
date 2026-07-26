## Description: <br>
Botsonic lets agents use an OOMOL-connected Botsonic account to generate responses and read conversations and FAQs through the oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to let an agent work with an OOMOL-connected Botsonic account for response generation, conversation lookup, conversation listing, and FAQ listing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose Botsonic conversations and FAQs from the connected account. <br>
Mitigation: Use the skill only for explicit Botsonic tasks and treat returned conversations and FAQs as sensitive account data. <br>
Risk: The skill depends on the OOMOL oo CLI and server-side Botsonic connection. <br>
Mitigation: Install only if you trust OOMOL, and review CLI install, login, or connection steps before running them. <br>


## Reference(s): <br>
- [Botsonic homepage](https://botsonic.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-botsonic) <br>
- [OOMOL ClawHub profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live oo connector schemas before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
