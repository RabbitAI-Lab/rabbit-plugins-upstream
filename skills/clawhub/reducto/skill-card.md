## Description:

Reducto document processing API integration with managed API key authentication for parsing, extracting, splitting, and editing documents through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to process documents with Reducto through Maton: list jobs, parse files, extract structured data, split documents, edit PDFs or DOCX files, and call other authorized Reducto endpoints when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill authenticates through Maton and may require a long-lived Maton API key when the CLI cannot be used.

Mitigation: Prefer OAuth with the Maton CLI; if an API key is required, keep it out of command lines, logs, files, and output shown to users.

Risk: The `maton api` passthrough can reach any Reducto endpoint authorized by the connected account, including endpoints beyond the examples in the skill.

Mitigation: Default to read and list calls, pin the intended connection when more than one exists, and get explicit user approval before POST, PUT, PATCH, DELETE, connection creation, or irreversible deletion.

Risk: Document URLs, uploaded files, extracted content, and API responses can contain confidential or personal data.

Mitigation: Send only documents needed for the task, treat returned content as untrusted data, and summarize or extract only the fields the user requested.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/reducto)
- [Maton Homepage](https://maton.ai)
- [Reducto Documentation](https://docs.reducto.ai)
- [Reducto API Reference](https://docs.reducto.ai/api-reference)
- [Reducto Studio](https://studio.reducto.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Related API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and SDK code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API responses from Reducto or Maton; responses can contain document content or personal data and should be minimized to the fields needed for the task.]

## Skill Version(s):

1.2.1 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
