## Description:

Connects agents to Revdoku inboxes and shared cloud storage to read messages and files and perform authorized file and account operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[emirn](https://clawhub.ai/user/emirn)

### License/Terms of Use:

MIT-0

## Use Case:

People and developers use this skill to let an authorized agent receive and review inbox messages and attachments, manage shared files, and perform explicitly requested storage or account actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An overly broad folder selection may upload sensitive local files.

Mitigation: Select only authorized paths and review a dry-run before recursive uploads.

Risk: Account credentials and access to private inboxes or stored files expose sensitive information.

Mitigation: Grant only the access needed for the task and keep credentials and recovery messages private.

Risk: Permanent bucket deletion irreversibly removes stored files.

Mitigation: Review the exact account, bucket, and deletion preview; require explicit approval before confirming.

## Reference(s):

- [Revdoku homepage](https://revdoku.com)
- [Revdoku API documentation](https://revdoku.com/api.md)
- [Incoming email documentation](https://revdoku.com/api.md#incoming-email-into-a-bucket)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Text or Markdown with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include summaries of messages and stored files, selected file paths, and operation results.]

## Skill Version(s):

1.0.508 (source: server release and VERSION file)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
