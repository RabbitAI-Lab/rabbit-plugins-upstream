## Description: <br>
Detects possible tail-loss events in gecko and lizard images or videos by sending media to a cloud analysis service that compares tail length, visible wounds, scabbing, regeneration signs, and image quality, then returns a structured report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze uploaded local or URL-based reptile tail media, detect possible autotomy or injury events, query prior cloud reports, and receive structured monitoring outputs. It is intended for reptile enclosure monitoring workflows where visual alerts and report links help guide follow-up review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends local media or supplied URLs to lifeemergence.com cloud services for processing. <br>
Mitigation: Use only media suitable for remote processing and avoid unrelated private media. <br>
Risk: The skill may create or reuse local identity state and store remote access tokens in the workspace database. <br>
Mitigation: Install only in trusted workspaces, avoid shared workspaces, and review or remove stored workspace data when access should end. <br>
Risk: Cloud history queries can expose account-linked prior report data. <br>
Mitigation: Use separate workspaces or accounts when report history should remain separated across users or projects. <br>
Risk: Visual tail-loss outputs could be mistaken for veterinary diagnosis or treatment direction. <br>
Mitigation: Treat results as visual screening guidance and route wound care or infection concerns to a qualified reptile veterinarian. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-reptile-tail-loss-detection-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/18072937735) <br>
- [API interface documentation](references/api_doc.md) <br>
- [Skill usage demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files, Guidance] <br>
**Output Format:** [Markdown text with structured JSON report content, history-list output, and report-export links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write the rendered analysis result to a user-specified file; analysis and history data are fetched from remote services.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
