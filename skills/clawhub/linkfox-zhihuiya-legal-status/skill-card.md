## Description: <br>
This skill queries Zhihuiya (PatSnap) for patent legal status, validity, and legal-event history by patent ID or publication number. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, patent analysts, and agents use this skill to check whether patents are active, inactive, pending, expired, revoked, transferred, licensed, pledged, or involved in other legal events. It supports single or batch lookup by patent ID or publication number. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: LinkFox/PatSnap lookups consume credits and may incur high cost for large result sets. <br>
Mitigation: Tell the user that the lookup consumes credits before running it, batch identifiers deliberately, and avoid automatic retries or modified follow-up searches without user approval. <br>
Risk: Full API responses are saved locally, which may expose sensitive patent research in shared workspaces. <br>
Mitigation: Use the skill only in appropriate workspaces, review where output files are written, and clean up saved response files when they are no longer needed. <br>
Risk: The security scan flags automatic feedback reporting and storage-location behavior for review. <br>
Mitigation: Review the feedback-reporting instruction and file-output behavior before installation, and disable or modify them if they do not match the deployment's privacy and storage requirements. <br>


## Reference(s): <br>
- [智慧芽专利法律状态查询 API 参考](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-legal-status) <br>
- [LinkFox Skills](https://skill.linkfox.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with JSON API responses, saved JSON files, and summarized stdout for large responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Queries accept patentId or patentNumber values, up to 100 comma-separated identifiers per request; responses may be cached for 24 hours and full API responses are written locally.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
