## Description:

Brief Yourself builds and applies a user-calibrated Personal Context for a person through bounded interviews, explicit source authorization, frozen task views, and reviewed patches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bagel-ew](https://clawhub.ai/user/bagel-ew)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and their agents use this skill to build, update, inspect, export, and apply a purpose-bound personal profile before tasks such as job search, writing, speaking, collaboration, or decision support. It is intended for user-controlled context sharing, not automated high-impact decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill manages sensitive personal-context data that may include private or restricted profile details.

Mitigation: Review each source authorization and avoid private, restricted, or downstream-persistent export options unless the user has deliberately approved the exact purpose and audience.

Risk: Unreviewed observations or inferences could misrepresent the user if treated as confirmed facts.

Mitigation: Keep new insights as candidate Claims or pending Patches until the user confirms, corrects, rejects, or leaves them unresolved.

Risk: Personal Context could be misused for employment, credit, insurance, medical, or other high-impact automated decisions.

Mitigation: Do not use the profile to make or rank high-impact decisions without explicit authorization and human review.

Risk: Exports, Views, or purge operations can create copies whose deletion boundaries may differ from the Personal Context Store.

Mitigation: State where outputs are saved, keep Views purpose-bound and time-limited, and distinguish controllable local copies from original or external systems during deletion.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/bagel-ew/skills/brief-yourself)
- [Server-Resolved GitHub Source](https://github.com/Bagel-EW/brief-yourself/tree/main/skills/brief-yourself)
- [Context View And Patch Protocol](references/context-view-and-patch.md)
- [Harness Memory, Personal Context, And Task Context Boundaries](references/harness-boundaries.md)
- [Interview And Calibration](references/interview-and-calibration.md)
- [Personal Context Model](references/personal-context-model.md)
- [Source Consent And Disclosure](references/source-consent-and-disclosure.md)
- [Store Operations](references/store-operations.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON with optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Human Briefs, candidate Claims, Tensions, Unknowns, frozen Context Views, pending Context Patches, and local store operation guidance.]

## Skill Version(s):

0.1.0 (source: server release evidence; display name references Brief Yourself 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
