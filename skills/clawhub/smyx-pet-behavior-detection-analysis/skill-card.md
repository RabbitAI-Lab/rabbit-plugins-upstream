## Description: <br>
Identifies common abnormal pet behaviors such as scratching, biting, destructive chewing, jumping, digging, chasing, and separation anxiety, helping owners understand their pet's habits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to analyze pet monitoring videos or video URLs for abnormal behaviors, receive structured behavior reports and suggestions, and query previously generated cloud reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet media or media URLs are sent to the vendor cloud service for analysis. <br>
Mitigation: Use only media appropriate for vendor processing, and confirm the publisher's retention and authorization model before using private videos. <br>
Risk: The skill creates or reuses an internal account identity and may store account or session tokens locally. <br>
Mitigation: Review and protect the local data directory before and after use, and clear stored credentials before sharing or archiving the workspace. <br>
Risk: The skill can query cloud report history associated with the internal identity. <br>
Mitigation: Confirm the user is authorized to view the associated report history and avoid exposing report links outside the intended context. <br>


## Reference(s): <br>
- [API interface documentation](references/api_doc.md) <br>
- [Analysis API error-code reference](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown reports and JSON analysis results with optional report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can save output to a user-specified file; supports basic, standard, and JSON detail modes.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata; artifact frontmatter says 1.0.10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
