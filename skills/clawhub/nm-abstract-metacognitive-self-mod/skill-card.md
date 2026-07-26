## Description: <br>
Analyze and improve the improvement process for skill changes by detecting regressions, assessing improvement effectiveness, and generating meta-optimization recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill after batches of skill improvements, regressions, or periodic reviews to analyze what improvement strategies worked and what should change in future improvement workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local trace and improvement-memory records may include project names, file paths, tool targets, decisions, outcomes, and rationales. <br>
Mitigation: Review the stored files under ~/.claude/skills/traces and improvement_memory.json, limit use on sensitive workflows, and periodically clear local records when retention is not needed. <br>
Risk: Meta-optimization recommendations could steer future skill-improvement behavior incorrectly if based on sparse or noisy history. <br>
Mitigation: Treat recommendations as proposals, require user approval before changing improvement strategy, and validate changes against recent outcomes before relying on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-abstract-metacognitive-self-mod) <br>
- [OpenClaw metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/abstract) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration] <br>
**Output Format:** [Markdown report with recommendations and optional local JSON insight or trace records] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Proposes changes for user approval; does not auto-apply modifications to the improvement process.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
