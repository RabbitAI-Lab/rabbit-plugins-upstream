## Description:

Uses product, supply capability, historical transaction, order, inquiry, quote, lost-deal, and customer-distribution evidence to decide which countries, regions, industries, and application scenarios should be prioritized for testing, active development, or deferral without generating bulk customer lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zaynpeng](https://clawhub.ai/user/zaynpeng)

### License/Terms of Use:

MIT-0

## Use Case:

Business development, sales, and market strategy teams use this skill to rank target markets and scenarios against real commercial evidence, internal supply constraints, and validation needs. It helps separate confirmed facts, supported judgments, open questions, and AI assumptions before recommending active development, test first, or do not enter.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may inspect commercially sensitive sales, order, inquiry, quote, lost-deal, and customer-distribution evidence.

Mitigation: Run it only in workspaces containing data the agent is authorized to inspect.

Risk: Market recommendations can be misleading when based only on macro market size, incomplete parameters, or unsupported assumptions.

Mitigation: Require product or service, candidate regions, analysis goal, supply and delivery capability, and supporting business evidence before making priority recommendations; otherwise return gaps and validation actions.

## Reference(s):


## Skill Output:

**Output Type(s):** [analysis, markdown, guidance]

**Output Format:** [Markdown report with parameter status, evidence summary, market recommendations, fit assessment, risks, priorities, validation actions, sources, and open questions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a report field structure referenced by the skill; server security evidence reports no install-time code, persistence, or hidden privileges.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
