## Description: <br>
A fast web content extraction skill that converts webpages into clean Markdown for AI agents, IDEs, and LLM pipelines. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and AI agents use this skill to fetch HTTP/HTTPS pages, convert content to Markdown, and prepare website information for documentation reading, content analysis, and LLM workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Target URLs and related parameters are sent to the XiaoBenYang third-party service. <br>
Mitigation: Install only when this data sharing is acceptable, and avoid submitting sensitive or confidential URLs unless the publisher documents how the service handles that data. <br>
Risk: The API key is stored locally in a .env file. <br>
Mitigation: Keep the .env file out of version control, restrict local file access, and rotate the key if it may have been exposed. <br>
Risk: The optional cookiesFile input can expose authenticated session data. <br>
Mitigation: Avoid using cookiesFile with sensitive sessions unless handling is documented; use a minimal, purpose-specific cookie file when authenticated extraction is necessary. <br>
Risk: The security scan verdict is suspicious because the skill relies on a third-party API, local API key storage, and unclear scoping of user data sent upstream. <br>
Mitigation: Review the skill before deployment and prefer a version that narrows the remote tool allowlist and pins patched dependencies. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/read-website) <br>
- [XiaoBenYang API key service](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Configuration] <br>
**Output Format:** [JSON result wrapper containing raw extracted content, typically Markdown, with success and message fields.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires XBY_APIKEY; accepts url, pages, and cookiesFile inputs.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
