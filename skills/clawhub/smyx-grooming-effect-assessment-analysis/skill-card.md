## Description: <br>
AI-powered pet grooming effect assessment: detects mat residue area, dandruff coverage, and coat smoothness from post-grooming images, then outputs a 0-100 grooming score with targeted re-grooming suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External pet owners, pet salons, and care teams use this skill to assess post-grooming pet images or videos for remaining mats, dandruff coverage, coat smoothness, and follow-up grooming needs. The output is a visual grooming-quality assessment and is not a medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet images or videos may be processed by the vendor cloud service. <br>
Mitigation: Use only with media that is appropriate for vendor cloud processing and disclose the cloud-processing behavior before deployment. <br>
Risk: The skill may create or reuse a local account identity, store tokens in the workspace database, and query prior cloud reports automatically. <br>
Mitigation: Prefer deployment controls that require explicit consent for account creation, token storage, media upload, and history lookup. <br>
Risk: The security verdict is suspicious because user control over account creation, history lookup, and media upload is not clear. <br>
Mitigation: Review the skill before execution, restrict it to trusted workspaces, and verify that identity, token, and upload behavior match local policy. <br>


## Reference(s): <br>
- [API documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON analysis report with scores, observations, recommendations, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports image, video, local file, and URL inputs; historical report lookup returns Markdown tables from the cloud service.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence; artifact frontmatter reports 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
