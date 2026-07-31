## Description: <br>
Shapes agent behavior via instruction framing and style transfer. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent authors use this skill to frame instructions, dispatch review agents, and transfer style from exemplars when writing prompts, skills, code, or documentation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate for some general instruction-writing or review-prompt tasks. <br>
Mitigation: Use it when instruction framing, style transfer, or multi-agent review framing is relevant, and ignore it for simple factual context-packing tasks. <br>
Risk: Style-transfer prompts may place exemplar code or prose into the agent context. <br>
Mitigation: Only include exemplar material that is appropriate to share in the agent context. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-imbue-latent-space-engineering) <br>
- [Claude Night Market imbue plugin](https://github.com/athola/claude-night-market/tree/master/plugins/imbue) <br>
- [Publisher profile](https://clawhub.ai/user/athola) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Text] <br>
**Output Format:** [Markdown guidance with prompt patterns and examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Markdown-only prompt-writing aid; no executable commands, credential access, persistence, or data-moving behavior found.] <br>

## Skill Version(s): <br>
1.9.17 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
