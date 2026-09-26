## Description:

Finds and dissects benchmark creators by searching or confirming a target account, filtering candidates for commercial relevance and copyability, collecting creator content batches, and producing a teardown plus a practical adaptation roadmap.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and operators use this skill to identify a suitable benchmark creator, analyze the creator's early, best-performing, and recent posts, and turn the analysis into a non-copying adaptation plan. The skill is aimed at solo knowledge creators who need structured evidence before deciding whom to learn from.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may require broad TikHub API credentials and refers to storing them in a shared plaintext ~/.env file.

Mitigation: Use a limited-scope or temporary API key when available, avoid committing or displaying credentials, and prefer session-scoped environment variables over persistent plaintext storage.

Risk: The workflow can make paid scraping requests through TikHub.

Mitigation: Run a dry-run or cost estimate first, confirm the target account and expected request count with the user, and wait for explicit approval before making paid requests.

Risk: Some paths may require logging into personal social or WeChat accounts through third-party tooling.

Mitigation: Warn the user before any login-based path, prefer non-login collection paths, and continue only after the user accepts the account-risk warning.

Risk: Creator content collection and adaptation can create copyright or impersonation risk if copied into public outputs.

Mitigation: Use collected material only for private analysis, do not reuse names, exact wording, cases, or first-party proof in generated public drafts, and keep adaptation guidance focused on transferable structures.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/aikey-benchmark)
- [Publisher profile](https://clawhub.ai/user/iamzifei)
- [Three-filter criteria](references/三筛判据.md)
- [Collection manual](references/抓取手册.md)
- [Rule cards](references/规则卡.md)
- [TikHub](https://tikhub.io)
- [TikHub user console](https://user.tikhub.io)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports, tables, file plans, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce structured creator teardown notes, candidate tables, cost estimates, and local artifact paths.]

## Skill Version(s):

0.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
