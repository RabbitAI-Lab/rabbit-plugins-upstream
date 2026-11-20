## Description:

Drafts locally, publishes HTML, Markdown, JSON, files, forms, and built sites to BrewPage, and updates existing publications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kochetkov-ma](https://clawhub.ai/user/kochetkov-ma)

### License/Terms of Use:

MIT

## Use Case:

OpenClaw users can prepare BrewPage content locally, publish or update pages and files, and manage access to anonymous publications. Review the requested content and audience before publishing, especially when a page collects visitor responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports a benign verdict with medium confidence and partial inspection; this does not establish that the artifact is risk-free.

Mitigation: Consider whether the publishing capabilities and undeclared tool scope fit your needs, and review the requested action and target before publishing.

Risk: An unlisted publication can be opened by anyone with its link, while eligible public publications can appear in the gallery and sitemap.

Mitigation: Choose the access level deliberately and keep confidential or limited-audience content out of public discovery.

Risk: Anonymous publication receipts may contain a private owner key or management link that can enable later edits or deletion.

Mitigation: Keep owner proof and management links in protected private storage or an owner-only channel.

## Reference(s):

- [BrewPage](https://brewpage.app)
- [BrewPage hosting API](https://brewpage.app/api#hosting)
- [BrewPage Page Data guide](https://brewpage.app/llms-page-data.txt)
- [OpenClaw skills documentation](https://docs.openclaw.ai/tools/skills)
- [Publishing workflow](artifact/references/publishing.md)
- [Ownership and receipts](artifact/references/ownership.md)
- [Page data reference](artifact/references/page-data.md)

## Skill Output:

**Output Type(s):** [Files, HTML, Markdown, JSON, Shell commands, Configuration instructions, Publishing guidance]

**Output Format:** [Local files and concise Markdown guidance; publishing results may include a reader URL and receipt details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can prepare drafts locally or perform a requested publication or update; output depends on the requested content and access settings.]

## Skill Version(s):

1.1.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
