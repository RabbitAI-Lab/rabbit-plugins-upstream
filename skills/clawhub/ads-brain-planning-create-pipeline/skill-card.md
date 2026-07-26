## Description: <br>
Defines an ad campaign planning state machine that normalizes business intent, applies creation gates, drafts a launch plan, and delegates validated campaign configuration generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lizejia668-code](https://clawhub.ai/user/lizejia668-code) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Ad planning agents use this skill to handle new campaign creation requests, separate unsupported or optimization scenarios, and produce a concise launch plan before campaign configuration is generated. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can prepare actionable campaign structures even though it does not execute ad creation itself. <br>
Mitigation: Connect it only to systems that require user confirmation before creating or launching ads. <br>
Risk: Planning outputs can be incomplete or unsuitable when eligibility checks, schema validation, or required context are unavailable. <br>
Mitigation: Use the skill's warnings and gate outcomes to withhold create_campaign output until validation succeeds. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lizejia668-code/skills/ads-brain-planning-create-pipeline) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown and structured JSON-like campaign planning outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a natural-language plan, launch_plan_draft, create_campaign when validation passes, warnings, and next_action.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
