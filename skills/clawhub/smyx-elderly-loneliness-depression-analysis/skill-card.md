## Description:

Analyzes fixed-camera home video of older adults living alone to report behavior indicators associated with loneliness or depression tendency, including dazing, sighing, and self-talking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to invoke a cloud-backed video analysis workflow for solo-living elder care scenarios, producing behavior statistics, emotional-risk level prompts, suggested follow-up actions, and report links for family members or community workers. The skill is framed as behavioral risk support and not as a medical diagnosis or psychological scale.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Home-camera video and mental-health-related inference can expose highly sensitive personal information.

Mitigation: Use the skill only with explicit informed consent from the elder, minimize retained media, secure stored reports, and prefer privacy-preserving modes such as body outline or face masking when available.

Risk: The workflow contacts cloud services and creates or reuses a local identity for report history.

Mitigation: Confirm the service operator, endpoint configuration, data retention expectations, and account/session handling before installation or production use.

Risk: Local persistence can retain identity values and remote account/session tokens.

Mitigation: Run the skill in an isolated workspace, restrict access to the workspace data directory, and remove or rotate stored credentials when the skill is no longer needed.

Risk: Behavioral risk prompts could be mistaken for a clinical diagnosis.

Mitigation: Present outputs as behavior statistics and care prompts only; route concerning cases to qualified medical or mental-health professionals.

## Reference(s):

- [Skill API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-loneliness-depression-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured report text, with optional report export links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save report output to a user-specified file; report history is retrieved from the configured cloud API.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter lists 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
