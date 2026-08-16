## Description:

估算实验和科研数据集所需资源、周期与成本。适用于：估算实验或训练数据集构建所需的人力、样本、试剂、设备、算力、采购和交付成本，用于预算规划与报价复核。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and biomedical data teams use this skill to estimate resources, timelines, compliance posture, and cost ranges for experiment or training dataset construction. It supports budget planning and quotation review for target-driven drug-discovery dataset projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PatSnap and Eureka MCP usage may expose regulated, licensed, or contract-bound biomedical data workflows.

Mitigation: Confirm user authorization and contractual rights before querying PatSnap data or generating Office reports.

Risk: Patent SAR and commercial-use compliance estimates may be incomplete or unsuitable as final legal conclusions.

Mitigation: Route commercial patent, SAR, ZINC, and licensing outputs through legal review before product or customer use.

Risk: ADMET and dataset-size outputs are estimates and may be misleading if treated as experimental validation.

Mitigation: Present ADMET predictions and cost ranges as planning estimates and validate critical assumptions with domain experts or experiments.

## Reference(s):

- [Compliance Rules](artifact/references/compliance_rules.md)
- [Cost Benchmarks](artifact/references/cost_benchmarks.md)
- [Database Coverage](artifact/references/database_coverage.md)
- [Field Schema](artifact/references/field_schema.md)
- [MCP Tool Routing](artifact/references/mcp_tool_routing.md)
- [ChEMBL](https://www.ebi.ac.uk/chembl/)
- [ChEMBL API](https://www.ebi.ac.uk/chembl/api/data/)
- [BindingDB](https://www.bindingdb.org/)
- [PubChem](https://pubchem.ncbi.nlm.nih.gov/)
- [RCSB PDB](https://www.rcsb.org/)
- [ZINC22](https://zinc22.docking.org/)
- [DrugBank](https://go.drugbank.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance plus structured JSON, CSV, and Word report outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces cost summaries, compliance matrices, data inventories, and dataset scheme reports named with the task slug.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
