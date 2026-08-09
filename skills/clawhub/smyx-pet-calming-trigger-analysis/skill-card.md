## Description: <br>
Analyzes pet-monitoring videos or video URLs through cloud APIs to produce structured pet emotion and behavior reports, report links, and report-history listings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent operators can use this skill to submit pet camera videos or URLs for cloud analysis of anxiety-related behavior and to retrieve prior analysis reports. It should be treated as a reporting and decision-support skill, not as proof that local soothing devices will be controlled automatically. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet camera videos or video URLs are sent to configured cloud services for analysis. <br>
Mitigation: Use the skill only for footage that is approved for cloud processing, and avoid submitting sensitive household scenes unless the operator accepts that data flow. <br>
Risk: The skill can silently create or reuse an internally managed identity and associate report history with it. <br>
Mitigation: Review identity handling before deployment and run it in an isolated workspace when report history should not be shared across sessions. <br>
Risk: Service tokens may be persisted in a local shared SQLite database. <br>
Mitigation: Restrict filesystem access to the workspace, rotate credentials after testing, and remove local state when uninstalling or transferring the environment. <br>
Risk: The public description claims soothing-device automation, but the reviewed behavior primarily performs cloud analysis and report retrieval. <br>
Mitigation: Present outputs as analysis and recommendations only unless separate, reviewed device-control integrations are installed and verified. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-calming-trigger-analysis) <br>
- [Pet calming trigger API documentation](references/api_doc.md) <br>
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-like structured text with report export links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May print progress messages and can write the returned analysis text to a user-specified output file.] <br>

## Skill Version(s): <br>
1.0.12 (source: server release evidence; artifact frontmatter says 1.0.11) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
