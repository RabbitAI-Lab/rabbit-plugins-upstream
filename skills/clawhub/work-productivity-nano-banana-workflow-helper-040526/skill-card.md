## Description: <br>
Builds practical AI image generation and editing workflows with prompt packs, reference planning, retry rules, and visual QA. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Designers, marketers, agent users, and skill authors use this skill to turn image goals into prompt packs, reference plans, QA checklists, and bounded retry or deployment checklists for image generation and editing workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger wording may activate the skill for loosely related image or workflow requests. <br>
Mitigation: Invoke the skill explicitly when precision matters, or disable implicit invocation in environments with strict routing requirements. <br>
Risk: Generated prompt and workflow guidance can miss model limits, visual defects, brand constraints, or licensing concerns. <br>
Mitigation: Review outputs with the skill's visual QA checklist and keep safety, brand, and export checks before handoff. <br>
Risk: Unbounded retries can increase cost, wait time, and failed-output loops. <br>
Mitigation: Set maximum attempts, stop conditions, fallback tools, and acceptance criteria before running image iterations. <br>


## Reference(s): <br>
- [Nano Banana Image Workflow Helper](https://clawhub.ai/kyro-ma/skills/work-productivity-nano-banana-workflow-helper-040526) <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [Nano Banana Pro demand signal](https://clawhub.ai/skills/nano-banana-pro) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown with prompt packs, QA checklists, retry plans, and deployment or configuration checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance; no executable code or sensitive access.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
