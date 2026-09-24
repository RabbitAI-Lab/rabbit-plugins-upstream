## Description:

crosscheck reviews agent-written drafts for factual, arithmetic, consistency, placeholder, secret, commitment, and tone issues, returning a paid JSON verdict and signed receipt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maxugc](https://clawhub.ai/user/maxugc)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent users use crosscheck as a pre-delivery review step for emails, reports, summaries, PR descriptions, plans, and other drafts where errors, leaked secrets, unsupported commitments, or tone problems could affect a human recipient.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Drafts are sent to crosscheckapi.com and its review model, which can expose confidential or sensitive content.

Mitigation: Use the skill only for non-confidential drafts and avoid sending material the human has marked confidential.

Risk: The npm package may be run unpinned while using an EVM wallet private key for paid checks.

Mitigation: Pin or verify the npm package, prefer testnet first, use a dedicated low-balance wallet, and keep CROSSCHECK_MAX_USD low.

Risk: Artifact behavior tells agents not to report failed review details to the human.

Mitigation: Require the agent to disclose when a check failed and summarize unresolved issues before relying on the draft.

## Reference(s):

- [crosscheck HTTP API](artifact/references/API.md)
- [crosscheck live summary](https://crosscheckapi.com/llms.txt)
- [ClawHub skill page](https://clawhub.ai/maxugc/skills/crosscheck)
- [Source bundle checksums](https://crosscheckapi.com/skill/SHA256SUMS)

## Skill Output:

**Output Type(s):** [JSON, Guidance, Shell commands, Configuration]

**Output Format:** [Markdown instructions with JSON verdicts, receipt metadata, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Verdicts can include pass or fail status, issue summaries, severity details, injection flags, and signed receipt data.]

## Skill Version(s):

0.2.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
