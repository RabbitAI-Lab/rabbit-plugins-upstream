## Description: <br>
跨会议知识库 builds a searchable meeting knowledge base from Tencent Meeting summaries or local notes by extracting decisions, conclusions, action items, and risks across meetings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[golgys0621](https://clawhub.ai/user/golgys0621) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Teams and agents use this skill to consolidate meeting records into a reusable knowledge base for follow-up, weekly reports, retrospectives, interview preparation, training, and cross-meeting decision lookup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can aggregate sensitive meeting records into a persistent knowledge-base index when prompts are broad. <br>
Mitigation: Before use, limit the meeting date range, topics, participants, or local folder and review the generated knowledge-base file before sharing or retaining it. <br>
Risk: Generated indexes may contain internal decisions, action items, risks, and names. <br>
Mitigation: Apply the same access controls and retention rules used for the source meeting records. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/golgys0621/skills/meeting-kb-skill) <br>
- [README](README.md) <br>
- [Knowledge base template](references/kb_template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown knowledge-base files, JSON query results, and natural-language guidance with optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Indexes .md/.txt meeting notes, groups items by decision, conclusion, action item, and risk, and includes source meeting and section references.] <br>

## Skill Version(s): <br>
3.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
