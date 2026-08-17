## Description:

This skill analyzes pet activity images or videos for over-excitement behaviors and returns a structured report with calming guidance for households, boarding centers, daycares, and training schools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze pet activity media, identify over-excitement indicators such as jumping, spinning, sprinting, and jumping on people, and receive behavior-safety guidance. The skill is intended for pet households, boarding centers, pet daycares, and dog training schools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet and home media may be processed by external cloud services.

Mitigation: Use only with media approved for cloud processing, and review the service's privacy, retention, billing, and account controls before deployment.

Risk: The skill creates or reuses an account-linked identifier and stores tokens locally.

Mitigation: Run it in a controlled workspace, restrict workspace sharing, and review local token storage before use with sensitive household, daycare, or boarding-center footage.

Risk: Cloud report history can be retrieved with limited user-facing consent.

Mitigation: Limit historical-report access to authorized users and confirm account controls before enabling report-history workflows.

Risk: Behavior guidance may be incomplete for medical or veterinary concerns.

Mitigation: Treat outputs as behavior-safety guidance only and escalate repeated or severe calming failures to a qualified behavior trainer or veterinarian.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-excitement-calming-guide-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown report text with optional JSON details and cloud report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include structured analysis results, behavior-safety recommendations, risk prompts, and history-report tables returned from cloud APIs.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
