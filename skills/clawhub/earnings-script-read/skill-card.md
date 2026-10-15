## Description:

Turns a company's official earnings script into a labeled plan and spoken clip for each section, typically producing 8 to 20 earnings-read clips.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Company communications and investor-relations teams use this skill to plan and produce one voiced read per section of an existing official earnings script without inventing figures or commentary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorization gives this package a shared, full-scope Beatra device token beyond earnings narration.

Mitigation: Review Beatra account permissions and billing exposure before approving device authorization; install only if this access is acceptable.

Risk: The bundled client silently installs package updates by default.

Mitigation: Consider disabling automatic updates with the documented update command before routine use, and review new releases before enabling them again.

Risk: Voice cloning and speech generation consume credits, and actual charges can differ from initial estimates.

Mitigation: Confirm each paid stage and its live price before submission; track request IDs and check final task billing before reporting costs.

Risk: A cloned voice or inaccurate reading could misrepresent a company's official remarks.

Mitigation: Use only an authorized voice sample and the supplied official script; verify names, figures, and pronunciation before delivery.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/earnings-script-read)
- [Earnings script voice workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Markdown with a labeled clip plan and links to generated audio]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically 8 to 20 clips; voice cloning and speech generation require separate paid approvals.]

## Skill Version(s):

0.2.0 (source: server-resolved ClawHub release and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
