## Description: <br>
Analyzes night-time crib video or image input to estimate infant blanket coverage, identify blanket-kicking or slip-off events, and return alerts and structured reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze infant crib night-monitoring media for blanket coverage status, kicking events, low-coverage alerts, and report links. Results are auxiliary monitoring information and do not replace adult supervision. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Infant or nursery media may be sent to the publisher's cloud service for analysis. <br>
Mitigation: Use only with guardian consent, avoid unnecessary third-party video URLs, and limit inputs to the minimum media needed for the analysis. <br>
Risk: The skill can automatically create or reuse account/session state and store reusable tokens in the workspace data directory. <br>
Mitigation: Run in a sandboxed workspace, review or clear the local data database on uninstall, and avoid sharing the workspace data directory. <br>
Risk: Historical report queries retrieve sensitive prior analysis records from the cloud service. <br>
Mitigation: Treat report listings and exported report links as sensitive, and restrict use to authorized guardians or operators. <br>
Risk: Blanket coverage alerts are auxiliary visual analysis and may be incorrect or delayed. <br>
Mitigation: Keep adult supervision in place and do not rely on this skill as a medical device or sole safety monitor. <br>


## Reference(s): <br>
- [Infant Blanket Kick Detection API Documentation](references/api_doc.md) <br>
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown and structured JSON-like analysis text with report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save the rendered analysis text to a user-specified output file.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact frontmatter reports 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
