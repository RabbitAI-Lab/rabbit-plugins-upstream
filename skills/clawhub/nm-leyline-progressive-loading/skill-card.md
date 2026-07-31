## Description: <br>
Implements hub-and-spoke lazy loading to minimize token usage in large skills. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill authors use this skill to design modular, lazily loaded agent skills that select workflow-specific guidance only when context and token budget call for it. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation terms may cause the skill to appear in conversations where progressive-loading guidance is not needed. <br>
Mitigation: Prefer explicit invocation or tighten triggers in environments that auto-select skills aggressively. <br>
Risk: The skill provides documentation and examples that could be applied incorrectly to a consuming skill architecture. <br>
Mitigation: Review selected module boundaries, token budgets, and loading paths before adopting the guidance in a production skill. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-leyline-progressive-loading) <br>
- [metadata.clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with examples, checklists, shell commands, code snippets, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces advisory patterns for progressive-loading skill design; it does not execute commands or handle credentials.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
