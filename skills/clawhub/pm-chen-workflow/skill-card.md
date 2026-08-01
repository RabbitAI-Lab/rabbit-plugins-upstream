## Description: <br>
pm-chen guides product teams through a Chinese-first workflow that turns natural-language feature requests into business architecture diagrams, interactive HTML prototypes, PRD documents, API specifications, review gates, and development handoff packages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chenxi102](https://clawhub.ai/user/chenxi102) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Product managers, founders, and developers use this skill to convert product ideas into reviewed architecture, prototype, PRD, API, and handoff artifacts. It is intended for product design and development handoff workflows where each stage should be confirmed before downstream artifacts are produced. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate on broad product design, prototype, PRD, architecture, API specification, or development handoff requests. <br>
Mitigation: Confirm the user's intent and scope before starting the workflow, and use the built-in review gates before moving between stages. <br>
Risk: The skill may create or update collaborative documents through connected Feishu or Tencent Docs tooling when available. <br>
Mitigation: Confirm the target document platform and review generated document links and access settings before sharing the handoff package. <br>
Risk: Generated handoff artifacts can introduce inconsistencies between architecture, prototype, PRD, and API definitions. <br>
Mitigation: Apply the bundled review checklist and require user confirmation at each stage before downstream artifacts are finalized. <br>


## Reference(s): <br>
- [PRD template](references/prd-template.md) <br>
- [API specification template](references/api-spec-template.md) <br>
- [Review checklist](references/review-checklist.md) <br>
- [ClawHub skill page](https://clawhub.ai/chenxi102/skills/pm-chen-workflow) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Chinese-first conversational guidance, inline SVG diagrams, self-contained HTML prototypes, Markdown documents, and structured API specifications] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update Feishu or Tencent Docs when those integrations are available; otherwise it falls back to workspace Markdown files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
