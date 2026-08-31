## Description:

Find, compare, and add Notion Marketplace templates with linked free shortlists, explicit workspace selection, browser-driven duplication, and Notion API verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[patrick-erichsen-2](https://clawhub.ai/user/patrick-erichsen-2)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to discover suitable Notion Marketplace templates, compare free options, add a selected template to an explicit workspace, and verify the created page through the Notion API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can add a selected Notion template into a user-selected workspace.

Mitigation: Use it only with a Notion account and workspace where adding private pages is acceptable, and require explicit workspace selection before mutation.

Risk: Paid or ambiguously priced templates could create unintended spending or checkout actions.

Mitigation: Default to free-only results, include paid templates only after explicit opt-in, and require action-time confirmation naming the template and price before checkout.

Risk: A browser success state alone may not prove that the template was installed.

Mitigation: Verify installation through Notion API search and page fetch; if no new fetchable page appears, report browser success as unverified.

Risk: The browser workspace and the Notion API workspace may differ.

Mitigation: Stop before adding the template when the browser-selected workspace and API-verifiable workspace do not match, and ask the user to align them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/patrick-erichsen-2/skills/notion-marketplace)
- [Notion Marketplace categories](https://www.notion.com/templates/category)
- [Notion Marketplace app](https://app.notion.com/marketplace)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with linked shortlists and verification summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include selected template links, workspace and destination names, and Notion page URLs or IDs after API verification.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
