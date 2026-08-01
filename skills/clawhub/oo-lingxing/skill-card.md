## Description: <br>
Lingxing helps agents discover Lingxing ERP tools, inspect their schemas, and run selected actions through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers with an OOMOL-connected Lingxing account use this skill to discover live Lingxing ERP tools, inspect action schemas, and run selected Lingxing actions through the oo CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad Lingxing ERP tool calls may change business data. <br>
Mitigation: Require explicit user confirmation for any action that could create, update, overwrite, or delete ERP data. <br>
Risk: The skill summary emphasizes search and read use while the connector can invoke broader ERP actions. <br>
Mitigation: Review before installing and treat the skill as a general ERP connector rather than a read-only search skill. <br>
Risk: Incorrect payloads could affect the wrong Lingxing operation or records. <br>
Mitigation: Fetch and follow each action's live schema before constructing JSON payloads. <br>


## Reference(s): <br>
- [Lingxing homepage](https://www.lingxing.com) <br>
- [oo CLI repository](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-lingxing) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The agent should inspect the live Lingxing action schema before constructing payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
