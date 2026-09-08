## Description:

Enables an agent to use the 2Ryun REST API for document management, knowledge-base search, webpage generation, publishing, notes, and attachments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iguoguo](https://clawhub.ai/user/iguoguo)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent users use this skill to connect an agent to 2Ryun for importing documents, deciding what enters the knowledge base, searching structured knowledge, generating Markdown-based webpages, publishing pages, and managing lightweight notes or attachments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can change, delete, upload, index, and publicly publish user content in 2Ryun.

Mitigation: Use a narrowly scoped API key and require explicit user confirmation before destructive actions, sensitive imports or uploads, sharing, or publishing public pages.

Risk: Default full read/write API-key permissions can expose more 2Ryun content and actions than a task requires.

Mitigation: Create a task-specific API key with only the needed module permissions, such as documents, wiki, gen-html, note, attachments, or users.

Risk: Generated reports or summaries derived from existing knowledge can be re-indexed as new knowledge if the agent sets extraction incorrectly.

Mitigation: Confirm whether content is new knowledge before enabling wiki extraction, and keep derived content out of the knowledge base.

Risk: Published webpages and uploaded asset URLs may become publicly reachable without an API key.

Mitigation: Review generated HTML and asset choices with the user before publishing, and unpublish or delete content that should not remain public.

## Reference(s):

- [Server-resolved source repository](https://github.com/iguoguo/2Ryun-skill)
- [ClawHub skill page](https://clawhub.ai/iguoguo/skills/2ryun-skill)
- [2Ryun API specification](artifact/2ryun-api-spec.md)
- [2Ryun platform](https://2ryun.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline curl commands, JSON payloads, and API-response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May result in API-created documents, notes, knowledge entries, generated HTML pages, public URLs, and uploaded attachments in the user's 2Ryun account.]

## Skill Version(s):

0.1.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
