## Description:

Conducts a value-based pricing study for a product or service, from its website and knowledge base to a ratified price list.

This skill is ready for commercial/non-commercial use.

## Publisher:

[c-kapsalis](https://clawhub.ai/user/c-kapsalis)

### License/Terms of Use:

MIT-0

## Use Case:

Product owners and pricing teams use the skill to compare market reference prices, cost-to-serve floors, and customer value, then develop pricing packages and a real-buyer validation plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The self-test can erase existing files at its destination.

Mitigation: Run it in an isolated disposable destination and confirm safeguards prevent overwriting existing study files.

Risk: The crawler may reach unintended network destinations.

Mitigation: Restrict crawler access to approved public sites and review the allowed targets before crawling.

Risk: Personal or confidential study fields may be included in Claude batch inputs.

Mitigation: Use trusted study files and remove personal or confidential fields before submitting batches.

Risk: Batch processing and real survey outreach can incur costs or contact buyers.

Mitigation: Approve batch costs and real survey outreach separately, and review pricing recommendations before applying them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/c-kapsalis/skills/value-pricing)
- [Server-resolved GitHub source](https://github.com/C-Kapsalis/value-pricing/tree/main/skills/value-pricing)
- [Literature and methods](artifact/references/literature.md)
- [Study output contract](artifact/references/output-contract.md)
- [Real-buyer validation and hand-over](artifact/references/8-validation.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, CSV, JSON, YAML, Python code, Shell commands]

**Output Format:** [A pricing-study workspace with configuration files, phase summaries, data tables, and Markdown reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs document assumptions and evidence, compare market, cost, and value estimates, and present pricing proposals with validation criteria. Estimates remain hypotheses until real buyers confirm them.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
