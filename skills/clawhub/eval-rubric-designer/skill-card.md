## Description: <br>
Design a scoring rubric and LLM-as-judge prompt to evaluate the quality of an AI feature's output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, product teams, and evaluators use this skill to turn an AI feature brief or sample outputs into a weighted evaluation rubric, anchored scoring guide, parseable LLM-as-judge prompt, labeling guide, and judge reliability notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated rubrics or judge workflows may be used for consequential scoring without enough review or calibration. <br>
Mitigation: Review generated rubrics before use, calibrate against representative good and weak examples, and spot-check judge scores against human labels. <br>
Risk: Confidential examples could be included in generated judge workflows. <br>
Mitigation: Avoid adding confidential examples unless the judge environment is approved for that data. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/mohitagw15856/skills/eval-rubric-designer) <br>
- [Skill Homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/eval-rubric-designer.html) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Guidance] <br>
**Output Format:** [Markdown with a strict JSON output contract embedded in the generated judge prompt] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces weighted rubric dimensions, 1/3/5 anchors, a labeling guide, and judge reliability notes.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
