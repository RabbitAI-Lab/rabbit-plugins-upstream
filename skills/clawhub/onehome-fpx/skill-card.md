## Description:

Query OneHome (CoreLogic) from a shell with the fpx CLI to resolve consumer scope, search shared listings, and read listing details through one-shot GraphQL calls routed through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and authorized OneHome users use this skill to configure fpx, obtain a session bearer from their own OneHome magic link or signed-in browser tab, and query shared property listings, listing details, photos, and location data from scripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to capture and reuse live OneHome session bearer tokens, magic-link tokens, Authorization headers, and sessionToken values.

Mitigation: Treat those values as passwords, avoid placing them in shared logs, transcripts, screenshots, or persistent files, and prefer owner-only temporary files or in-memory handling.

Risk: The examples can create temporary files containing authentication material, including /tmp/checktoken*.json.

Mitigation: Delete temporary token files after use and avoid running the workflow on shared machines unless file permissions and cleanup are controlled.

Risk: The workflow queries OneHome data through a signed-in browser session and may encounter agent-only operations that return access errors for consumer-share sessions.

Mitigation: Use only sessions and listings the user is authorized to access, prefer consumer-readable saved-search queries first, and check GraphQL errors before relying on results.

## Reference(s):

- [OneHome GraphQL + REST operations for fpx](references/graphql-operations.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Code]

**Output Format:** [Markdown with shell, GraphQL, and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes fpx setup commands, token acquisition flows, GraphQL operation bodies, REST examples, and jq post-processing snippets.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
