## Description: <br>
Drafts, rewrites, compresses, and reviews Chinese official documents and formal workplace materials, including requests, reports, notices, plans, meeting minutes, institutional rules, AI-compute materials, and news-style formal texts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, public-sector-adjacent teams, schools, enterprises, and agent users use this skill to draft or review Chinese official documents and formal work materials while checking genre, hierarchy, factual boundaries, formatting, and formal tone. It is not intended for English writing, literary writing, marketing copy, social media posts, academic papers, or personal job applications. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Drafts involving legal, finance, procurement, audit, formal signing, public policy, or time-sensitive facts may be incomplete or require authoritative confirmation. <br>
Mitigation: Treat these outputs as drafts and require human review plus source verification before use. <br>
Risk: Formal-document drafting can introduce unsupported facts, dates, amounts, organizations, policy claims, or approval conclusions if the user has not provided sufficient evidence. <br>
Mitigation: Use the skill's factual-boundary rules and confirm missing or sensitive facts before finalizing the document. <br>
Risk: The optional local prose lint script may flag language, formatting, and repetition issues but does not validate document genre, official authority, or factual accuracy. <br>
Mitigation: Use lint output only as a drafting aid and apply human judgment for official-document structure and substance. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing) <br>
- [README](README.md) <br>
- [Workflow](references/workflow.md) <br>
- [Genre Routing](references/genre-routing.md) <br>
- [Handling Elements](references/handling-elements.md) <br>
- [Final Review Layers](references/final-review-layers.md) <br>
- [GB/T 9704 Format](references/format-gbt9704.md) <br>
- [AI Compute Documents](references/ai-compute-docs.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, code, shell commands] <br>
**Output Format:** [Chinese prose, Markdown when requested, review notes, and optional shell commands for local prose linting] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are draft or review materials that should be human-reviewed for legal, finance, procurement, audit, formal signing, public policy, and time-sensitive facts.] <br>

## Skill Version(s): <br>
1.5.32 (source: server release metadata and skill frontmatter metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
