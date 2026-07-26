## Description: <br>
Use when you need to parse or audit a FigJam User Story Map (Jeff Patton methodology) into LLM-readable Markdown or JSON - after a Story Mapping workshop, before publishing a Story Map template, or when feeding a Story Map to a coding agent. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[monikazapisekstudio](https://clawhub.ai/user/monikazapisekstudio) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, product managers, UX practitioners, and workshop facilitators use this skill to audit FigJam story maps for LLM-readiness and convert validated boards into structured Markdown or JSON backlog artifacts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill or parser reads the selected FigJam board, which may contain confidential workshop, product, or roadmap content. <br>
Mitigation: Use it only on boards your organization permits, and avoid confidential boards unless that use is approved. <br>
Risk: Live API parsing requires a Figma token. <br>
Mitigation: Use a minimally scoped token where possible, keep it in an environment variable or secret store, and do not paste it into shared files or screenshots. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/monikazapisekstudio/skills/figjam-storymap-llm) <br>
- [Published FigJam Template](https://www.figma.com/community/file/1661156551667594442) <br>
- [LLM-ready FigJam Guidelines](references/llm-ready-figjam-guidelines.md) <br>
- [FigJam Template Spec](references/figjam-template-spec.md) <br>
- [FigJam Executive Summary](references/figjam-executive-summary.md) <br>
- [System Prompt](references/system-prompt.md) <br>
- [Figma REST API Documentation](https://www.figma.com/developers/api) <br>
- [Jeff Patton User Story Mapping](https://www.jpattonassociates.com/user-story-mapping/) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown reports and structured JSON, with optional shell commands for running the parser] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Parser output is typically story-map.md or story-map.json; audit mode produces an LLM-readiness report with concrete fix recommendations.] <br>

## Skill Version(s): <br>
0.1.3 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
