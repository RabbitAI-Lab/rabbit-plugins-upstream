## Description: <br>
This skill analyzes pet oral snapshot images or videos through the publisher's cloud API to estimate gum color, gum redness level, and tartar coverage, then returns oral-health observations and report links without providing a disease diagnosis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill in pet cameras, smart pet products, and pet health management workflows to analyze oral snapshots for visible gum redness and tartar indicators. It supports single-image, video, URL-based, and history-query workflows for structured pet oral-health observations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet images, videos, or media URLs may be sent to the publisher's cloud service for analysis. <br>
Mitigation: Use only media approved for cloud processing, avoid sensitive content, and confirm the publisher's retention and deletion practices before deployment. <br>
Risk: Cloud report history is tied to an automatically selected or created identity. <br>
Mitigation: Review the identity behavior before installation and provide clear user consent, disclosure, and opt-out paths in production workflows. <br>
Risk: Local token or account records may be stored in the workspace data directory. <br>
Mitigation: Restrict workspace access, rotate or delete stored credentials when no longer needed, and prefer a release that documents local storage controls explicitly. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pet-oral-snapshot-gum-redness-analysis) <br>
- [API Documentation](references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown text with optional JSON details and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write a requested output file; cloud history queries are presented as a Markdown table.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata; artifact frontmatter lists 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
