## Description: <br>
Extracts and analyzes images from local files, URLs, or base64 input through an upstream API for LLM visual analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external agent users use this skill to send image inputs from files, URLs, or base64 strings to an upstream image-analysis service and summarize the returned JSON for visual content, OCR, or object-recognition tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Image content, image URLs, local-path-derived data, and API keys may be sent to an upstream service. <br>
Mitigation: Use only non-sensitive images and URLs unless the publisher clearly documents the remote data flow and credential handling. <br>
Risk: The artifact persists XBY_APIKEY to a local .env file. <br>
Mitigation: Make credential persistence explicit to the user and avoid shared workspaces or sensitive credentials during evaluation. <br>
Risk: ClawHub security evidence marks the release as suspicious because the documentation and credential handling are inconsistent for a simple image utility. <br>
Mitigation: Review the release and scanner summary before deployment; avoid sensitive screenshots, IDs, invoices, private documents, or secrets. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/extract-image) <br>
- [Publisher profile](https://clawhub.ai/user/alinklab) <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Guidance] <br>
**Output Format:** [Text or JSON summaries derived from upstream API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires XBY_APIKEY; file, URL, and base64 image inputs may be sent to the upstream service.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
