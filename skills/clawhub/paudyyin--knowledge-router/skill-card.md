## Description: <br>
Knowledge Router is a unified knowledge-query entry point that routes questions to the best available source across compiled wiki knowledge, conversation memory, ontology graphs, vector search, and domain ontologies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to classify knowledge questions, route searches across wiki, memory, ontology, vector, and domain sources, and return sourced answers with confidence or no-result guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad prompts could trigger searches over prior conversation memory without clear user consent. <br>
Mitigation: Require explicit memory-recall wording or confirmation before querying prior conversations. <br>
Risk: Memory-derived answers could expose or blur sensitive personal, business, or project information. <br>
Mitigation: Review the skill before installing in environments with sensitive memory stores and clearly label memory-derived answers. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/knowledge-router) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown with sourced query results, confidence labels, conflict notes, and no-result guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include source labels for wiki-kb, Ontology, memory, or domain-kit.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
