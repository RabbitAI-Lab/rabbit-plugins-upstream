## Description: <br>
Analyzes fixed-camera video of an elder's water-cup area to count cup pickups, estimate drinking frequency, and surface dehydration-risk reminders for caregivers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External caregivers, family members, and elder-care operators use this skill to analyze home or care-facility video of a water-cup area, review cup-pickup frequency, and receive directional reminders when the pattern suggests possible dehydration risk. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Home video or video URLs may be sent to external services, and cloud report history may be queried. <br>
Mitigation: Require explicit consent from monitored people, avoid unrelated household footage, and confirm cloud processing is acceptable before use. <br>
Risk: The skill may create or reuse local and remote identity records and tokens. <br>
Mitigation: Review or clear the workspace data directory if identity or token reuse is not desired. <br>
Risk: Cup-pickup counts are only an indirect proxy for water intake and may be inaccurate in shared or unstable scenes. <br>
Mitigation: Treat alerts as caregiver prompts rather than medical diagnosis, verify with the elder or caregiver, and seek medical care if symptoms are present. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-drinking-frequency-analysis) <br>
- [API documentation](artifact/references/api_doc.md) <br>
- [SMYX analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON analysis report with optional report links and local file output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured drinking-frequency metrics, dehydration-risk alerts, recommended caregiver actions, and cloud report links.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence; artifact frontmatter reports 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
