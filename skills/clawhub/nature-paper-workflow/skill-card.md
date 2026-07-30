## Description: <br>
Nature Paper Workflow 论文生产链 is a top-level academic paper workflow router that identifies a user's manuscript stage and routes the request to the appropriate installed sub-skill without directly executing paper tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardwason](https://clawhub.ai/user/edwardwason) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Researchers, students, and academic writing teams use this skill to orient paper-workflow requests, choose the next phase from literature review through revision, and hand off to specialized sub-skills. It is suited to bilingual Chinese/English manuscript workflows, especially Nature-family or adjacent journal submission workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The router can direct users to other installed sub-skills that may have broader permissions than this skill. <br>
Mitigation: Review each routed sub-skill's permissions and security notes before using stages that download papers, create files, analyze data, or call external services. <br>
Risk: The workflow defaults toward Nature-family journal assumptions when the target venue is not specified. <br>
Mitigation: Specify the target venue or publication context so the agent can choose the appropriate route and adjust recommendations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/edwardwason/skills/nature-paper-workflow) <br>
- [Workflow map](references/workflow-map.md) <br>
- [Skill map](references/skill-map.md) <br>
- [Trigger map](references/trigger-map.md) <br>
- [Sub-skill protocol](references/sub-skill-protocol.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown or plain text routing guidance with phase labels, target sub-skill names, handoff notes, and next-step recommendations.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference local sub-skill names and expected handoff artifacts; the router itself is read-only.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
