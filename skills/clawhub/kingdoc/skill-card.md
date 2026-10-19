## Description:

Helps users create, edit, search, and manage Kingsoft Docs documents through natural-language requests and local document tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and teams use KingDoc to draft local documents, work with cloud documents and spreadsheets, search content, manage versions and sharing, and review document compliance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sharing an App Secret in chat may expose credentials with broad document access.

Mitigation: Never paste production App Secrets into chat; use a least-privilege test app and keep secrets in a secure credential store.

Risk: Deletion, permanent deletion, version restoration, and permission changes can have high-impact consequences without enforceable approval gates.

Mitigation: Require independent manual confirmation of the exact target and operation before allowing these actions.

Risk: Webhook processing, memory bridging, and local indexing may expose or propagate document data.

Mitigation: Review the data and intended recipients, limit access to necessary documents, and manually approve these features before use.

## Reference(s):

- [KingDoc on ClawHub](https://clawhub.ai/fyniujin/skills/kingdoc)
- [Kingsoft Docs developer documentation](https://developer.kdocs.cn)
- [KingDoc authentication guidance](artifact/references/auth.md)
- [KingDoc workflows](artifact/references/workflows.md)
- [KingDoc security guidance](artifact/references/security.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance]

**Output Format:** [Natural-language responses and structured tool results; local document files and cloud document changes when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cloud document operations require Kingsoft Docs app credentials; local document generation can work without them.]

## Skill Version(s):

4.3.5 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
