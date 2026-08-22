## Description:

Integrate Dropbox Sign eSignature workflows through Pontx. Use for signature requests, templates, embedded signing, callbacks, test mode, document downloads, or HelloSign migrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pontjs](https://clawhub.ai/user/pontjs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and integration engineers use this skill to plan and review Dropbox Sign eSignature workflows through Pontx, including signature requests, templates, embedded signing, callbacks, test mode, document downloads, and HelloSign migrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys, callback payloads, signer data, documents, or signing URLs could be exposed through source code, command arguments, logs, callback dumps, or examples.

Mitigation: Keep credentials in an environment or credential manager, redact previews and logs, avoid printing sensitive files or URLs, and apply the approved access and deletion policy.

Risk: A real signature request, production send, or document download could happen before the workflow is approved.

Mitigation: Use dry-run previews first, require explicit approval before confirming unchanged requests, and re-preview when a document, signer, template, field, or option changes.

Risk: Unverified, duplicated, or out-of-order callbacks could drive incorrect workflow state or premature final-file downloads.

Mitigation: Verify callback HMACs before trusting event data, process callbacks idempotently, derive state from verified events, and wait for the downloadable event before fetching final files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pontjs/skills/pontx-dropbox-sign)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and code-oriented integration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Emphasizes dry-run previews, explicit approval before mutations, credential handling, callback verification, and document retention controls.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
