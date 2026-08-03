## Description: <br>
Analyzes cat scratch-post video or URL inputs through a remote service to estimate scratching frequency, session duration, intensity, stress indicators, and claw-health observations without medical diagnosis or behavior correction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to submit cat scratch-post area videos or public video URLs for structured behavior observations, including scratch frequency, duration, relative intensity, stress indicators, and report links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet-area videos or supplied video URLs are sent to the lifeemergence.com service for analysis. <br>
Mitigation: Use only media intended for that cloud workflow; avoid private household footage, intranet URLs, presigned links, or sensitive account identifiers. <br>
Risk: The skill can silently create or reuse a cloud-linked identity and store service tokens in a local workspace SQLite database. <br>
Mitigation: Install and run it only in trusted workspaces, review local data storage before use, and remove stored credentials when they are no longer needed. <br>
Risk: The analysis output is observational and may be mistaken for veterinary or behavior-correction advice. <br>
Mitigation: Treat the output as behavior observation data only and seek qualified veterinary guidance for health concerns. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-scratch-frequency-intensity-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [Common analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, files] <br>
**Output Format:** [Markdown text containing structured JSON-style analysis and report links; optional file output when --output is used.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Remote API analysis output; local video inputs are documented as mp4, avi, or mov files up to 10 MB.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter reports 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
