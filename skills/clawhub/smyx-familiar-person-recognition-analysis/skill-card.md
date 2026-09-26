## Description:

Identifies enrolled acquaintances in images or videos by comparing face photos, then reports matched identities and locations for home or office identity-checking workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, or operators use this skill to analyze supplied images or videos against an enrolled face database, then review structured identity, location, and historical-report outputs for home or office monitoring scenarios.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Face images, surveillance videos, and reports may be sent to the configured cloud service and tied to an automatically managed local or remote identity.

Mitigation: Install and use only when users are comfortable with that data flow, have consent and authority for the people shown, and have reviewed local workspace data and cloud report history handling.

Risk: The scanner summary notes insufficient user-facing control or privacy disclosure for biometric analysis linked to identity and cloud history.

Mitigation: Confirm privacy notice, retention, access-control, and report-history expectations before using the skill in homes or offices.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-familiar-person-recognition-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured analysis reports, with shell-command examples and optional file output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires suitable image or video input, prior face enrollment, configured cloud API access, and consent or authority for people shown; results are reference-only and not legal identity verification.]

## Skill Version(s):

1.0.16 (source: server release metadata; artifact frontmatter states 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
