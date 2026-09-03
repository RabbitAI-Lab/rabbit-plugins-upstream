## Description:

Finds and analyzes benchmark creators across Douyin, Xiaohongshu, and WeChat Channels by applying three filters, collecting representative content batches, and producing a teardown and copy roadmap.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and agents use this skill to identify a comparable creator, assess whether that creator is worth learning from, gather representative content batches, and produce an evidence-labeled benchmark teardown and action roadmap.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may require a paid third-party scraping API key and can store that secret in a persistent local .env file.

Mitigation: Use a narrowly scoped, revocable TikHub key if available; avoid persistent secret storage unless local file exposure is understood; rotate or revoke the key after use.

Risk: Scraping requests may incur per-request costs or target the wrong account if started before confirmation.

Mitigation: Run a dry-run cost estimate first, confirm the account and estimated cost with the user, and proceed only after explicit approval.

Risk: Some paths may involve third-party tools or login-based workflows that can expose account credentials or trigger platform controls.

Mitigation: Prefer no-login API paths, warn the user before any login-based route, and wait for explicit confirmation before continuing.

Risk: Benchmark content could be misused by copying names, original wording, cases, or creator-specific proof into downstream drafts.

Mitigation: Use only transferable signals and structures, keep benchmark names and source-specific material out of generated drafts, and preserve the skill's final no-copy warning.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-benchmark)
- [Publisher profile](https://clawhub.ai/user/iamzifei)
- [三筛判据](references/三筛判据.md)
- [抓取手册](references/抓取手册.md)
- [TikHub](https://tikhub.io)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports, structured tables, CSV-oriented file outputs, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide creation of local benchmark folders, CSV inventories, per-post metadata, cover images, transcripts, and a final teardown report.]

## Skill Version(s):

0.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
