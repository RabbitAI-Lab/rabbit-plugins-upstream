## Description: <br>
设计门控与创意打磨 - 融合Superpowers HARD-GATE与Anthropic idea-refine的发散能力. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and product teams use this skill to explore feature ideas, clarify success criteria, evaluate alternatives, and require explicit design approval before implementation. It is especially suited to ambiguous product or coding requests that need a structured brainstorming and assumption-checking workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation phrases such as design, idea, and creativity may trigger the workflow during ordinary coding requests. <br>
Mitigation: Review the trigger list before installation and invoke or skip the skill explicitly when the request does not need design approval. <br>
Risk: The workflow may create or update design record files in the project. <br>
Mitigation: Review proposed file paths and content before accepting changes, especially .superpowers/design-approval.md and record.md. <br>
Risk: The hard design gate can slow very small implementation tasks if applied too broadly. <br>
Mitigation: Use the documented skip conditions for pure queries, existing-design bug fixes, and user-approved direct implementation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/brainstorming) <br>
- [Publisher profile](https://clawhub.ai/user/paudyyin) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Files] <br>
**Output Format:** [Markdown design notes, approval records, and conversational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update .superpowers/design-approval.md and record.md as part of the documented workflow.] <br>

## Skill Version(s): <br>
2.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
