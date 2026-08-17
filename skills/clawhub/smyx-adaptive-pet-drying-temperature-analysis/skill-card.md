## Description:

This skill analyzes full-body pet images or videos through external APIs to estimate breed or body type and fur density, then returns a drying temperature and time curve for grooming or smart drying devices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet grooming operators, smart pet-care device teams, and agents assisting pet owners use this skill to submit pet media and receive a non-medical drying temperature curve, structured report, and report link.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends pet media or media URLs to external lifeemergence.com services.

Mitigation: Use only with media the user is allowed to share externally, and disclose external processing before deployment.

Risk: The skill silently creates or reuses an identity and can query cloud history associated with that identity.

Mitigation: Confirm that identity handling and cloud history access match the deployment's privacy and account policies.

Risk: Authentication tokens may be stored in a workspace SQLite database.

Mitigation: Restrict workspace access, rotate tokens when needed, and remove local token stores when uninstalling or transferring the skill.

Risk: Drying recommendations could be unsafe if treated as medical or veterinary advice.

Mitigation: Present recommendations as grooming-device guidance only, keep conservative temperature limits, and require human review for young, senior, flat-faced, or vulnerable pets.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Common AI analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report text with optional JSON detail and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include drying temperature and time curve values, pet type context, analysis status, and cloud report links.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
