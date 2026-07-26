## Description: <br>
A Chinese-first workday companion that turns four high-friction moments--starting work, choosing lunch, handling low energy, and planning after work--into concise decisions and next actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[killsnake01](https://clawhub.ai/user/killsnake01) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, students, interns, freelancers, and remote workers use this skill to reduce small workday decision fatigue. It gives short, action-oriented cards for work start, lunch, low-energy moments, and after-work planning, with at most one clarifying question when needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Casual workday phrases may route into this skill on some hosts. <br>
Mitigation: Use explicit invocation or confirm intent when an input could belong to another assistant workflow. <br>
Risk: Bundled Python utilities can validate, render, and package local skill artifacts when run. <br>
Mitigation: Run those scripts only during intentional local validation, rendering, or packaging, and review generated artifacts before publishing. <br>
Risk: Optional search and image-card flows can involve sensitive location, route, meal, work, or mood details. <br>
Mitigation: Keep real names, precise places, routes, and sensitive personal context out of shareable cards unless the user explicitly confirms they should be included. <br>


## Reference(s): <br>
- [Skill listing](https://clawhub.ai/killsnake01/skills/workday-companion) <br>
- [Module contracts](references/module-contracts.md) <br>
- [Baseline intake](templates/baseline-intake.md) <br>
- [Image model adapter](adapters/image-model.md) <br>
- [Public listing pack](references/public-listing-pack.json) <br>
- [ClawHub discovery playbook](references/clawhub-discovery-playbook.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Code, Configuration] <br>
**Output Format:** [Markdown cards, structured text, JSON card data, SVG or HTML card assets, and optional shell commands for local validation or rendering] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Chinese-first short-card responses; optional image-card flows hide real locations, routes, restaurants, and sensitive details unless the user explicitly makes them shareable.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
