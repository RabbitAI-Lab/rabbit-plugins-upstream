## Description: <br>
PubMed (pubmed.ncbi.nlm.nih.gov). Use this skill for PubMed search and article retrieval tasks through the OOMOL PubMed connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to search PubMed, retrieve normalized article records, convert article identifiers, find related or citing articles, and match biomedical citations without calling PubMed APIs directly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PubMed queries and article requests are routed through OOMOL and depend on its account connection and billing model. <br>
Mitigation: Use the skill only when that routing is acceptable, and run authentication, connection, or billing setup steps only after a command fails for that reason. <br>
Risk: Connector payloads can be malformed or become stale if action schemas change. <br>
Mitigation: Inspect the live action schema with `oo connector schema` before constructing each payload. <br>


## Reference(s): <br>
- [ClawHub PubMed skill page](https://clawhub.ai/oomol/skills/oo-pubmed) <br>
- [Publisher profile](https://clawhub.ai/user/oomol) <br>
- [PubMed homepage](https://pubmed.ncbi.nlm.nih.gov/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON connector payloads or responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the live oo connector schema before building action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence.release.version and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
