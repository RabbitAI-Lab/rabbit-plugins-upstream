## Description: <br>
Monitors workplace images or video through a remote computer-vision service to identify personnel presence, on-duty status, leave-post events, and absence duration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Operations, security, and workplace management teams use this skill to analyze monitoring images or videos for employee absence and leave-post events. It can also query prior absence-monitoring reports associated with the configured local identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Workplace surveillance media or URLs are processed by a configured remote service. <br>
Mitigation: Deploy only with explicit consent, retention, access-control, and deletion guidance for real employee footage. <br>
Risk: Report history is tied to a local identity and tokens that may be created or reused automatically. <br>
Mitigation: Restrict access to the runtime environment and define identity, token, and report-history handling procedures before workplace use. <br>


## Reference(s): <br>
- [Personnel absence monitoring API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-staff-absence-detection-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON analysis report with status counts, absence duration, report links, and optional saved output files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts local image or video files, media URLs, confidence and absence thresholds, and a history-list mode.] <br>

## Skill Version(s): <br>
1.0.10 (source: server evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
