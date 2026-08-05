## Description: <br>
Analyzes pet training videos or video URLs through a server-side service to judge whether Sit, Down, or Stay commands were executed, returning posture-match results, response timing, structured reports, and report links without medical or behavior-therapy advice. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to evaluate pet command-following from training-area video, including posture matching, command timestamp comparison, response latency, and report-history lookup for remote or smart-device-assisted training workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet-training media or supplied video URLs are sent to lifeemergence.com services for analysis. <br>
Mitigation: Use only media and URLs appropriate for that external service, and confirm retention and account handling before processing sensitive videos. <br>
Risk: The skill can create or reuse a backend identity and store service tokens in a local workspace database. <br>
Mitigation: Review the installation before use, run it in an isolated workspace when possible, and remove local stored data or rotate credentials if access should be withdrawn. <br>
Risk: History queries can retrieve cloud report records associated with the resolved identity. <br>
Mitigation: Run history lookup only for the intended account or workspace, and review report output before sharing it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-training-command-execution-analysis) <br>
- [Pet training command execution API documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown or JSON report text with optional report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save report output to a user-specified file; history queries return structured report lists.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
