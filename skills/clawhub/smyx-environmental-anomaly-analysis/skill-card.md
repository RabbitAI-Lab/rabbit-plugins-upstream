## Description: <br>
Combines continuous livestock barn video with environmental sensor data such as temperature, humidity, and ammonia to identify group stress responses caused by abnormal in-barn conditions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Farm operators, livestock environment teams, and agent developers use this skill to analyze barn video and optional sensor time series for environment-linked group stress indicators. It returns structured anomaly findings, stress levels, historical report listings, and report links for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan verdict is suspicious because the skill sends barn media or supplied URLs to a Life Emergence/Open API service and can access authenticated report history. <br>
Mitigation: Use only with non-sensitive footage and sensor data that may be processed by that external service; review the service relationship and data handling expectations before deployment. <br>
Risk: The skill performs automatic identity creation and stores or reuses identity-linked values and tokens in local workspace data. <br>
Mitigation: Run it in a dedicated workspace, inspect local data persistence such as data/smyx-api-key.txt and the SQLite token store, and avoid shared workspaces unless account-linking and retention behavior is acceptable. <br>
Risk: Analysis output is an anomaly-screening aid and may be incorrect or incomplete for animal welfare or facility control decisions. <br>
Mitigation: Treat results as review material and require qualified personnel to verify findings before changing equipment settings or making operational decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-environmental-anomaly-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](artifact/references/api_doc.md) <br>
- [SMYX analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, files] <br>
**Output Format:** [Markdown report text with JSON-style structured analysis and optional saved output file.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include behavior findings, environmental correlation results, stress levels, historical report lists, and cloud report links.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; SKILL.md frontmatter says 1.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
