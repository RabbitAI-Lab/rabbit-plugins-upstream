## Description:

用于回答药物相关问题，面向明确药物、疾病或靶点查询汇总 PatSnap 药物、专利、文献、临床试验和交易信息。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External users and life science analysts use this skill to investigate drugs, targets, indications, clinical results, competitive landscape, pharmacovigilance, and licensing deals through PatSnap life-science MCP services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on PatSnap MCP services and an API key stored in MCP configuration.

Mitigation: Install only when PatSnap service use is intended, protect the API key, and verify MCP connectivity before running research tasks.

Risk: Drug, disease, target, and related research terms are sent to PatSnap services during lookups.

Mitigation: Avoid submitting confidential or restricted research terms unless the deployment environment and PatSnap account terms permit that use.

Risk: Generated clinical or safety analysis may be incomplete or unsuitable for medical decision-making.

Mitigation: Treat outputs as research support and require qualified review before clinical, safety, regulatory, or investment decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yuanzhian-patsnap/skills/pharmaceuticals-exploration-zhcn)
- [PatSnap Open Platform](https://open.patsnap.com)
- [PatSnap Developer Portal](https://open.patsnap.com/devportal)
- [PatSnap Life Sciences](https://eureka.patsnap.com/ls-landing)
- [Pharma Intelligence MCP Service](https://open.patsnap.com/marketplace/mcp-servers/096456)
- [Chemical Molecular MCP Service](https://open.patsnap.com/marketplace/mcp-servers/713886)
- [Biology Modality MCP Service](https://open.patsnap.com/marketplace/mcp-servers/06e741)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with inline setup commands and structured research sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-language pharmaceutical research responses with required MCP connectivity checks before analysis]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
