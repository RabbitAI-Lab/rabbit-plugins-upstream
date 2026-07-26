## Description: <br>
Design an evaluation plan for an LLM or AI feature before shipping it, including task definition, datasets, metrics, rubrics, baselines, human and automated evaluation, a pass bar, and a regression gate. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, product teams, and AI feature owners use this skill to turn a prompt, model, or agent quality goal into a repeatable evaluation plan before shipping. It helps define datasets, failure modes, metrics, rubrics, baselines, human or LLM judging, and CI regression gates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Evaluation planning may involve examples, logs, labelled cases, or failure modes that contain sensitive production data. <br>
Mitigation: Use sanitized or approved evaluation examples unless sensitive data is intentionally part of the evaluation design. <br>
Risk: A poorly calibrated LLM judge or vague rubric can produce misleading ship or no-ship decisions. <br>
Mitigation: Calibrate LLM-judge results against human labels on a representative sample and require explicit rubric anchors before using the plan as a release gate. <br>
Risk: An evaluation set that includes only happy-path examples can miss edge-case, adversarial, safety, or regression failures. <br>
Mitigation: Include adversarial and edge-case coverage, deterministic checks where possible, and a numeric regression threshold in CI. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mohitagw15856/skills/ai-eval-plan) <br>
- [Skill homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/ai-eval-plan.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown evaluation plan with checklists and rubric guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces planning guidance only; it does not execute code, access external systems, or request credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
