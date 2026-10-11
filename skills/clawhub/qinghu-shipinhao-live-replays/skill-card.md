## Description:

Retrieves WeChat Channels live replay listings for an account to support streaming-frequency and replay-content analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and creators use this skill to retrieve an account's WeChat Channels live replay history and assess streaming frequency or identify replay material.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or upgrading runtime tools may run unreviewed third-party code.

Mitigation: Use a trusted installation path and review the Qinghu qhkit package before installing; avoid unpinned latest or npx execution where possible.

Risk: Configuring an account token can expose credentials to the installed package or persistent storage.

Mitigation: Only provide a token to software you trust; use a scoped environment variable or managed secret instead of persistent storage when available.

Risk: Replay queries consume paid Qinghu credits.

Mitigation: Check the estimated cost and obtain user consent before paid calls; report the actual credits consumed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-shipinhao-live-replays)
- [Qinghu qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise analysis with a replay preview and a table file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Replay listings can be paginated; reported usage includes Qinghu credit consumption.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
