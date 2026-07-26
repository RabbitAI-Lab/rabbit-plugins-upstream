## Description: <br>
Token Saver Skill provides prompt-level guidance for reducing AI token usage through context compression, response caching, adaptive optimization modes, and token-usage reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, independent builders, and agent users can use this skill to guide long AI sessions toward lower token consumption while preserving recent context, code blocks, errors, and other high-value content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests execution authority even though the evidence describes it as a prompt-only token-saving helper. <br>
Mitigation: Review proposed commands before execution and install it only in agents where exec access is intentionally allowed. <br>
Risk: The skill describes caching and compression of conversation content without clear implementation, limits, or privacy controls. <br>
Mitigation: Avoid sensitive or precision-critical sessions unless the host agent provides explicit controls for cache storage, clearing, and compression behavior. <br>
Risk: Optimization claims may not be enforced because the artifact does not include code that performs safe token optimization. <br>
Mitigation: Treat savings reports and mode changes as guidance unless verified by the host agent's actual token accounting and context-management features. <br>


## Reference(s): <br>
- [Token Saver Skill on ClawHub](https://clawhub.ai/thcjp/skills/token-saver-skill) <br>
- [thcjp ClawHub publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with command-style examples and plain-text status reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prompt-only guidance; host-agent behavior determines whether caching, compression, or commands are actually available.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter lists 1.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
