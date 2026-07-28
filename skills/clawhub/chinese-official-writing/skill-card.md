## Description: <br>
Drafts, rewrites, compresses, and reviews Chinese official documents and formal work materials, including requests, reports, notices, plans, meeting minutes, institutional rules, procurement notices, feasibility materials, and AI-compute service documents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and external users use this skill to prepare, revise, condense, and review Chinese official documents and formal workplace materials while checking document type, administrative relationship, required handling elements, tone, formatting, and unsupported facts. It is intended for Chinese formal work writing, not English writing, literary writing, marketing copy, social media posts, academic papers, personal job materials, or batch corpus generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Document review or rewriting may require the agent to read drafts that contain sensitive operational, legal, financial, procurement, audit, or personnel information. <br>
Mitigation: Only provide drafts and supporting materials that are appropriate for the agent environment, and keep final legal, financial, procurement, audit, and signing conclusions under responsible human review. <br>
Risk: Formal documents can become misleading if the agent fills missing facts, dates, amounts, approvals, contacts, official numbers, seals, or conclusions that were not supplied by the user. <br>
Mitigation: Use the skill's fact-bound drafting rules, review missing or unsupported elements before release, and confirm all official facts and signing details against authoritative source material. <br>
Risk: The local prose lint helper reports language, format, and repetition risks but does not decide document type, administrative relationship, or handling-element completeness on its own. <br>
Mitigation: Treat lint output as a review aid and apply the relevant genre, handling-element, and final-review references before accepting changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing) <br>
- [README](README.md) <br>
- [Skill instructions](SKILL.md) <br>
- [Information Selection](references/information-selection.md) <br>
- [Task Route Cards](references/task-route-cards.md) <br>
- [Writing Workflow](references/workflow.md) <br>
- [Document Type Routing](references/genre-routing.md) <br>
- [Handling Elements](references/handling-elements.md) <br>
- [Argument Chains](references/argument-chains.md) <br>
- [Official Style](references/official-style.md) <br>
- [Anti-AI Expression Checks](references/anti-ai-patterns.md) <br>
- [Final Review Layers](references/final-review-layers.md) <br>
- [Proofreading Checklist](references/proofreading-checklist.md) <br>
- [Review Checklist](references/review-checklist.md) <br>
- [GB/T 9704-2012 Format Reference](references/format-gbt9704.md) <br>
- [AI Compute and Technical Service Materials](references/ai-compute-docs.md) <br>
- [Formal Addressing](references/formal-addressing.md) <br>
- [External Research Guidance](references/external-research.md) <br>
- [Genre Playbooks](references/genre-playbooks.md) <br>
- [Genre Checklist](references/genre-checklist.md) <br>
- [Report Checklist](references/genre-checklist-report.md) <br>
- [Request Checklist](references/genre-checklist-request.md) <br>
- [Correspondence Playbook](references/genre-playbook-correspondence.md) <br>
- [Institutional Rules Playbook](references/genre-playbook-institution-rules.md) <br>
- [Meeting Minutes Playbook](references/genre-playbook-minutes.md) <br>
- [Request Playbook](references/genre-playbook-request.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Shell commands] <br>
**Output Format:** [Plain text or Markdown, with optional shell commands for the local prose lint helper] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include drafted formal Chinese text, revised text, issue locations, risk levels, editing suggestions, document-structure checks, or prose-lint command examples.] <br>

## Skill Version(s): <br>
1.5.27 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
