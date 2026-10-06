## Description:

Analyzes fixed-camera video of an older person's cup area to count cup pickups and provide indicative dehydration-risk reminders and historical reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Families, caregivers, and elder-care providers use footage from a fixed camera near a drinking cup to review pickup frequency, receive low-frequency reminders, and view past reports. Cup pickups are only an indirect measure of drinking, not a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private elder-care footage and analysis or history requests are sent to cloud services.

Mitigation: Obtain clear consent from the monitored person or legal representative, and review the remote service's privacy and data-handling practices before use.

Risk: The skill silently creates or reuses a cloud identity and stores returned tokens in a local workspace database.

Mitigation: Review the account-linking model before installation and restrict access to the workspace and its stored credentials.

Risk: Cup-pickup frequency may be mistaken for actual water consumption or a clinical dehydration diagnosis.

Mitigation: Treat reminders as prompts for a caregiver to check in, not as evidence of intake or a medical diagnosis.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-elderly-drinking-frequency-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [JSON analysis results or Markdown report links and history tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes cup-pickup counts, indicative risk reminders, and links to historical reports; results may also be saved to a file.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata; bundled SKILL.md states 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
