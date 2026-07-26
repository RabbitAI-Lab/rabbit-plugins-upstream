## Description: <br>
Based on computer vision, this skill analyzes pet camera or feeder media for feeding, drinking, excretion, mental state, vomiting, and limping indicators, then outputs health monitoring reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External pet-care users and developers use this skill to submit pet monitoring media or media URLs to the publisher's cloud service, receive structured pet health reports, and query historical monitoring reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet media or supplied URLs are sent to the publisher's cloud service for analysis and may reveal household context or routines. <br>
Mitigation: Use only media suitable for the provider to process; avoid footage containing people, interiors, or sensitive routines unless the provider's retention and access practices are acceptable. <br>
Risk: The skill creates or reuses a local identity and stores service tokens locally for API access. <br>
Mitigation: Review local identity and token storage before installing, restrict workspace access, and clear stored identity or token data when the skill is no longer needed. <br>
Risk: Health analysis reports are informational and can be incomplete or wrong. <br>
Mitigation: Treat outputs as pet health reference material and consult a veterinarian for diagnosis, treatment, or urgent symptoms. <br>


## Reference(s): <br>
- [Pet health analysis API documentation](artifact/references/api_doc.md) <br>
- [smyx analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-health-monitoring-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files] <br>
**Output Format:** [Plain text or Markdown report with optional JSON detail and optional saved output file.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports may include cloud report export links; local video files are limited to mp4, avi, or mov up to 10 MB.] <br>

## Skill Version(s): <br>
1.0.8 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
