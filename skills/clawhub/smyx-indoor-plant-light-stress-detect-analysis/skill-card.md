## Description: <br>
Detects indoor plant light stress from images, videos, URLs, and optional lux data, then reports whether lighting appears insufficient, excessive, or normal with care suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze indoor plant images, videos, or URLs for signs of low-light or excessive-light stress and receive structured care guidance. It also supports querying cloud-hosted historical light-stress reports associated with the skill's internal identity state. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Plant images, videos, or supplied URLs may be sent to Life Emergence cloud APIs for analysis. <br>
Mitigation: Use the skill only with media and URLs that are acceptable to process through that cloud service. <br>
Risk: The skill may create or reuse persistent local and remote identity state for report history. <br>
Mitigation: Review identity and report-retention expectations before enabling historical report queries. <br>
Risk: Real secrets placed in local API-key files may be mishandled if publisher guidance is unclear. <br>
Mitigation: Avoid storing production secrets in data/smyx-api-key.txt unless the publisher documents that workflow clearly. <br>


## Reference(s): <br>
- [API documentation](artifact/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-indoor-plant-light-stress-detect-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON-style structured analysis with report links and optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call remote Life Emergence APIs for analysis and historical report retrieval.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence; artifact frontmatter says 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
