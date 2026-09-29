## Description:

Analyzes pet-area UV disinfection video through a remote service and returns safety findings and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and facility staff use the skill to assess uploaded footage or video URLs for potential pet exposure during UV disinfection and to review past analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Claims of live protection and automatic UV lamp shutoff may give a false sense of safety.

Mitigation: Do not rely on the skill to switch off a lamp or provide live protection; verify lamp status and shut it off independently unless a device-control integration is verified.

Risk: Pet or household media and URLs are sent to a remote analysis service.

Mitigation: Obtain consent and review the destination and privacy implications before submitting media or URLs.

Risk: The skill may create or reuse a local account identity with stored tokens.

Mitigation: Review account and token handling before use and avoid running it with sensitive local credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-uv-safety-monitor-analysis)
- [UV safety monitor API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Text or Markdown with structured analysis results and report links; optional saved text file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports historical report listings and basic, standard, or JSON detail settings.]

## Skill Version(s):

1.0.10 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
