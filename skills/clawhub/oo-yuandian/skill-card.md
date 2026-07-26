## Description: <br>
Yuan Dian lets agents search and read Yuan Dian legal and enterprise data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, legal researchers, and due-diligence analysts use this skill to search and retrieve Yuan Dian cases, regulations, statutory clauses, legal hallucination checks, and enterprise records through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Legal text, enterprise records, and due-diligence queries may be submitted to the Yuan Dian service through the OOMOL connector. <br>
Mitigation: Use the skill only when those queries are appropriate for the connected account and external service. <br>
Risk: Setup, installation, connection, or billing steps can affect the user's local environment or OOMOL account. <br>
Mitigation: Run setup or billing steps only after the matching command failure, and review install or billing commands before running them. <br>
Risk: Connector action schemas can change over time. <br>
Mitigation: Inspect the live action schema with oo connector schema before constructing JSON payloads. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-yuandian) <br>
- [Yuan Dian Homepage](https://open.chineselaw.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with oo CLI shell commands and JSON connector payloads or responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses from connector runs include data and meta.executionId when invoked with --json.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
