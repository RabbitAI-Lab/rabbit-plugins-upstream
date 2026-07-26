## Description: <br>
Guides structured co-authoring of substantial documents through context alignment, section drafting, reader testing, and final checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yangchao228](https://clawhub.ai/user/yangchao228) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external collaborators, and developers use this skill to co-author proposals, PRDs, technical specs, decision records, RFCs, and similar long-form documents. It helps turn raw context or drafts into structured sections, reader-tested revisions, and final readiness checks while keeping the user responsible for factual and strategic approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Substantial documents may include sensitive business, product, or stakeholder context provided by the user. <br>
Mitigation: Provide only the context needed for the document and avoid pasting sensitive material unless it is appropriate for the agent environment, especially when independent review tools or subagents are enabled. <br>
Risk: Generated drafts or reviews could make unsupported assertions or hide unresolved assumptions in polished prose. <br>
Mitigation: Keep assumptions and open questions explicit, require user approval for facts and strategy, and run reader-readiness checks before treating the document as final. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yangchao228/skills/doc-coauthoring) <br>
- [Project homepage](https://github.com/yangchao228/my_open_skills/tree/main/skills/work/doc-coauthoring) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown responses with compact YAML handoff blocks, questions, review notes, and section drafts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Maintains a compact doc_state handoff and separates must-fix, should-improve, and optional review notes when reviewing documents.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
