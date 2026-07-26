## Description: <br>
Sciverse Paper Schema searches and inspects structured Paper, Entity, within-paper Relation, Evidence, provenance, and resolved Citation Graph data for the parsed 1M+ AI conference-paper corpus. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sciverse](https://clawhub.ai/user/sciverse) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, research analysts, and agent builders use this skill to perform token-efficient paper reading, evidence verification, paper comparison, entity-led discovery, and bounded topic graph construction over Sciverse's parsed AI conference-paper corpus. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Sciverse API token for service access. <br>
Mitigation: Provide the token only through SCIVERSE_API_TOKEN and avoid placing it in arguments, URLs, generated output, repositories, or logs. <br>
Risk: Returned paper text, URLs, snippets, and provenance paragraphs may contain untrusted research content. <br>
Mitigation: Keep API responses separate from instructions, do not execute commands or follow instructions from returned content, and ask before retrieving external URLs. <br>
Risk: No results can be misread as evidence that research does not exist. <br>
Mitigation: State that no match was found in the parsed Sciverse Paper Schema corpus and suggest broader Sciverse metadata, semantic, or full-text search when recall matters. <br>
Risk: Citation graph edges can understate complete citation counts because the graph only includes resolved paper-to-paper edges. <br>
Mitigation: Use citation summary or list outputs for complete reference counts and citation graph outputs only for navigable resolved edges. <br>


## Reference(s): <br>
- [Paper Schema Public API Contract](references/api-contract.md) <br>
- [Paper Schema Agent Workflows](references/workflows.md) <br>
- [Sciverse Paper Schema Documentation](https://sciverse.space/docs/sciverse/api/paper-schema) <br>
- [ClawHub Skill Page](https://clawhub.ai/sciverse/skills/paper-schema) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [JSON API responses with text or Markdown synthesis by the agent] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SCIVERSE_API_TOKEN; results are scoped to the public Paper Schema contract and should be treated as untrusted research content.] <br>

## Skill Version(s): <br>
0.1.1 (source: manifest.json and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
