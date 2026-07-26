## Description: <br>
Analyzes fixed-camera pet sleep videos through cloud APIs to report sleep and awake states, total sleep duration, roll-over or position-change counts, startle-awakening events, a 0-100 sleep-quality score, recommendations, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External pet owners, animal hospital staff, boarding centers, and developers operating the skill use it to analyze pet bed or rest-area videos for sleep quality indicators and retrieve cloud-hosted historical analysis reports. The output is a sleep-health reference, not a medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet monitoring videos or video URLs are sent to lifeemergence.com cloud APIs for processing. <br>
Mitigation: Use only footage appropriate for third-party cloud processing, avoid sensitive home, hospital, boarding, or third-party footage unless retention and access controls are understood, and prefer non-sensitive test media during evaluation. <br>
Risk: The skill performs silent identity setup and stores an internal user identity plus service tokens in a local workspace database. <br>
Mitigation: Run the skill in a controlled workspace, review local data storage before production use, and remove or rotate stored credentials when the workspace is shared or decommissioned. <br>
Risk: The server security verdict is suspicious because cloud processing, local token storage, and history retrieval may not be obvious to users. <br>
Mitigation: Disclose these behaviors to operators, restrict use to trusted environments, and review the configured endpoints before allowing access to real monitoring footage. <br>


## Reference(s): <br>
- [Pet Sleep Quality Analysis API Documentation](references/api_doc.md) <br>
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-sleep-quality-analysis-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, files, guidance] <br>
**Output Format:** [Markdown text with structured JSON-style analysis results, recommendations, historical report lists, and report export links; optionally saved to an output file.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts local mp4, avi, or mov video files up to 10 MB, or public video URLs processed by the API service; pet type can be cat, dog, or other.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter says 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
