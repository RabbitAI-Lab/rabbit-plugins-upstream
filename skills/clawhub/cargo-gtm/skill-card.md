## Description: <br>
Front door for any GTM task on Cargo - sourcing, waterfall enrichment, email/phone/LinkedIn lookup, email verification, scoring, qualification, sequencing, CRM sync, and signal monitoring (job changes, funding, tech-stack/hiring intent). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cargo-ai](https://clawhub.ai/user/cargo-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
GTM, RevOps, sales, and growth teams use this skill to plan and execute prospecting, enrichment, verification, scoring, outreach, CRM sync, and signal-monitoring workflows in Cargo. It guides agents through task-specific docs, recipes, provider playbooks, cost controls, and quality checks before running paid or sensitive actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can process prospect, customer, and contact data through many third-party enrichment, LLM, web-search, scraping, CRM, sequencer, and LinkedIn integrations. <br>
Mitigation: Minimize fields sent to providers, confirm lawful basis and internal policy approval, and treat signed URLs and downloaded outputs as sensitive data. <br>
Risk: CRM, sequencer, LinkedIn, recurring workflow, visitor identification, phone lookup, reverse lookup, and personality analysis actions can have privacy or operational impact. <br>
Mitigation: Require explicit user confirmation before these actions and keep the skill's pilot, approval, receipt, and cost-cap gates in place. <br>
Risk: The security evidence flags the release for review because privacy and confirmation guardrails are not consistent across all workflows. <br>
Mitigation: Review the skill before deployment and scan any local changes, especially provider playbooks and recipes that execute paid or data-writing actions. <br>


## Reference(s): <br>
- [Cargo GTM Skill on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-gtm) <br>
- [Cargo Skills Homepage](https://github.com/getcargohq/cargo-skills) <br>
- [Finding companies and contacts](guides/finding-companies-and-contacts.md) <br>
- [Enriching and researching](guides/enriching-and-researching.md) <br>
- [Writing outreach](guides/writing-outreach.md) <br>
- [Cost discipline](references/cost-discipline.md) <br>
- [Contact accuracy](references/contact-accuracy.md) <br>
- [Output retrieval](references/output-retrieval.md) <br>
- [Stage action map](references/stage-action-map.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline JSON and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct agents to create or retrieve structured Cargo workflow outputs, CSV/JSON downloads, CRM updates, sequencer handoffs, or recurring plays after user approval.] <br>

## Skill Version(s): <br>
1.9.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
