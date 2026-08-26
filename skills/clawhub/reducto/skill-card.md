## Description:

Reducto document processing API integration with managed API key authentication for parsing, extracting, splitting, and editing documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to process documents through Reducto via Maton, including parsing content, extracting structured data, splitting documents into sections, and editing PDFs or DOCX files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documents sent through this skill may be processed by Maton and Reducto services.

Mitigation: Use the skill only for documents intended for those services, and review the connected Reducto account before processing.

Risk: Uploads, document edits, connection creation, and other mutating API calls can change account state or expose document contents.

Mitigation: Require explicit user confirmation before uploads, edits, connection creation, POST, PUT, PATCH, or DELETE operations.

Risk: Authentication credentials or provider-issued tokens may be exposed if printed, logged, stored, or passed on command lines.

Mitigation: Use Maton OAuth or credential-store handling where available, avoid printing or persisting secrets, and send fallback API keys only through stdin-based request configuration.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/reducto)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Reducto Documentation](https://docs.reducto.ai)
- [Reducto API Reference](https://docs.reducto.ai/api-reference)
- [Reducto Studio](https://studio.reducto.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent guidance for Maton CLI and SDK calls; API responses may include document text, structured JSON, job identifiers, URLs, usage data, and edited document links.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
