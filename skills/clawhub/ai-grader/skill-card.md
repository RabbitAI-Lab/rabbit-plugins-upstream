## Description:

ai-grader is an offline AI evaluation skill that scores AI systems against a 45-dimension work-awareness rubric and generates reports, probe packs, and improvement guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, AI operators, and evaluation teams use this skill to run structured behavior checks on AI assistants or agents, compare results, and produce local score reports for follow-up improvement work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated local reports and stored evaluation records may contain sensitive AI names, transcripts, or business context.

Mitigation: Use de-identified object names and test data, keep generated files private by default, and redact reports before sharing.

Risk: External judge prompts or probe packs can expose raw transcripts if users include unredacted evaluation material.

Mitigation: Redact transcripts before turning them into judge prompts or sending them to any external reviewer or model.

Risk: The optional human-profiling persona workflow can characterize a person rather than only an AI system.

Mitigation: Enable human-profiling only with informed consent from the person being characterized.

## Reference(s):

- [ClawHub ai-grader release](https://clawhub.ai/zhaoxinghua09-cell/skills/ai-grader)
- [AI Evaluation Protocol](references/ai_eval_protocol.md)
- [External Evaluation Loop](references/ai_external_eval.md)
- [Capability Bounds Methodology](references/ai_capability_bounds.md)
- [Domain-Fit Evaluation](references/ai_domain_fit.md)
- [AI Growth Trend](references/ai_growth_trend.md)
- [Improvement Plan Output](references/ai_improvement_plan.md)
- [Persona Resonance](references/ai_persona_resonance.md)
- [Problem Remedy](references/ai_problem_remedy.md)
- [Owner Grading](references/ai_owner_grading.md)
- [Bidirectional Evaluation](references/ai_bidirectional_eval.md)
- [Host Mirror](references/ai_host_mirror.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, HTML, shell commands, guidance]

**Output Format:** [Markdown guidance, JSON records, shell command examples, and local HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline operation; writes local evaluation records and report files when invoked.]

## Skill Version(s):

2.7.0 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
