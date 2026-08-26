## Description:

Write the WeChat article and make its pictures in one pass, returning title candidates, a digest line, a phone-readable article body, a 2.35:1 cover, and a coordinated set of in-body images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and content teams use this skill to draft WeChat Official Account articles and generate matching cover and in-body images in one workflow. It is intended for promotional articles, product stories, columns, case studies, and other long-form posts where the writing and visuals need to be produced together.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores and uses a shared Beatra bearer credential with broad media and wallet-related scopes.

Mitigation: Use the bundled authorization flow only, keep the credential in the protected local Beatra state, and revoke or disconnect it when the installation is no longer trusted.

Risk: Silent automatic updates are enabled by default.

Mitigation: In restricted or enterprise environments, disable automatic updates with `python3 scripts/mcp_client.py update --auto off` and review updates before re-enabling them.

Risk: Image generation is paid work and duplicate submissions can create avoidable charges.

Mitigation: Require approval before paid calls, use one stable `client_request_id` per frozen request, poll existing task IDs, and retry only identical payloads under the same request identity.

Risk: The workflow can upload local reference media selected by the user.

Mitigation: Upload only files the user explicitly chooses and avoid placing credentials, private tokens, or unnecessary sensitive content in prompts, command arguments, or uploaded references.

## Reference(s):

- [Skill source](artifact/SKILL.md)
- [Writing the article](artifact/references/article-craft.md)
- [Planning the images](artifact/references/visual-set.md)
- [Article workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with code blocks, JSON request examples, shell commands, generated article text, image task details, and artifact links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces title candidates, digest copy, article body, image plans, Beatra image generation calls, task IDs, returned dimensions, and billing facts when available.]

## Skill Version(s):

0.1.3 (source: release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
