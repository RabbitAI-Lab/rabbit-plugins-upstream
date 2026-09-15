## Description:

AI-powered enterprise bidding assistant for China government procurement and commercial projects, covering bid document analysis, strategy, drafting, compliance audit, and post-bid follow-up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gechengling](https://clawhub.ai/user/gechengling)

### License/Terms of Use:

MIT-0

## Use Case:

Business development, procurement, legal, and proposal teams use this skill to analyze China tender documents, plan bid strategy, draft bid materials, check disqualification risks, and prepare post-bid follow-up. It is an assistive workflow and final submissions should be reviewed by qualified staff.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Tender materials often contain confidential pricing, client, personnel, and technical information.

Mitigation: Sanitize or redact sensitive content before use and confirm the organization permits AI-assisted processing of the materials.

Risk: Generated bid, legal, regulatory, pricing, or compliance guidance may be incomplete or incorrect for a specific project.

Mitigation: Have qualified procurement, legal, or compliance staff verify outputs before relying on them in a bid or post-bid action.

Risk: Installing an unpinned or unexpected package version can introduce unreviewed upstream changes.

Mitigation: Install the reviewed version explicitly and run installation from a trusted source or isolated low-privilege environment where practical.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gechengling/skills/tender-bidding-assistant)
- [ClawHub publisher profile](https://clawhub.ai/user/gechengling)
- [Artifact skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with tables, checklists, templates, inline shell commands, and draft bid document sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May analyze uploaded or pasted tender materials; generated bid, legal, regulatory, pricing, and compliance content requires qualified human review.]

## Skill Version(s):

3.2.2 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
