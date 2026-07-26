## Description: <br>
Query 14+ biomedical databases for drug repurposing, target discovery, clinical trials, and literature research. Access ChEMBL, PubMed, ClinicalTrials.gov, OpenTargets, OpenFDA, OMIM, Reactome, KEGG, UniProt, and more through a unified MCP endpoint. Use when researching disease targets, finding approved/investigational drugs, searching clinical evidence, discovering genetic associations, or analyzing compound bioactivity data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juanbastias](https://clawhub.ai/user/juanbastias) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External researchers, clinicians, bioinformatics teams, and developers use this skill to query biomedical databases for drug repurposing, target discovery, clinical evidence review, literature mining, safety checks, and compound bioactivity analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Hosted biomedical queries can expose patient identifiers, confidential study details, or proprietary drug-discovery terms to the Curiloo MCP service. <br>
Mitigation: Avoid sensitive terms in hosted queries, or run the tool locally for sensitive work. <br>
Risk: Biomedical search results may be incomplete, stale, or unsuitable for direct drug, safety, trial, or target decisions. <br>
Mitigation: Verify results against authoritative sources and qualified professional review before acting on them. <br>


## Reference(s): <br>
- [Medical Research Toolkit on ClawHub](https://clawhub.ai/juanbastias/skills/medical-research-toolkit) <br>
- [Curiloo unified MCP endpoint](https://mcp.cloud.curiloo.com/tools/unified/mcp) <br>
- [OMIM API](https://omim.org/api) <br>
- [OpenFDA](https://open.fda.gov) <br>
- [NCI Clinical Trials API](https://clinicaltrialsapi.cancer.gov) <br>
- [Every Cure](https://www.everycure.org) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, API calls, configuration] <br>
**Output Format:** [Markdown with JSON-RPC curl examples and setup guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Queries may use the hosted Curiloo MCP endpoint or a local medical-mcps service; some upstream databases may require optional API keys or impose rate limits.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
