## Description:

Finds and dissects social-media benchmark creators by searching or confirming an account, applying money, clarity, and copyability filters, collecting early, top-performing, and latest content, and producing a teardown plus a copy roadmap.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and solo content operators use this skill to identify a benchmark account worth learning from, collect comparable content batches, and turn the analysis into concrete next actions. It is especially oriented toward knowledge creators who need account-level evidence before imitating formats or topics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can require third-party API credentials and may persist them in local configuration.

Mitigation: Use a least-privilege key if available, store it in a protected secret manager or restricted config file, and rotate or revoke it after use.

Risk: Benchmark memory and saved outputs can reveal business intent, target accounts, collection history, and creator strategy.

Mitigation: Review saved benchmark folders and memory entries after each run, remove sensitive history that is no longer needed, and restrict access to the output directory.

Risk: Collected social-media content may create copyright, platform-policy, or account-safety exposure if reused or scraped through logged-in paths.

Mitigation: Use collected material for private analysis, avoid republishing names, wording, cases, or media, and confirm before using any workflow that routes login credentials through third-party tools.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-benchmark)
- [三筛判据](artifact/references/三筛判据.md)
- [抓取手册](artifact/references/抓取手册.md)
- [TikHub](https://tikhub.io)
- [TikHub user console](https://user.tikhub.io)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown reports, CSV-style content inventories, command guidance, and structured local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include benchmark account dossiers, full content lists, three content-batch directories, covers, transcripts, and a final teardown when collection succeeds.]

## Skill Version(s):

0.1.2 (source: server release metadata; artifact frontmatter says 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
