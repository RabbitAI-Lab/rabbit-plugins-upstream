## Description:

ct-advisor is a clinical-trial lifecycle advisor that answers methodology, design, compliance, QC, and tone questions from its local knowledge pack, routes raw data and competitive-intelligence requests to sibling ct-series skills, and refines answers through an author-hosted Coze endpoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT

## Use Case:

Clinical-trial practitioners, clinicians, nurses, medical students, and supporting agents use this skill to get structured clinical-trial methodology, regulatory, safety, operations, QC, and communication guidance. For live trial, safety, literature, sample-size, or competitive-intelligence needs, it routes to sibling ct-series skills and returns traceable guidance rather than fabricating missing data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Every refined answer is sent off-device to the author-hosted Coze endpoint with a bundled shared credential and a stable hashed machine identifier.

Mitigation: Install and use only after organizational review of that data flow; do not submit confidential protocols, unpublished sponsor strategy, patient or subject information, regulated internal documents, passwords, API keys, or other restricted clinical data.

Risk: The security summary flags weak scoping for sensitive clinical content in outbound answer payloads.

Mitigation: Treat auto-redaction as a supporting control, not a guarantee; keep sensitive or regulated content out of prompts unless the organization has approved this remote refinement path.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/medstatstar/skills/ct-advisor)
- [Project homepage](https://github.com/medstatstar/ct-advisor)
- [README](README.md)
- [Knowledge reference index](knowledge/reference-index.md)
- [Workflow steps](references/steps.md)
- [Author-hosted Coze refinement endpoint](https://ct-advisor.coze.site/run)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with optional code blocks, command snippets, menus, and source labels]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include sibling-skill handoffs for registry, safety, literature, sample-size, or meta-analysis work; each refined answer is sent to the author-hosted Coze endpoint.]

## Skill Version(s):

0.9.39 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
