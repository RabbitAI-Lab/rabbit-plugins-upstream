## Description:

Call third-party APIs through the Maton gateway, which injects the credential for an app the user has already connected.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to route approved agent requests through Maton's gateway to connected third-party apps, inspect data, update app resources, manage connections, and configure functions or event triggers when explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify or delete data in connected third-party apps.

Mitigation: Start with read-only calls and require explicit approval for every POST, PUT, PATCH, or DELETE, including the exact app, account, target, payload, and intended effect.

Risk: High-impact operations such as bulk email, public posting, billing actions, deletion, functions, webhooks, and trigger destinations can create broad side effects.

Mitigation: Treat these as elevated-risk actions and obtain separate, specific confirmation before proceeding.

Risk: Trigger destinations can persistently forward future event payloads to an external URL.

Mitigation: Confirm the destination URL, controller, event data, persistence, and any credentials before creation, then review and delete destinations that are no longer needed.

Risk: Local --exec handlers run local code on third-party event data.

Mitigation: Use only user-authored or user-reviewed handlers, scope them narrowly, and get separate approval before starting a long-running watch.

## Reference(s):

- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/api-gateway)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, code blocks, API paths, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Maton CLI commands, raw HTTPS examples, connection identifiers, function snippets, trigger setup steps, and approval prompts.]

## Skill Version(s):

1.2.19 (source: server release evidence, created 2026-09-14T07:17:48Z; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
