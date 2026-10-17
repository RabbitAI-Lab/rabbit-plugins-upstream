## Description:

Analyzes pet monitoring media through a cloud service and returns behavior reports and report links, but does not activate soothing devices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and caregivers can submit pet monitoring media for cloud-based behavior analysis and retrieve structured reports or past report links. The skill does not control soothing devices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media or media URLs are sent to a remote service and may contain sensitive household footage.

Mitigation: Review cloud-processing terms and avoid submitting sensitive household footage without consent.

Risk: The skill may automatically create or reuse an identity and persist authentication tokens locally.

Mitigation: Review identity association and local credential storage before installation, and protect the machine running the skill.

Risk: The advertised automatic soothing-device trigger is not implemented.

Mitigation: Treat the results as analysis only; use a separately verified integration for device control.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-pet-calming-trigger-analysis)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Structured text or Markdown with report links; optionally saved to a file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can list historical cloud reports; does not actuate soothing devices.]

## Skill Version(s):

1.0.18 (source: server-resolved ClawHub release; bundled frontmatter says 1.0.22)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
