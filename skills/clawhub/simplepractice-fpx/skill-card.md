## Description:

Reads SimplePractice Client Portal data from a shell with curl, including appointments, billing documents, documents to sign, announcements, and practice or clinician information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically comfortable users use this skill to read their own SimplePractice Client Portal records from scripts or machines where the MCP server is not installed. It focuses on read-only access to authenticated portal data and avoids portal writes such as payments, cancellations, or signed-document submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles medical, billing, session, and document data from a SimplePractice portal.

Mitigation: Use it only on trusted personal machines, keep cookies and downloaded records out of git and logs, and avoid shared terminals.

Risk: Magic-link tokens and session cookies provide authenticated portal access.

Mitigation: Treat copied tokens and cookie jars as credentials, restrict cookie jar permissions, and re-check the target practice host before running commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/simplepractice-fpx)
- [SimplePractice Client Portal request reference](artifact/references/requests.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON:API request notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only portal workflows; users supply their own practice host, session cookie, and portal credentials.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
