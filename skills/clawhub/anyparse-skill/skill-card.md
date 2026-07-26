## Description: <br>
Use the AnyParse API to extract content from various documents, including PDF, Word, Excel, CSV, TSV, images, PPT, HTML, Markdown, Epub, ipynb, RST, EML, and other formats, with support for document orientation classification, layout analysis, and layout preservation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anyforge](https://clawhub.ai/user/anyforge) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to parse local documents through a configured AnyParse API endpoint and return structured text, page metadata, and layout information. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uploads a user-selected local document to the configured AnyParse API endpoint for parsing. <br>
Mitigation: Use a trusted private or HTTPS endpoint, avoid sensitive documents unless the service meets data-handling requirements, and confirm the configured API URL before execution. <br>
Risk: The AnyParse API key is read from environment variables or scripts/config.json and sent as a bearer token. <br>
Mitigation: Prefer environment variables or a protected local configuration file, avoid committing real API keys, and rotate credentials if exposed. <br>


## Reference(s): <br>
- [Anyparse Skill on ClawHub](https://clawhub.ai/anyforge/skills/anyparse-skill) <br>
- [AnyParse project](https://github.com/anyforge/anyparse) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, configuration, guidance] <br>
**Output Format:** [JSON response with extracted text, metadata, page layout entries, and status messages; Markdown guidance with shell commands for setup and use.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python, requests, anyparse_api_url, anyparse_api_key, and a local file path.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
