## Description:

Analyzes fixed-camera video of an older adult's water-cup area to count cup-pickup events, report drinking-frequency metrics, and flag dehydration-risk reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers, family members, nursing-home staff, and health-management platform operators use this skill to analyze home-care or facility video for cup-pickup frequency, long gaps between drinking events, and daily reminder reports. The output is a visual behavior signal for follow-up and should not be treated as a medical diagnosis or proof of actual fluid intake.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Home-care video and health-analysis reports may be sent to or retrieved from external services.

Mitigation: Use the skill only with informed consent from the monitored person or legal guardian, and only with trusted backend storage, transport, and report-access controls.

Risk: The skill silently manages account identity, persists tokens, and can retrieve historical reports with limited user-visible control.

Mitigation: Review identity handling and token storage before deployment, restrict installation to trusted environments, and audit who can access report history.

Risk: Cup-pickup frequency is only an indirect proxy for hydration and may be affected by empty cups, other people using the cup, camera framing, or behavior outside the monitored area.

Mitigation: Treat alerts as prompts for caregiver follow-up, combine them with personal baseline and context, and seek medical care when low intake or symptoms persist.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-elderly-drinking-frequency-analysis)
- [API interface documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON reports with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes cup-pickup counts, suspected drinking gestures, interval metrics, risk type, risk level, reminder text, recommended action, and report links when available.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter says 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
