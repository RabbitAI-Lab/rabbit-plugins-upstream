## Description: <br>
Analyzes tomato or chili flower and fruit images or videos to count open flowers and young fruits, compute fruit-set rate, and return grower-facing guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External growers, horticulture operators, and agent developers use this skill to analyze tomato or chili flower/fruit media, estimate fruit-set rates, receive pollination or environment adjustment guidance, and view prior analysis reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded media or URLs are sent to lifeemergence cloud services for analysis. <br>
Mitigation: Use only media and URLs suitable for third-party cloud processing; avoid sensitive images or private/internal URLs unless publisher disclosures meet your consent, retention, deletion, and permission requirements. <br>
Risk: The skill silently creates or reuses an identity, stores tokens locally, and queries cloud report history tied to that identity. <br>
Mitigation: Review local identity and token storage before installation, run the skill in an isolated workspace, and avoid using it where silent cloud history linkage is unacceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-flowering-fruit-set-rate-analysis-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API 接口文档](references/api_doc.md) <br>
- [API接口文档](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown and JSON text, including structured analysis reports, report links, and optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts local image/video paths or public media URLs; documented media limit is 10 MB.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter reports 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
