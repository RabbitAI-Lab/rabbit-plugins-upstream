## Description: <br>
Endpoints document management API toolkit. Scan documents with AI extraction and organize structured data into categorized endpoints. Use when the user asks to: scan a document, upload a file, list endpoints, inspect endpoint data, check usage stats, create or delete endpoints, get file URLs, or manage document metadata. Requires ENDPOINTS_API_KEY from endpoints.work dashboard. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[adamkristopher](https://clawhub.ai/user/adamkristopher) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to connect to the Endpoints document management API, scan files or text, organize extracted metadata into endpoints, inspect endpoint data, retrieve file URLs, check usage, and manage endpoint records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Files and text passed to scan functions are sent to the external Endpoints API. <br>
Mitigation: Use the skill only with content intended for endpoints.work and verify ENDPOINTS_API_URL before execution. <br>
Risk: Endpoint and item delete functions can remove remote data without built-in confirmation safeguards. <br>
Mitigation: Require explicit user confirmation with the exact endpoint path or item ID before any delete operation. <br>
Risk: API keys and locally saved result files may expose sensitive document metadata. <br>
Mitigation: Keep ENDPOINTS_API_KEY private and clean up results/ after processing sensitive documents. <br>


## Reference(s): <br>
- [Endpoints API Reference](references/api-reference.md) <br>
- [Endpoints API](https://endpoints.work/api) <br>
- [API Keys](https://endpoints.work/api-keys) <br>
- [ClawHub Skill Page](https://clawhub.ai/adamkristopher/skills/endpoints) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, API calls, JSON files, guidance] <br>
**Output Format:** [TypeScript functions, JSON result files, Markdown summaries, and concise setup or usage guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ENDPOINTS_API_KEY and may save API responses under results/{category}/.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
