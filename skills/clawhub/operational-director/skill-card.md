## Description: <br>
Operational Director is a Russian-language assistant that summarizes a local test/mock business snapshot covering accounts, balances, payments, taxes, documents, liquidity, risks, and suggested actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vladbigbrain](https://clawhub.ai/user/vladbigbrain) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Business leaders and operations staff use this skill to get read-only management summaries and focused answers about a company's local demo/test snapshot, including finances, obligations, documents, and operational risks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may mistake the financial summary for live bank or real-company data. <br>
Mitigation: Present the output as demo/test information and avoid using it for real banking, tax, or liquidity decisions. <br>
Risk: A stale, partial, or unavailable local snapshot could lead to incomplete operational guidance. <br>
Mitigation: Use the snapshot date and completeness fields, disclose unavailable data, and do not infer missing facts. <br>


## Reference(s): <br>
- [Operational Director on ClawHub](https://clawhub.ai/vladbigbrain/skills/operational-director) <br>
- [Local business snapshot documentation](artifact/assets/get_data.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Guidance] <br>
**Output Format:** [Russian-language Markdown responses and compact JSON snapshots] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only; uses bundled local test/mock data and does not perform banking operations or mutate data.] <br>

## Skill Version(s): <br>
1.3.0 (source: server release and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
