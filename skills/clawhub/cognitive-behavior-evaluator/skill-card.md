## Description: <br>
Run standardized, safety-oriented behavioral evaluations of a target AI agent by relaying controlled diagnostic probes, scoring responses on anchored rubrics with cited evidence, and running bounded self-correction only for failures. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fretelli](https://clawhub.ai/user/fretelli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, evaluators, and safety reviewers use this skill to stress-test AI agents or prompts for authority-pressure resistance, false-premise grounding, and anti-stereotyping behavior. It produces a contained diagnostic report with scores, cited evidence, behavioral analysis, and remediation guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill intentionally sends adversarial diagnostic prompts to a target agent. <br>
Mitigation: Use it only in controlled safety evaluation contexts and avoid invoking it for unrelated audits or benchmarks. <br>
Risk: A failing target may produce harmful, fabricated, or biased content during evaluation. <br>
Mitigation: Report only short, non-reconstructable evidence spans and describe failures without redistributing harmful artifacts. <br>
Risk: Single-run evaluations can misrepresent stochastic model behavior. <br>
Mitigation: Run each probe at least three times in fresh contexts and report the distribution rather than a single draw. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fretelli/skills/cognitive-behavior-evaluator) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/fretelli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, analysis, guidance] <br>
**Output Format:** [Markdown diagnostic report with rubric scores, cited response evidence, behavioral analysis, containment note, and remediation guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Single-probe mode reports one scored dimension out of 5; full-battery mode reports three dimensions out of 15 and recommends at least three fresh-context runs per probe.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
