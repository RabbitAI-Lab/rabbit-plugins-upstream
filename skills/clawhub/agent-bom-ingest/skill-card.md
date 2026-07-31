## Description: <br>
Validate and ingest operator-pushed agent-bom inventory JSON from AWS, Azure, GCP, Snowflake, CMDB, or endpoint collectors for local findings, graph, policy, provenance, and auditor-ready exports without giving agent-bom direct cloud credentials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[msaad00](https://clawhub.ai/user/msaad00) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, security engineers, and auditors use this skill to validate canonical inventory JSON, run local agent-bom scans, and export findings for automation, review, or compliance workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Inventory files or export destinations chosen by the operator may be untrusted or malformed. <br>
Mitigation: Confirm trust in the agent-bom CLI, validate inventory against the packaged schema, and only scan inventory files and write exports selected by the operator. <br>
Risk: Optional control-plane push can expose API tokens or send inventory data to an unintended endpoint. <br>
Mitigation: Use an operator-provided destination URL and API token through environment variables, and avoid exposing secrets in chat or outputs. <br>
Risk: Optional vulnerability enrichment contacts external advisory services during local scans. <br>
Mitigation: Treat OSV and GitHub Advisory lookups as operator-directed optional network use and run them only when appropriate for the inventory workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-ingest) <br>
- [agent-bom repository](https://github.com/msaad00/agent-bom) <br>
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/) <br>
- [OSV API](https://api.osv.dev/v1) <br>
- [GitHub Advisory Database API](https://api.github.com/advisories) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown, JSON, Code] <br>
**Output Format:** [Markdown guidance with shell commands and export format choices] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local scan and export guidance for JSON, SARIF, HTML, Markdown, CycloneDX, or SPDX outputs.] <br>

## Skill Version(s): <br>
0.98.2 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
