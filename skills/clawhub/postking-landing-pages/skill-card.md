## Description:

Generate, edit, vibe-edit, and publish landing pages on PostKing, including comparison/side pages and custom domains, for launches and campaigns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bitsandtea](https://clawhub.ai/user/bitsandtea)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams, founders, and operators use this skill to create, revise, preview, translate, and publish PostKing landing pages and related side pages for launches and campaigns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents to publish or unpublish public pages.

Mitigation: Confirm the exact page slug, preview or live URL, and publication consequence with the user before changing public state.

Risk: The skill can guide destructive actions such as deleting versions, landing pages, domains, or blocks.

Mitigation: Require explicit confirmation for the target object and action, and prefer inspecting available versions or current state before deletion.

Risk: Renaming a side page changes the live URL and the old URL returns 404 with no redirect.

Mitigation: Warn the user before renaming a published side page and confirm whether reference rewriting should be enabled.

Risk: Importing external pages can bring outside content into a PostKing side page workflow.

Mitigation: Confirm the source URL or supplied HTML and intended destination side-page slug before external import.

Risk: Custom-domain support through the skill stops at registration and verification for landing pages.

Mitigation: Tell the user to complete landing-page domain attachment in the PostKing dashboard after MCP or CLI verification.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bitsandtea/skills/postking-landing-pages)
- [Hosted PostKing MCP endpoint](https://mcp.postking.app/mcp)
- [Skill icon asset](https://raw.githubusercontent.com/bitsandtea/postking-skills/main/assets/icons/postking-landing-pages.svg)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Shell commands, Configuration instructions, API Calls]

**Output Format:** [Markdown guidance with tool-call descriptions and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents through asynchronous polling, draft review, publication, version restore, domain registration, and side-page workflows.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
