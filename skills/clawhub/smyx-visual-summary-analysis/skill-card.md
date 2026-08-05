## Description: <br>
Performs AI analysis on input video clips/image content and generates a smooth, natural scene description. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agents use this skill to analyze uploaded or URL-based images and videos, generate visual scene summaries, and retrieve cloud-hosted historical visual-analysis reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded images, videos, or supplied URLs are processed by the skill's cloud service. <br>
Mitigation: Avoid sensitive media unless cloud processing is acceptable for the intended use case. <br>
Risk: The skill silently creates or reuses an internal account identity and stores account tokens locally. <br>
Mitigation: Review or clear local data such as data/smyx-api-key.txt and the workspace SQLite database when identity reuse is not desired. <br>
Risk: The skill can retrieve cloud-hosted report history associated with the internal identity. <br>
Mitigation: Review installation and execution behavior before deployment, especially where report history may contain sensitive visual-analysis results. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-visual-summary-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Visual summary API documentation](artifact/references/api_doc.md) <br>
- [Analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, files, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON analysis report, optionally written to an output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured visual-analysis results, report links, and cloud history tables.] <br>

## Skill Version(s): <br>
1.0.11 (source: server release metadata; artifact frontmatter says 1.0.10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
