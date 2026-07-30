## Description: <br>
Drafts, rewrites, compresses, and reviews Chinese official documents and formal institutional work materials, including requests, reports, notices, plans, meeting minutes, policies, procurement notices, feasibility studies, and AI-compute materials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external contributors, and agent users use this skill to draft, revise, compress, and review Chinese official and formal workplace documents while preserving document genre, reporting relationship, handling elements, factual boundaries, and formal tone. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Official, legal, procurement, finance, audit, and signature-sensitive content may require institution-specific approval or factual verification. <br>
Mitigation: Review those materials manually before use, especially dates, amounts, authorities, formal conclusions, and signing details. <br>
Risk: User-provided documents may contain sensitive institutional information. <br>
Mitigation: Use the skill only in an environment appropriate for the sensitivity of the supplied materials and avoid sharing unnecessary confidential details. <br>
Risk: The included lint script can report prose risks from files passed to it. <br>
Mitigation: Run the lint script only on intended local files and review its findings before applying changes; it does not rewrite files automatically. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing) <br>
- [README](artifact/README.md) <br>
- [Workflow](artifact/references/workflow.md) <br>
- [Genre Routing](artifact/references/genre-routing.md) <br>
- [Handling Elements](artifact/references/handling-elements.md) <br>
- [GB/T 9704 Formatting](artifact/references/format-gbt9704.md) <br>
- [AI Compute and Technical Service Materials](artifact/references/ai-compute-docs.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Plain text or Markdown, depending on the user's requested delivery format] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include review findings, risk notes, or rewritten document drafts; does not automatically rewrite files.] <br>

## Skill Version(s): <br>
1.5.29 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
