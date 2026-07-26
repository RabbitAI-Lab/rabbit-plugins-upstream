## Description: <br>
Ai Pm Workbench is a Chinese-language AI product management workbench that helps agents produce strategy, product, architecture, evaluation, safety, pricing, and governance guidance for AI products. <br>

This skill is for research and development only. <br>

## Publisher: <br>
[yinjianheng](https://clawhub.ai/user/yinjianheng) <br>

### License/Terms of Use: <br>
Personal Use Only <br>


## Use Case: <br>
AI product managers, product teams, and AI builders use this skill to structure AI product strategy, model selection, RAG and agent design, prompt engineering, evaluation, safety, commercialization, and governance work. It provides reusable guidance, checklists, templates, and case material for Chinese-language AI PM workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill has broad AI product management triggers and may activate for many AI PM-related requests. <br>
Mitigation: Constrain routing or activation to requests that explicitly need AI product management methods, templates, or planning support. <br>
Risk: The skill asks agents to append author, legal, disclaimer, and reminder text to responses. <br>
Mitigation: Review response policy expectations before deployment and adjust router or system-level behavior if repeated legal text is not appropriate for the host agent. <br>
Risk: Customer-service and agent examples may be adapted to workflows involving user data or state-changing actions. <br>
Mitigation: Apply user notice, data minimization, redaction, retention limits, and human approval for refunds, account changes, messaging, or other state-changing actions. <br>
Risk: The workbench provides reference guidance rather than professional advice. <br>
Mitigation: Require independent review of key product, legal, safety, and technical decisions before using outputs in business or production settings. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yinjianheng/skills/ai-pm-workbench) <br>
- [README](README.md) <br>
- [AI product manager deep methodology](references/methodologies/ai-pm-deep-methods.md) <br>
- [AI customer service product example](references/examples/ai-customer-service-example.md) <br>
- [AI customer service agent case](examples/ai-customer-service-agent-case.md) <br>
- [Agent system design template](references/templates/agent-design-template.md) <br>
- [AI product evaluation template](references/templates/ai-evaluation-template.md) <br>
- [AI safety template](references/templates/ai-safety-template.md) <br>
- [RAG architecture design template](references/templates/rag-design-template.md) <br>
- [Prompt engineering template](references/templates/prompt-engineering-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown guidance, templates, checklists, matrices, examples, and structured product planning documents] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Chinese-language responses; the source skill asks agents to append author, legal, disclaimer, and usage reminder text.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
