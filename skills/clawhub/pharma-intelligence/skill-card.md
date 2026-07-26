## Description: <br>
Provides source-prioritized pharmaceutical and biomedical research workflows for drug approvals, clinical trials, regulatory submissions, competitive intelligence, patents, target discovery, literature review, and bioactivity analysis across major global markets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sciminer](https://clawhub.ai/user/sciminer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, employees, and developers use this skill to gather and synthesize source-grounded pharmaceutical intelligence for approvals, trials, safety, pipeline, patent, target-discovery, repurposing, and literature-review questions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Helper scripts can make broadly scoped outbound HTTP requests and may save fetched data to caller-chosen local file paths. <br>
Mitigation: Run the skill in a sandboxed environment, review generated commands before execution, avoid untrusted JSON inputs, and use raw-output file options only when necessary. <br>
Risk: Pharmaceutical research outputs can be incomplete or misleading if upstream sources are blocked, stale, or interpreted without source priority. <br>
Mitigation: Prefer official regulatory and registry sources, cite source tier and access date, and flag unresolved conflicts or absence of records instead of treating missing data as negative evidence. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/sciminer/skills/pharma-intelligence) <br>
- [Sub-Skills Quick Reference](artifact/references/sub-skills.md) <br>
- [Sources by Region](artifact/references/sources-by-region.md) <br>
- [Drug Naming Conventions by Region](artifact/references/drug-naming.md) <br>
- [Regulatory Timelines by Agency](artifact/references/regulatory-timelines.md) <br>
- [Pharma Intelligence Workflow](artifact/references/pharma-intelligence-workflow.md) <br>
- [GEO Within Entrez](artifact/skills/ncbi-entrez-skill/references/geo.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summaries, tables, command examples, and compact JSON summaries when requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save raw API responses to local files only when explicitly requested.] <br>

## Skill Version(s): <br>
1.0.3 (source: release evidence and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
