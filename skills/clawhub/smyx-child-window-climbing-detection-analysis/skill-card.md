## Description: <br>
Analyzes fixed-camera images or videos of window and balcony areas to detect child climbing, leaning, railing-crossing, gripping, and other fall-risk behaviors, then returns alerts and structured analysis reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, home-safety operators, childcare operators, and smart-camera integrators use this skill to analyze child activity near windows or balconies and receive structured warning results or cloud report history. It is intended as an auxiliary monitoring and alerting tool, not a substitute for adult supervision. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Child or home video files and URLs are sent to LifeEmergence cloud endpoints for analysis. <br>
Mitigation: Install and use only in deployments with guardian consent, privacy review, and appropriate retention controls for child-safety media. <br>
Risk: The skill creates or reuses a local or remote identity and may cache authentication tokens. <br>
Mitigation: Review identity provisioning before installation, restrict local data directory access, and ensure there is a process to revoke tokens and delete local database records. <br>
Risk: Cloud report history may expose prior child-safety analyses and report links. <br>
Mitigation: Limit access to history-listing workflows and confirm that cloud reports can be deleted or governed under the deployment's data policy. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-window-climbing-detection-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Child climbing window/balcony API documentation](artifact/references/api_doc.md) <br>
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON text containing structured analysis results, alert levels, report links, or history tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save the rendered result to a local output file when requested; cloud history queries return report lists associated with the resolved identity.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter reports 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
