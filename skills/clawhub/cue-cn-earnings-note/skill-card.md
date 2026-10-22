## Description:

Drafts an eight-section earnings review for a Chinese-listed company, combining period comparisons, account reconciliations, guidance checks, and a forecast scaffold.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

Investment researchers and financial analysts can provide an issuer and reporting period, with optional public materials and focus areas, to prepare a structured earnings-review draft and source index. Treat the draft as a starting point: manually verify figures and complete ratings or other investment judgments before sharing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: When authenticated connectivity is enabled, the optional connection test may send the API key to an unverified or unencrypted destination.

Mitigation: Use only approved HTTPS destinations and prevent credentials from being forwarded across redirects; keep the credential-free workflow when authenticated connectivity is not needed.

Risk: Financial figures or conclusions in a generated draft may be inaccurate or misleading.

Mitigation: Submit only public documents suitable for external processing, review optional dependencies and their versions, and manually verify report figures before sharing.

## Reference(s):

- [README and quick start](artifact/README.md)
- [Data channel coverage and limits](artifact/references/data-channels.md)
- [Coverage ledger contract](artifact/references/coverage-ledger.md)
- [Cue skill release](https://clawhub.ai/huhoo/skills/cue-cn-earnings-note)
- [Publisher profile](https://clawhub.ai/user/huhoo)
- [Cue API catalog](https://cuecue.cn/api/mcp-catalog)

## Skill Output:

**Output Type(s):** [Markdown, JSONL, Text]

**Output Format:** [Markdown earnings note (note.md), JSON Lines source index (sources.jsonl), and a progress ledger (progress.md).]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [AI-generated first draft; manually verify figures and investment judgments before sharing.]

## Skill Version(s):

0.3.41 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
