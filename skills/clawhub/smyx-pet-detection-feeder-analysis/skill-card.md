## Description: <br>
Detects and recognizes cats and dogs from smart feeder or IPC camera images and videos, supports pet identity matching and enrollment, and returns structured analysis reports for smart feeding workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze smart feeder or IPC camera media, enroll pet identities, and query historical pet detection reports for smart feeding scenarios. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends pet-camera images, videos, URLs, report queries, and internal user identifiers to lifeemergence.com and open.lifeemergence.com services. <br>
Mitigation: Use only when that remote processing is acceptable, and review the publisher's account, retention, deletion, and data handling documentation before installation. <br>
Risk: The skill silently creates or logs into a remote account and stores authentication tokens locally without clear user control. <br>
Mitigation: Run in an isolated workspace where appropriate, and verify how to clear the local SQLite database, data/smyx-api-key.txt identity state, and any retained tokens. <br>


## Reference(s): <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration] <br>
**Output Format:** [Markdown reports, JSON detail output, and optional saved text or JSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts local media paths or public media URLs; supports mp4, avi, mov, jpg, png, and jpeg inputs up to 10 MB.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
