## Description:

Prepare BrewPage drafts, publish supplied content or new pages, and update a specific publication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kochetkov-ma](https://clawhub.ai/user/kochetkov-ma)

### License/Terms of Use:

MIT

## Use Case:

OpenClaw users can prepare BrewPage content locally, publish pages or files, and update an existing publication. It supports hosted sites, visitor response forms, and custom domains when the requested workflow and owner access allow them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan flags ownership recovery and reconciliation workflows beyond the stated publishing purpose, and reports that its scan was incomplete.

Mitigation: Review the ownership and recovery behavior and confirm the required host permissions before installing; treat the skill as unverified until the remaining components are inspected.

## Reference(s):

- [BrewPage](https://brewpage.app)
- [ClawHub release page](https://clawhub.ai/kochetkov-ma/skills/brewpage-publish)
- [Publishing guide](references/publishing.md)
- [Ownership and receipts](references/ownership.md)
- [Page data guide](references/page-data.md)
- [Custom domains guide](references/custom-domain.md)
- [BrewPage hosting API](https://brewpage.app/api#hosting)

## Skill Output:

**Output Type(s):** [Files, Markdown, HTML, JSON, Guidance]

**Output Format:** [Local content artifacts and concise text describing a confirmed publication or update]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The output depends on the request and may be a local draft or a confirmed reader link with publication status.]

## Skill Version(s):

1.1.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
