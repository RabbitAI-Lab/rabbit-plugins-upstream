## Description:

Analyzes child nighttime sleep video and audio to report rollover, crying, sleep-talk, body-jerk, sleep-quality, and possible nightmare or restless-sleep alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and caregivers can use this skill to analyze child bedroom sleep media, generate sleep-behavior reports, and receive non-diagnostic alerts about possible nightmares or restless sleep.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive child bedroom audio/video and sleep-report history are sent to configured lifeemergence cloud services.

Mitigation: Use only with guardian consent, confirm the provider's retention, deletion, and access policies, and avoid inputs that should not leave the user's environment.

Risk: The skill stores tokens locally and associates activity with cloud identities.

Mitigation: Treat the workspace data directory and smyx-api-key.txt as sensitive, restrict local access, and remove stored credentials when the skill is no longer needed.

Risk: Arbitrary media URLs may be retrieved by the external service.

Mitigation: Use only trusted media URLs and avoid links that could expose private, untrusted, or unintended content.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-nightmare-rollover-detection-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured analysis text with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write an optional result file when the user supplies an output path.]

## Skill Version(s):

1.0.5 (source: server release evidence; artifact SKILL.md frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
