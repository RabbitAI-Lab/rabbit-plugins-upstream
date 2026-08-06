## Description: <br>
Accurately identifies cat and dog breeds and supports distinguishing between different individuals in multi-pet households; an essential assistant for intelligent pet butlers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to analyze pet images, videos, or media URLs for cat and dog breed identification, individual pet distinction, confidence-bearing structured results, and history/report lookup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet images, videos, or supplied URLs are processed by external LifeEmergence services. <br>
Mitigation: Use only media appropriate for cloud processing, avoid private or internal URLs, and do not submit sensitive home footage unless cloud processing is acceptable. <br>
Risk: The skill can create or reuse a persistent account identity and store service tokens in the workspace. <br>
Mitigation: Run it in an isolated workspace, review stored credentials before reuse, and remove local account/token data when the skill is no longer needed. <br>
Risk: History lookup can retrieve account-linked prior analysis reports. <br>
Mitigation: Confirm the user intends to list historical reports and that the active workspace identity is the expected one before using report-history functionality. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-breed-individual-recognition-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Pet recognition API documentation](references/api_doc.md) <br>
- [Common analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON] <br>
**Output Format:** [Markdown text containing structured JSON results and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write the same result text to a user-specified output file.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release evidence; artifact frontmatter reports 1.0.10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
