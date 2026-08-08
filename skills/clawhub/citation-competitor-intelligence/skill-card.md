## Description: <br>
Discover hidden competitors through academic citation network analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tianzhiceng297-boop](https://clawhub.ai/user/tianzhiceng297-boop) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External analysts, investors, and strategy teams use this skill to research deep-tech startups, university spin-offs, professor-founded companies, and academic commercialization by tracing backward and forward citation networks. It produces structured competitor intelligence that connects papers, researchers, patents, companies, funding, products, timelines, and threat levels. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can lead an agent to research people, companies, patents, funding, and products across public or commercial databases. <br>
Mitigation: Use it only for legitimate business research and follow the terms, privacy rules, and access limits of each external data provider. <br>
Risk: Competitor intelligence claims may be incomplete, stale, or misleading when citation, patent, company, funding, or product evidence is not independently checked. <br>
Mitigation: Verify important claims against primary sources and keep confidence levels visible in the final report. <br>


## Reference(s): <br>
- [Detailed Workflow](references/workflow.md) <br>
- [Checklists and Scoring Rules](references/checklists.md) <br>
- [Real Case: Spot-Size Converter](examples/real-case-spot-size-converter.md) <br>
- [Semantic Scholar Graph API references endpoint](https://api.semanticscholar.org/graph/v1/paper/{paper_id}/references) <br>
- [Semantic Scholar Graph API citations endpoint](https://api.semanticscholar.org/graph/v1/paper/{paper_id}/citations) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown competitor intelligence report with tables, timelines, matrices, and risk assessment] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include anchor summaries, citation graph summaries, per-competitor profiles, commercialization levels, threat scores, and follow-up recommendations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter and changelog report 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
