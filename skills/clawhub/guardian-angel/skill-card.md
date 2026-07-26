## Description: <br>
Guardian Angel gives AI agents a virtue-based moral conscience grounded in Thomistic ethics and a plugin enforcement layer for evaluating, blocking, or escalating tool actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leo3linbeck](https://clawhub.ai/user/leo3linbeck) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use Guardian Angel to add an ethics and security gate that evaluates tool calls, detects risky provenance or high-stakes actions, and requests explicit approval when needed. It is intended for environments where the operator explicitly wants Thomistic/Catholic ethics to influence agent behavior. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can take broad control over tool execution by blocking or escalating agent actions. <br>
Mitigation: Review the plugin configuration before deployment, keep exempt and always-block lists intentional, and do not rely on this plugin as the only control against destructive commands or malicious plugins. <br>
Risk: Pending approval records may temporarily contain sensitive tool parameters. <br>
Mitigation: Keep approval windows and pending timeouts short, store approval data in a private location, and avoid approving actions from shared transcripts. <br>
Risk: The skill intentionally applies a Thomistic/Catholic ethics framework that can influence agent choices. <br>
Mitigation: Install it only when that ethical posture is desired by the operator and disclose that posture to affected users where appropriate. <br>


## Reference(s): <br>
- [Guardian Angel Skill Page](https://clawhub.ai/leo3linbeck/skills/guardian-angel) <br>
- [Guardian Angel Plugin Specification](PLUGIN-SPEC.md) <br>
- [Moral Credit Scoring Rubric](references/rubric.md) <br>
- [Thomistic Framework for Moral Evaluation](references/thomistic-framework.md) <br>
- [Virtue Ethics Reference](references/virtue-ethics.md) <br>
- [Prompt Injection Defense Reference](references/prompt-injection-defense.md) <br>
- [Affected Parties Rubric](references/affected-parties-rubric.md) <br>
- [High-Scrutiny Domains](references/domains.md) <br>
- [Principle of Double Effect](references/double-effect.md) <br>
- [Pattern Triggers Reference](references/pattern-triggers.md) <br>
- [Reversibility and Commitment Rubric](references/reversibility-commitment-rubric.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance, JSON configuration, and structured approval or escalation messages] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May block or pause tool execution pending explicit approval when configured as an enforcement plugin] <br>

## Skill Version(s): <br>
3.1.2 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
