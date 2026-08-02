## Description: <br>
Afrexai Knowledge Management helps agents produce knowledge audits, taxonomy plans, documentation templates, contribution workflows, freshness reviews, and handoff plans for organizational knowledge bases. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and team leads use this skill to structure organizational knowledge: auditing documentation coverage, designing knowledge taxonomies, generating runbooks and ADR templates, and planning contribution and freshness workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad read, write, and shell execution authority. <br>
Mitigation: Run it only in a constrained workspace and require explicit approval before file writes or shell commands. <br>
Risk: The skill references API credentials and external callbacks without a precise integration boundary. <br>
Mitigation: Provide least-privilege credentials only for a specific approved integration and require approval before API calls or external callbacks. <br>
Risk: Knowledge-management workflows may involve personal or performance-adjacent employee details. <br>
Mitigation: Use clear consent, retention, and access-control rules, and avoid storing such details unless organizational policy permits it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/afrexai-knowledge-management) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with tables, checklists, templates, and occasional shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include task status, parsed summaries, risk registers, taxonomy outlines, runbooks, ADR templates, and troubleshooting guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter says 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
