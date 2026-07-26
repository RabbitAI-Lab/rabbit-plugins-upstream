## Description: <br>
Creates production-grade PRDs for web, mobile, and full-stack projects, including traceable requirements and an execution-ready implementation task breakdown. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anjasta-tarigan](https://clawhub.ai/user/anjasta-tarigan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Product managers, founders, and engineering teams use this skill to turn product ideas or feature requests into a structured PRD and implementation task list for a coding agent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated PRD and task files may contain private product, customer, or business context. <br>
Mitigation: Review generated files before sharing and add `.project/` to `.gitignore` when the content should not enter public repository history. <br>
Risk: Task breakdowns may be handed to a coding agent before product intent and acceptance criteria are reviewed. <br>
Mitigation: Review the generated PRD and task Markdown files before using them as implementation instructions. <br>


## Reference(s): <br>
- [PRD Creator ClawHub page](https://clawhub.ai/anjasta-tarigan/skills/prd-creator) <br>
- [PRD Master Template](references/prd-master-template.md) <br>
- [Requirement Writing Standards](references/requirement-writing-standards.md) <br>
- [Task Breakdown Guide](references/task-breakdown-guide.md) <br>
- [ISO/IEC/IEEE 29148:2018](https://standards.ieee.org/standard/29148-2018.html) <br>
- [IEEE 830-1998](https://ieeexplore.ieee.org/document/720574) <br>
- [Amazon Working Backwards PR/FAQ](https://workingbackwards.com/resources/working-backwards-pr-faq/) <br>
- [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) <br>
- [EARS Requirements Syntax](https://alistairmavin.com/ears/) <br>
- [INVEST User Stories](https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/) <br>
- [MoSCoW Prioritisation](https://www.agilebusiness.org/dsdm-project-framework/moscow-prioritisation.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown files containing PRDs, requirements, acceptance criteria, and implementation task breakdowns] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates PRD and task documents under .project/prd/ after user clarification.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
