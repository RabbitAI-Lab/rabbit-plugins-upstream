## Description:

Analyzes fixed-camera video and optional audio from dementia-care environments to identify confusion or disorientation signals and produce structured orientation-soothing reports and actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Care teams, facility operators, and developers use this skill to analyze dementia-care media or URLs for confusion and disorientation events, generate structured reports, query report history, and coordinate gentle orientation cues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dementia-care audio, video, URLs, and report queries may be sent to the publisher's cloud service.

Mitigation: Install only in deployments with documented consent, opt-out, retention, and caregiver authorization controls.

Risk: The skill can silently create or reuse a persistent local/default account identity and link future reports to that identity.

Mitigation: Review identity handling before deployment and ensure stored tokens and report linkage match the deployment's privacy policy.

Risk: The skill operates in a sensitive care setting where incorrect or overbroad use could affect vulnerable people.

Mitigation: Use outputs as behavioral monitoring and orientation-support guidance, with caregiver review and without treating results as a medical diagnosis.

## Reference(s):

- [API Interface Documentation](artifact/references/api_doc.md)
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-dementia-confusion-orientation-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown text with structured JSON report content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can analyze local media paths or URLs, query historical reports, and optionally write results to an output file.]

## Skill Version(s):

1.0.5 (source: server release metadata; artifact frontmatter and changelog mention 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
