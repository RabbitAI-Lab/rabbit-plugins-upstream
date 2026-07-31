## Description: <br>
Analyzes pet oral snapshot images or videos through cloud APIs to report gum color, redness level, tartar coverage, and non-diagnostic oral-health observations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users can use this skill in pet cameras, smart pet products, and pet health management workflows to analyze uploaded or URL-based pet oral media and return structured oral-health observations. It is for visual monitoring and care guidance, not disease diagnosis or treatment planning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet media files, media URLs, and analysis requests are sent to the publisher's cloud APIs. <br>
Mitigation: Install and run the skill only in workspaces where cloud processing by the publisher is acceptable; avoid submitting sensitive or unnecessary media. <br>
Risk: The skill silently reuses or creates an account identity and can fetch historical reports from that cloud account context. <br>
Mitigation: Use a dedicated workspace identity for this skill and review historical-report access expectations before enabling list queries. <br>
Risk: Reusable identity and authentication tokens may be persisted in the local workspace database. <br>
Mitigation: Keep the workspace data directory access-controlled and rotate or remove the local identity data when the workspace is shared or decommissioned. <br>
Risk: Oral-health outputs are observations and care guidance, not veterinary diagnosis. <br>
Mitigation: Treat results as screening support and consult a veterinarian for diagnosis, treatment, severe symptoms, or persistent oral-health concerns. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-oral-snapshot-gum-redness-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands] <br>
**Output Format:** [Markdown text with structured JSON-style analysis results, history-report lists, and report links; optional file output is supported.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts local media paths or public media URLs, supports cat/dog/other pet type selection, and can query cloud-stored historical reports.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
