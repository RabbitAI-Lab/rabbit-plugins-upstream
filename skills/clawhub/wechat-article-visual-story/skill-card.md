## Description:

Write the WeChat article and make its pictures in one pass from a topic, promotion details, and audience, returning feed-oriented title candidates, a digest line, a phone-readable article body, a 2.35:1 cover, and matching in-body images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Content marketers, founders, operators, and editorial teams use this skill to draft WeChat Official Account articles and generate the cover plus in-body image set in one coordinated workflow. It is intended for brand, product, promotional, expert-column, and case-study posts where the writing and visuals need to be planned together.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad Beatra account authority, including spending-capable and multi-media MCP access.

Mitigation: Review the Beatra approval page before authorizing and install only when that account scope is acceptable for the intended user and workspace.

Risk: A shared Beatra device bearer credential is stored locally for this and other Beatra skills.

Mitigation: Protect the local credential file, avoid exposing tokens in prompts or logs, and use the bundled uninstall flow or Beatra Console revocation when access should be removed.

Risk: Brand references and private article content may be uploaded to an external service for generation or transformation.

Mitigation: Do not upload confidential campaign material, customer data, or protected brand assets unless external processing by Beatra is approved.

Risk: Image generation and transformation can spend Beatra credits.

Mitigation: Confirm every paid image request, keep stable request IDs, and report only task-returned billing facts such as net charged credits.

Risk: Silent package updates are enabled by default.

Mitigation: Disable automatic updates with scripts/mcp_client.py update --auto off when change control or review is required before package replacement.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/wechat-article-visual-story)
- [Beatra skill homepage](https://beatra.ai/skills/wechat-article-visual-story)
- [Writing the article](references/article-craft.md)
- [Planning the images](references/visual-set.md)
- [Article workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Shell commands, Guidance]

**Output Format:** [Markdown with generated article copy, image placement notes, task identifiers, artifact links, dimensions, model details, and billing facts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke paid Beatra image generation or transformation calls after user approval; generated media and billing details are reported from task results.]

## Skill Version(s):

0.1.5 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
