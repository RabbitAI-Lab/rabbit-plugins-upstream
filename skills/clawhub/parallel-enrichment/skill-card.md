## Description: <br>
Parallel Enrichment uses the Parallel API to add web-sourced fields, such as CEO names, funding, and contact info, to CSV files or inline company, people, and product records. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[normallygaussian](https://clawhub.ai/user/normallygaussian) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and business teams use this skill to enrich CSV files or inline records with web-sourced company, people, product, lead, funding, and contact fields through the Parallel CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Input CSV or JSON data may contain personal, customer, lead, regulated, or confidential business information that should not be shared with Parallel. <br>
Mitigation: Use the skill only with data you are permitted to share with Parallel, and avoid previewing, storing in shared temporary paths, or handing enriched outputs to another agent when rows contain sensitive data. <br>
Risk: Installing or running an untrusted Parallel CLI source could expose data or credentials. <br>
Mitigation: Install parallel-cli only from Parallel's official source and stop if installation or authentication cannot be verified. <br>


## Reference(s): <br>
- [Parallel Homepage](https://parallel.ai) <br>
- [Parallel CLI Integration Docs](https://docs.parallel.ai/integrations/cli) <br>
- [Parallel API Docs](https://docs.parallel.ai) <br>
- [Parallel Enrichment API Reference](https://docs.parallel.ai/api-reference/enrichment) <br>
- [ClawHub Skill Page](https://clawhub.ai/normallygaussian/skills/parallel-enrichment) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON examples, YAML configuration examples, and CSV output expectations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The Parallel CLI writes enriched CSV files that retain original columns, add requested enrichment columns, and include a _parallel_status column.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
