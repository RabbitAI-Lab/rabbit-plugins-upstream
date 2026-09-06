## Description:

Find and dissect a benchmark creator by searching or confirming a creator account, filtering candidates for commercial fit, understandable business mechanics, and copyable capabilities, then collecting early, top-performing, and recent posts to produce a teardown and adaptation roadmap.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and content operators use this skill to identify a benchmark creator, decide whether that creator is worth learning from, and turn collected post evidence into a concrete adaptation plan without copying names, wording, cases, or identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can require a paid scraping API key and may encourage broad local persistence of that secret.

Mitigation: Use the narrowest available TikHub key, keep it in a secure secret store, avoid sharing it in chat or shell history, and run the documented dry-run cost estimate before paid collection.

Risk: Some extraction paths depend on third-party services or mini-programs that may require account login or link submission.

Mitigation: Verify the provider before use, avoid login-based paths when possible, and require explicit user confirmation before any step that sends credentials or creator links to a third party.

Risk: Benchmark teardowns can be misused to copy another creator's words, cases, identity, or content.

Mitigation: Use collected material only as private research notes and keep final user-facing work free of the benchmark creator's name, original wording, cases, and personal claims.

Risk: Incomplete post lists, missing transcripts, or platform metrics gaps can lead to misleading conclusions.

Mitigation: Label incomplete collection clearly, require full-list denominators for top-performing conclusions when available, and state when analysis is limited to titles, covers, engagement, or a partial sample.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/iamzifei/skills/zmm-benchmark)
- [三筛判据](artifact/references/三筛判据.md)
- [抓取手册](artifact/references/抓取手册.md)
- [TikHub](https://tikhub.io)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with tables, inline shell commands, and file-oriented report structures]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local research notes, CSV-style tabular data, media extraction status, and a final teardown plan when supporting collection steps are completed.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
