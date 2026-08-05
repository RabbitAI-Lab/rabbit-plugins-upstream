## Description: <br>
Generates condensed album highlights by extracting target video segments based on specified keywords or subjects. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to submit local or URL-based videos with target keywords, then receive structured condensed highlight analysis, report links, or cloud history results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local media files or video URLs may be sent to configured lifeemergence.com cloud services for analysis. <br>
Mitigation: Use only videos whose provider, consent, and retention requirements are acceptable; avoid sensitive media unless those conditions are satisfied. <br>
Risk: The skill may create or reuse an internal identity and retrieve cloud report history associated with that identity. <br>
Mitigation: Run the skill in a controlled workspace, review who can access that workspace, and avoid sharing generated identities or history outputs. <br>
Risk: Authentication tokens may be stored in the workspace data database. <br>
Mitigation: Restrict workspace file access, clean local data after use when appropriate, and rotate or revoke credentials if the workspace may have been exposed. <br>
Risk: Keyword-target extraction quality is unverified by the provided evidence. <br>
Mitigation: Test representative sample videos and manually review generated highlight reports before relying on them for important decisions or publication. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-custom-timelapse-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/18072937735) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](references/api_doc.md) <br>
- [Analysis API interface documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, files, guidance] <br>
**Output Format:** [Markdown text with JSON report bodies, report links, and optional saved output files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may depend on cloud analysis services and the selected detail level.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.11) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
