## Description: <br>
Detects cats, dogs, and birds in images or video streams for home pet monitoring, then returns structured detection reports and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze home monitoring images, videos, local files, or media URLs for common pets, including cats, dogs, and birds. It can also retrieve cloud-hosted historical pet detection reports associated with the current account identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends media to the publisher's cloud service for analysis. <br>
Mitigation: Install only when that cloud processing is acceptable for the media being analyzed, and avoid sensitive media unless the deployment has approved this data flow. <br>
Risk: The skill creates or reuses an account-linked identity and stores local authentication tokens in a workspace SQLite database. <br>
Mitigation: Use an isolated workspace for this skill, restrict access to the workspace data directory, and review or clear stored tokens when users or agents share the environment. <br>
Risk: Historical report retrieval can automatically fetch cloud-hosted reports for the current account identity. <br>
Mitigation: Confirm the account context before requesting historical reports and avoid running the skill in shared workspaces where account identity may be ambiguous. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-detection-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Pet detection API documentation](artifact/references/api_doc.md) <br>
- [SMYX analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Shell commands, Files] <br>
**Output Format:** [Markdown reports or JSON results, with optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports can include detection counts, structured pet detection fields, historical report tables, and cloud report links.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
