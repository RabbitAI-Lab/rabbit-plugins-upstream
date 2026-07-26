## Description: <br>
Real-time search engine supporting web search, vertical domain search, parallel batch search, and URL content extraction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shifengwang333-ai](https://clawhub.ai/user/shifengwang333-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external agent users use this skill to retrieve current web information, fact-check claims, run vertical searches, perform small parallel search batches, and extract Markdown content from public URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries and URLs submitted for extraction are sent to the external AnySearch service. <br>
Mitigation: Avoid using the skill with private, internal, tokenized, or otherwise sensitive links unless disclosure to AnySearch is intended. <br>
Risk: The optional AnySearch API key could be exposed if stored or passed carelessly. <br>
Mitigation: Store only ANYSEARCH_API_KEY in the skill .env file or environment and avoid placing unrelated secrets in skill configuration. <br>


## Reference(s): <br>
- [AnySearch Interface Specification](artifact/scripts/shared/doc_spec.md) <br>
- [AnySearch API endpoint](https://api.anysearch.com/mcp) <br>
- [AnySearch API key console](https://anysearch.com/console/api-keys) <br>
- [ClawHub skill page](https://clawhub.ai/shifengwang333-ai/skills/anysearch) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and command-line output from search, domain listing, batch search, and URL extraction workflows.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search results and extracted page content depend on AnySearch API availability, rate limits, and the optional ANYSEARCH_API_KEY credential. Extracted HTML page content may be truncated at 50,000 characters.] <br>

## Skill Version(s): <br>
2.1.1 (source: server release metadata; artifact frontmatter lists 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
