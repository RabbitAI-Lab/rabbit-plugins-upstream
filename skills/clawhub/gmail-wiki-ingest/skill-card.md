## Description:

Triage recent Gmail messages against a user's personal wiki, propose verdicts for what should be discarded, reviewed, or ingested, and send a brief digest back to HiJavis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samuel-wei](https://clawhub.ai/user/samuel-wei)

### License/Terms of Use:

MIT-0

## Use Case:

HiJavis users use this skill to turn durable personal correspondence into personal wiki candidates while filtering routine mail. The agent judges each offered thread using the bundled rubric, selected bounded email content, and the user's existing wiki context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles private Gmail metadata and can read selected message bodies during a run.

Mitigation: Use the HiJavis app switch to control whether ingest runs, and rely on the documented body-read bound of only server-offered threads with no body persistence in local run state.

Risk: A shared bearer token and configurable server endpoint could expose data if the runtime is misconfigured.

Mitigation: Lock JAVIS_SERVER_URL to the intended javis-server origin, prefer scoped credentials where available, and keep the local data directory private.

Risk: Email content can contain adversarial instructions that try to influence the agent's judgment.

Mitigation: Treat message content only as evidence, not instructions; server-side category gates, reference validation, score clamping, and user confirmation paths limit the impact of incorrect verdicts.

## Reference(s):

- [Judgment rubric](rubric.md)
- [Server endpoint contract](references/tool-contract.md)
- [Banding and trust reference](references/banding-and-trust.md)
- [Trigger contract](references/trigger-contract.md)
- [HiJavis iPhone app](https://apps.apple.com/us/app/hijavis/id6745134765)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown digest prose, JSON verdict payloads, and shell command invocations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches up to 50 metadata items and can request body text for at most 12 server-offered threads per run.]

## Skill Version(s):

0.5.1 (source: package.json and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
