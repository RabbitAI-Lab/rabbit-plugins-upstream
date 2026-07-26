## Description: <br>
Uses fixed home-camera video to identify prolonged standing and frequent bending by a pregnant person, summarize posture and fatigue-risk signals, and produce rest reminders for health reference rather than medical diagnosis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers can use this skill to analyze fixed-camera video from homes, prenatal schools, community health centers, or smart-home and pregnancy-management apps for posture, standing-duration, bending-frequency, and reminder generation. The output is intended for wellness reference and should not be used as medical diagnosis or treatment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive in-home pregnancy-related video or video URLs are sent to external Life Emergence services. <br>
Mitigation: Use only with the pregnant person's explicit informed consent, verify the configured service endpoints, and avoid submitting footage unless the privacy and retention terms are acceptable. <br>
Risk: Reports are tied to a persistent local or remote identity and auth tokens may be stored locally. <br>
Mitigation: Use a dedicated workspace or account, review local token storage before deployment, and clear credentials and report history when no longer needed. <br>
Risk: The analysis may be mistaken for clinical advice. <br>
Mitigation: Present outputs as wellness reminders and posture statistics only, and direct users to qualified medical care for symptoms or pregnancy health concerns. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pregnant-posture-fatigue-detection-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Pregnant posture fatigue API documentation](artifact/references/api_doc.md) <br>
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON-style structured analysis with posture metrics, alert type, alert level, reminder text, recommended action, and optional report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write the analysis result to a user-specified output file.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; SKILL.md frontmatter lists 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
