## Description:

Triage a batch of the user's email against their personal knowledge wiki and return verdicts that the server resolves into auto-ingest, review, or discard outcomes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samuel-wei](https://clawhub.ai/user/samuel-wei)

### License/Terms of Use:

MIT-0

## Use Case:

External HiJavis users use this skill to review recent Gmail threads against their personal knowledge wiki, request limited message bodies when metadata is insufficient, and submit one verdict per candidate for server-side handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads Gmail metadata and can request full message bodies for selected threads.

Mitigation: Install only when read-only Gmail access for daily or on-demand triage is acceptable; the artifact limits body reads to staged threads and a maximum of 12 per run.

Risk: A shared gateway bearer token may be sent to an environment-configured server URL.

Mitigation: Pin or validate the server URL before attaching the gateway token, as recommended by the security guidance.

Risk: The local run-state file briefly stores email subjects and senders.

Mitigation: Harden state file permissions and cleanup behavior; the artifact states that message bodies are not written to this state file.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/samuel-wei/skills/gmail-wiki-ingest)
- [HiJavis iPhone app](https://apps.apple.com/us/app/hijavis/id6745134765)
- [The judgment rubric](artifact/rubric.md)
- [Server endpoint contract](artifact/references/tool-contract.md)
- [Trigger contract](artifact/references/trigger-contract.md)
- [Banding and trust reference](artifact/references/banding-and-trust.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON command payloads and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches Gmail thread metadata, may request bodies for up to 12 staged threads per run, submits verdict JSON, and reports a short markdown digest.]

## Skill Version(s):

0.5.0 (source: server release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
