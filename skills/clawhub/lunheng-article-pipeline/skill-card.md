## Description:

A Chinese long-form writing pipeline for academic papers, business commentary, industry analysis, and in-depth public articles, with staged research, drafting, review, audit, and final inspection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to coordinate Chinese long-form writing projects that need evidence gathering, multi-role drafting, audit gates, and human approval before final delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security evidence flags inconsistent tool-boundary instructions and recommends review before installation.

Mitigation: Install only in a host or profile that mechanically denies exec, process, browser, apply_patch, and sensitive memory or session tools unless those capabilities are intentionally granted.

Risk: The workflow can create many project files, spawn subagents, use web search or fetch, and send prompts to external providers when optional features are enabled.

Mitigation: Use the Phase 0 consent gates, keep work in the project-scoped run/<project name>/ directory, and opt out of external or provider-backed features for sensitive content.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zuoyunlai/skills/lunheng-article-pipeline)
- [Quickstart Guide](QUICKSTART.md)
- [Pipeline Overview](references/pipeline-readme.md)
- [Permissions and Tool Boundaries](references/permissions.md)
- [Deliverables](references/deliverables.md)
- [M-Gate Algorithm](references/_shared/M-Gate-Algorithm.md)
- [Chinese AI Trace Checker](references/checkers/中文AI痕迹-checker.md)
- [Coordinator Role Card](references/agents/00-主控-coordinator.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown documents and structured project files, with optional SVG or Markdown templates and status reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes project artifacts under run/<project name>/ and may spawn subagents, use web retrieval, or call opt-in providers after Phase 0 consent.]

## Skill Version(s):

2.11.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
