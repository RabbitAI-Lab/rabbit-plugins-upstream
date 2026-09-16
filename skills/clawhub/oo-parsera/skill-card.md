## Description:

Parsera (parsera.org) routes search, extraction, Markdown conversion, and parsing requests through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Parsera through an OOMOL-connected account, extracting structured data or clean Markdown from webpage URLs and parsing structured attributes from provided HTML or text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes direct remote installer execution for the oo CLI.

Mitigation: Review the installer source or prefer an official package manager or verified installer path before running first-time setup commands.

Risk: Parsera inputs are sent through OOMOL as the connector service.

Mitigation: Submit only the webpage content, prompts, and attributes needed for extraction; avoid secrets or unrelated private content in payloads.

## Reference(s):

- [Parsera homepage](https://parsera.org)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected as JSON with data and meta.executionId fields.]

## Skill Version(s):

1.0.4 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
