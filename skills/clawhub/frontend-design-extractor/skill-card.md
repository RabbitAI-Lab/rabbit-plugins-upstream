## Description: <br>
Extract reusable UI/UX design systems from frontend codebases: design tokens, global styles, components, interaction patterns, and page templates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xsir0](https://clawhub.ai/user/xsir0) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to extract frontend UI/UX foundations, component catalogs, page templates, accessibility notes, and migration plans from existing codebases or to define a reusable design foundation for a new project. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill references helper scripts that are not included in the release, so an agent might find similarly named project-local scripts. <br>
Mitigation: Inspect any project-local scripts before execution and run them only when the user explicitly intends that behavior. <br>
Risk: UI refactor mode could affect product behavior if implementation changes drift beyond UI/UX concerns. <br>
Mitigation: Require an accepted phased plan and review diffs to confirm business logic, routing, and APIs remain unchanged. <br>


## Reference(s): <br>
- [Frontend Design Extractor on ClawHub](https://clawhub.ai/xsir0/skills/frontend-design-extractor) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown documentation with optional shell commands and code changes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are normally written under a dedicated ui-ux-spec folder when documenting a frontend design system.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
