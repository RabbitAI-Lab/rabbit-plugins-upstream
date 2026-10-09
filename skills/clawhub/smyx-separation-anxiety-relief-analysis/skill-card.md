## Description:

Analyzes footage of pets left alone for separation-anxiety behaviors and provides observations, severity guidance, comfort suggestions, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and boarding staff use the skill to review footage of pets alone, identify possible anxiety-related behavior, and consider comfort measures or professional follow-up. It can also retrieve historical cloud reports; its observations are not a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Indoor pet-camera footage is sent to the vendor's cloud service for analysis.

Mitigation: Review the vendor's privacy terms and data retention before submitting home footage; share only footage you are comfortable sending.

Risk: The skill can automatically create or reuse a local identity and register or log in remotely.

Mitigation: Review the vendor's account practices and account cleanup path before installation.

Risk: Session tokens are persisted locally.

Mitigation: Limit access to the device and review how stored tokens are protected and removed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-separation-anxiety-relief-analysis)
- [Skill API reference](references/api_doc.md)
- [Skill usage introduction](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured report or JSON-formatted text; optional saved result file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include behavior observations, comfort suggestions, historical report links, and severity indications; not a medical diagnosis.]

## Skill Version(s):

1.0.11 (source: ClawHub release; artifact frontmatter says 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
