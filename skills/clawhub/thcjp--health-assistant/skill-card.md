## Description:

健康指导助手 provides personalized wellness guidance with safety boundaries, evidence-level framing, baseline tracking, behavior-change support, and professional referral prompts without diagnosing, treating, or prescribing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users can ask an agent for wellness guidance that emphasizes non-diagnostic advice, individualized baselines, evidence distinctions, gradual habit changes, progress tracking, and referral to qualified medical or mental-health professionals when appropriate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive health information may be exposed because privacy and retention boundaries are unclear.

Mitigation: Avoid entering unnecessary medical details and require publisher documentation for data retention, callback handling, and privacy controls before deployment.

Risk: Broad read, write, and exec permissions could allow behavior beyond text-only wellness guidance.

Mitigation: Run with least-privilege tool access, disable command and file permissions unless required, and review any proposed file, shell, API, or callback actions before execution.

Risk: Wellness guidance can be mistaken for medical diagnosis, treatment, prescription, or mental-health care.

Mitigation: Keep responses non-diagnostic, cite evidence strength where possible, and direct persistent symptoms, concerning changes, medication questions, and serious mental-health concerns to qualified professionals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/health-assistant)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, shell commands, configuration]

**Output Format:** [Markdown or plain text wellness guidance, with shell commands only for environment configuration when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May ask for user context such as goals, symptoms, sleep, stress, medication considerations, and progress signals; should avoid collecting unnecessary sensitive health details.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter lists 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
