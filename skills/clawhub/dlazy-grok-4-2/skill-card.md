## Description:

Generates text, answers questions, and supports reasoning through dLazy's hosted Grok 4.2 service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to generate text, answer questions, and reason over prompts via the dLazy-hosted Grok 4.2 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad chat and question-answering triggers may send prompts to an external service unexpectedly.

Mitigation: Invoke this skill explicitly and confirm that sending each prompt to dLazy is acceptable.

Risk: Prompts and any supplied local media files may be sent to dLazy; the text-versus-media documentation is inconsistent.

Mitigation: Avoid sensitive prompts or file paths unless external processing is approved, and check expected outputs before use.

Risk: The skill installs an external npm CLI for hosted API access.

Mitigation: Review the pinned CLI package before installation, especially before installing it globally.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-grok-4-2)
- [dLazy CLI project (linked in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [Text returned in a CLI JSON response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional asynchronous task ID; documented example shows an image despite the text-generation description.]

## Skill Version(s):

1.3.31 (source: server release; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
