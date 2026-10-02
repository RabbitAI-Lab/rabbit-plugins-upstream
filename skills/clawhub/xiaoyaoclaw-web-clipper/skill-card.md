## Description:

Clips user-selected public web pages into local Markdown files with source metadata, with batch clipping and URL deduplication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT

## Use Case:

People and developers use this skill to save explicitly requested web pages as searchable local Markdown, individually or in batches, for later reference or knowledge-base indexing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Clipped web content may contain misleading instructions for an agent that later reads it.

Mitigation: Treat saved Markdown as untrusted reference material, not instructions to execute.

Risk: Clipping makes external requests and persists page content and an index locally.

Mitigation: Run only for pages the user intends to save and use a dedicated clippings directory.

Risk: Installing or updating parsing dependencies can change the runtime environment.

Mitigation: Install from the bundled requirements.txt when possible.

## Reference(s):

- [OpenClaw Web Clipper on ClawHub](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-web-clipper)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [Local Markdown files with YAML frontmatter and CLI status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Maintains a local URL-deduplication index alongside saved clippings.]

## Skill Version(s):

1.0.6 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
