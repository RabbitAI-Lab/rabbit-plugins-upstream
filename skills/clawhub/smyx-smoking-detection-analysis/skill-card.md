## Description: <br>
Detects smoking behavior in uploaded or URL-based images and videos, returns structured smoking-detection reports, and can query historical detection reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Facilities, community, park, and enterprise safety teams use this skill through an agent to analyze images or videos for possible smoking violations and retrieve structured reports for smoking-control and fire-safety workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Surveillance images or videos and report history are processed by lifeemergence.com services. <br>
Mitigation: Use only with media the operator is authorized to submit, and review retention, authorization, and deletion expectations before using sensitive workplace, community, or camera footage. <br>
Risk: The skill creates or reuses local identity state and stores service tokens in a workspace SQLite database. <br>
Mitigation: Run in a controlled workspace, restrict access to local state files, and clear or rotate stored identity and token data when the workspace changes users or trust boundaries. <br>
Risk: Media and identity data are sent to remote services without enough user control. <br>
Mitigation: Confirm organizational approval for remote processing and avoid submitting sensitive footage when the operator cannot accept the remote-processing and identity-handling behavior. <br>


## Reference(s): <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Reference](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown and JSON analysis reports, with Markdown tables for historical report lists.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include detection summaries, monitoring results, management suggestions, report links, and historical report lists.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata; artifact frontmatter lists 1.0.11) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
