## Description: <br>
AI-powered pet grooming effect assessment: detects mat residue area, dandruff coverage, and coat smoothness from post-grooming images, outputs a 0-100 grooming score with targeted re-grooming suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, pet owners, and pet grooming operators use this skill to assess post-grooming pet images or videos for mat residue, dandruff coverage, coat smoothness, and whether additional grooming or care is suggested. The output is a visual grooming-quality assessment, not medical diagnosis or treatment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet images, videos, URLs, and report-history requests may be sent to a configured cloud service. <br>
Mitigation: Use only with consent to upload pet media and review the configured service endpoint before running analysis or history lookup. <br>
Risk: The skill can create or reuse an internal identity and persist service tokens in a workspace SQLite database. <br>
Mitigation: Run in an isolated workspace, review local token storage after use, and prefer a version that asks for explicit confirmation before identity creation or token persistence. <br>
Risk: History report lookup can be triggered by report-history language and queries the cloud service. <br>
Mitigation: Require operator confirmation before history lookup in governed deployments, or disable automatic history-query behavior. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-grooming-effect-assessment-analysis) <br>
- [API interface documentation](artifact/references/api_doc.md) <br>
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [Skill usage demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON analysis report with optional report links and shell-command usage examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can write an output file when requested; history-report listing is formatted as Markdown from cloud API results.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter reports 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
