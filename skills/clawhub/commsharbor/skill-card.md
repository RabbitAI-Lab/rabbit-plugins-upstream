## Description:

Inspect domain email setup and authorized email workspaces with CommsHarbor.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wrpbr](https://clawhub.ai/user/wrpbr)

### License/Terms of Use:

MIT-0

## Use Case:

People with authorized organization access use this skill to inspect email workspace information and find existing domain setup in CommsHarbor.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private workspace information could be accessed without appropriate authority.

Mitigation: Use only an organization ID and API key for an organization the requester is authorized to access; confirm authority before any write.

Risk: Organization API keys or mailbox passwords could be exposed in conversation.

Mitigation: Keep API keys in client secret storage and never include keys or mailbox passwords in responses.

## Reference(s):

- [CommsHarbor API contract](https://commsharbor.com/llms.txt)
- [CommsHarbor ClawHub release](https://clawhub.ai/wrpbr/skills/commsharbor)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Describes authorized workspace and domain setup information; does not include secrets in responses.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
