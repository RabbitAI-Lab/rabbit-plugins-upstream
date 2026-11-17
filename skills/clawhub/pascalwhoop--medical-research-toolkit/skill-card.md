## Description:

Query 14+ biomedical databases through a unified MCP endpoint for drug repurposing, target discovery, clinical trials, literature research, genetic associations, and compound bioactivity analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pascalwhoop](https://clawhub.ai/user/pascalwhoop)

### License/Terms of Use:

MIT

## Use Case:

Biomedical researchers and developers use this skill to query public and credentialed biomedical databases, assemble evidence for drug repurposing or target discovery, review literature and clinical trials, and draft research workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive biomedical queries, patient-identifying details, or private research plans could be sent to a third-party MCP service.

Mitigation: Do not submit patient-identifying information or private research plans; review the service's logging, caching, and retention practices before use.

Risk: Credentialed sources such as OMIM may require API keys that could be routed through the production proxy.

Mitigation: Avoid sending real OMIM or OpenFDA keys through the proxy unless the service is trusted; prefer a pinned isolated local install or direct official APIs for credentialed sources.

Risk: Drug, trial, safety, and diagnosis-related outputs could be misused as clinical advice.

Mitigation: Treat outputs as research support only and validate findings with primary sources and qualified clinical review before clinical or patient-facing use.

Risk: Some database workflows and examples are not fully tested and the artifact notes known ID-format issues.

Mitigation: Test intended workflows end to end, verify database identifier formats, and confirm returned evidence against source databases before relying on results.

## Reference(s):

- [PubMed & PubTator3 Guide](./references/pubmed.md)
- [ClinicalTrials.gov Guide](./references/clinical-trials.md)
- [ChEMBL Guide](./references/chembl.md)
- [OpenTargets Platform Guide](./references/opentargets.md)
- [OpenFDA Guide](./references/openfda.md)
- [OMIM Guide](./references/omim.md)
- [Additional Biomedical Databases](./references/other-apis.md)
- [Drug Repurposing Workflow](./scripts/drug-repurposing-workflow.md)
- [Production MCP Endpoint](https://mcp.cloud.curiloo.com/tools/unified/mcp)
- [OMIM API](https://omim.org/api)
- [OpenFDA API](https://open.fda.gov)
- [NCI Clinical Trials API](https://clinicaltrialsapi.cancer.gov)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, API calls, Configuration]

**Output Format:** [Markdown with JSON-RPC examples and inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include database query recipes, workflow steps, API-key notes, and research synthesis guidance.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
