## Description:

Cognitive immune system for AI agents. Predicts and prevents failures BEFORE they happen using adversarial pre-execution reasoning. Zero dependencies, zero cost, universal quality improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jcools1977](https://clawhub.ai/user/jcools1977)

### License/Terms of Use:


## Use Case:

Developers, engineers, and agent users use this skill to add a pre-action failure-prediction checklist before significant responses, code changes, plans, and shared-system actions. It is intended to improve alignment, completeness, confidence calibration, and risk awareness without external tools or services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can broadly influence an agent's reasoning style through always-loaded silent pre-action checks.

Mitigation: Disable automatic activation where supported when minimal behavioral changes are preferred.

Risk: The skill's value depends on the agent applying the premortem checklist proportionally rather than delaying or overcomplicating simple tasks.

Mitigation: Apply the documented intensity scaling and anti-paralysis guard, and review high-stakes outputs before use.

## Reference(s):

- [Premortem Effectiveness: Expected Impact Areas](references/benchmarks.md)
- [The Science Behind Premortem](references/cognitive-science.md)
- [ClawHub Skill Page](https://clawhub.ai/jcools1977/skills/premortem)
- [Project Homepage](https://github.com/jcools1977/Opengnaw)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text guidance produced by the agent after applying an internal premortem reasoning pass]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No external services, API calls, network access, file writes, or persistent runtime state are required by the skill.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
