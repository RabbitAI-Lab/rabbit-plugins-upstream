## Description:

Connects agents to Revdoku for private cloud file storage, bucket-based incoming email, sharing, and file management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[emirn](https://clawhub.ai/user/emirn)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents with authorized Revdoku accounts use this skill to upload and manage files in shared buckets, receive and read bucket email, and coordinate access to stored content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploading the wrong local files can disclose their contents to an authorized bucket.

Mitigation: Review upload paths and intended bucket access before uploading.

Risk: Archiving, restoring, or permanently deleting bucket data can have high impact.

Mitigation: Obtain explicit approval for each archive, restore, or delete action.

Risk: Local sign-in credentials are stored under ~/.revdoku.

Mitigation: Protect local credentials and connect only to an account you intend the agent to access.

## Reference(s):

- [Revdoku](https://revdoku.com)
- [Revdoku API documentation](https://revdoku.com/api.md)
- [ClawHub skill release](https://clawhub.ai/emirn/skills/revdoku)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain text and structured JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bucket identifiers, file paths, incoming-email addresses, and dashboard links.]

## Skill Version(s):

1.0.497 (source: ClawHub release and VERSION file)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
