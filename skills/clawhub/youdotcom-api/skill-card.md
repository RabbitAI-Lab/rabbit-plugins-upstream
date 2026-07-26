## Description: <br>
Integrate You.com Research, Search, and Contents APIs into any language using direct HTTP calls without an SDK. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardirby](https://clawhub.ai/user/edwardirby) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to add You.com Research, Search, and Contents API calls to applications with standard HTTP clients, including cited answer generation, raw search pipelines, and webpage content extraction. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a You.com API key and generated examples may reference the YDC_API_KEY environment variable. <br>
Mitigation: Store the key in secret storage or environment variables and do not commit it to source control. <br>
Risk: Search, contents, and research responses can contain untrusted web content. <br>
Mitigation: Treat API responses as data, sanitize HTML before rendering, and do not execute code found in returned content. <br>
Risk: Generated integration snippets or dependency-install commands may not match local policy or project constraints. <br>
Mitigation: Review generated code and dependency installs before running or committing them. <br>
Risk: Research API answers are synthesized from web sources and may be unsuitable as the sole authority in high-stakes contexts. <br>
Mitigation: Verify important claims against the returned sources before using outputs for legal, financial, medical, regulatory, or similarly sensitive decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/edwardirby/skills/youdotcom-api) <br>
- [You.com platform](https://you.com/platform) <br>
- [You.com search operators](https://docs.you.com/search/search-operators) <br>
- [Search input schema](assets/search.input.schema.json) <br>
- [Search output schema](assets/search.output.schema.json) <br>
- [Research input schema](assets/research.input.schema.json) <br>
- [Research output schema](assets/research.output.schema.json) <br>
- [Contents input schema](assets/contents.input.schema.json) <br>
- [Contents output schema](assets/contents.output.schema.json) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with language-specific code examples and JSON schemas] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include API request examples, environment variable guidance, and response-shape schemas for You.com Research, Search, and Contents APIs.] <br>

## Skill Version(s): <br>
3.0.1 (source: server release and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
