## Description: <br>
Analyzes pet face images or videos for visual signs of eye redness, abnormal tearing, and pupil or cornea opacity, then returns structured anomaly alerts, guidance, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent operators use this skill to run a pet eye health visual check from close-up images, videos, or URLs, including daily self-checks, boarding-center inspections, veterinary triage, and senior-pet cataract monitoring. The output is a visual screening aid and does not replace professional veterinary diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet images, videos, or provided URLs are sent to the Life Emergence cloud service for analysis. <br>
Mitigation: Use only media that the user is authorized to upload, avoid unnecessary sensitive content, and confirm cloud-processing acceptability before deployment. <br>
Risk: The skill can create or reuse a persistent identity and store account tokens in the workspace data directory. <br>
Mitigation: Run only in trusted workspaces, protect workspace data files, and rotate or remove stored credentials when access is no longer needed. <br>
Risk: Cloud-stored report history is tied to the persistent identity and may be retrieved by the skill. <br>
Mitigation: Use separate identities for separate users or environments and review account, retention, and access expectations before enabling history lookup. <br>
Risk: Eye anomaly results are visual screening guidance and may be incomplete or medically misleading if treated as diagnosis. <br>
Mitigation: Present outputs as non-diagnostic screening information and direct users to a veterinarian for suspected abnormalities or urgent symptoms. <br>


## Reference(s): <br>
- [Pet Eye Anomaly Detection API Documentation](artifact/references/api_doc.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-eye-anomaly-detection-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown and JSON-like structured text with anomaly findings, recommendations, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save output to a local file when requested and may return cloud report history for the current persistent identity.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter states 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
