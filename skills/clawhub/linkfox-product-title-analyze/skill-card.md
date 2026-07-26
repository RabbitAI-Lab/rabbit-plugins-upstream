## Description: <br>
Analyzes product listing titles by tokenizing them and extracting keyword frequencies, scene words, audience words, materials, and other title attribute dimensions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Amazon sellers, marketplace analysts, and agents use this skill to analyze previously retrieved product titles one attribute dimension at a time, then compare recurring keywords and grouped title patterns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Product titles, related product data, session metadata, and possible feedback text may be sent to LinkFox or external services. <br>
Mitigation: Use the skill only with data acceptable for third-party processing, avoid sensitive product information, and confirm API key configuration intentionally. <br>
Risk: Analysis responses and caches can persist locally and may contain business or product data. <br>
Mitigation: Review generated files under the local LinkFox output and cache directories, and delete them when retention is not needed. <br>
Risk: Title analysis can consume paid credits, especially for large product sets or repeated calls. <br>
Mitigation: Confirm high-volume analysis with the user before proceeding and use the built-in cache for repeated identical requests. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-product-title-analyze) <br>
- [LinkFox Publisher Profile](https://clawhub.ai/user/linkfox-ai) <br>
- [API Reference](artifact/references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, saved JSON response files, and summarized JSON or table-ready results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Analyzes one requested title attribute dimension per call; large responses are summarized on stdout while full responses are saved locally.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
