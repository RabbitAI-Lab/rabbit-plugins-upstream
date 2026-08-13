## Description:

通用 BOSS 直聘求职 copilot：配合仿真人浏览器后端用真实光标安全检索/收藏岗位、读 JD、写破冰话术并按授权发送。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huagavin](https://clawhub.ai/user/huagavin)

### License/Terms of Use:

MIT

## Use Case:

Job seekers and their agents use this skill to turn a resume or job-search goal into a reusable BOSS Zhipin workflow for profile building, job search, filtering, bookmarking, JD reading, icebreaker drafting, and authorized message sending.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate a logged-in BOSS Zhipin account and may change account state through bookmarking or message sending.

Mitigation: Review each send or bookmark action and keep AUTHORIZED unset unless the account-changing action is intended.

Risk: Local files such as profile.yaml, target_library.csv, and .work outputs may contain job-search details and recruiter contact data.

Mitigation: Store generated files with appropriate local access controls and remove sensitive working files when they are no longer needed.

Risk: Browser automation against BOSS Zhipin can encounter verification, rate limiting, or anti-abuse controls.

Mitigation: Use only the documented agent-browser-runtime backend, follow real-cursor and rate-limit rules, and stop for human review on verification or safety-wall signals.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huagavin/skills/boss-zhipin-copilot)
- [Server-Resolved GitHub Repository](https://github.com/HuaGavin/boss-zhipin-copilot)
- [agent-browser-runtime](https://github.com/energypantry/agent-browser-runtime)
- [Browser Backend Contract](references/browser_backend.md)
- [Safety Rules](references/safety_rules.md)
- [Script Catalog](references/script_catalog.md)
- [Profile Schema](references/profile_schema.md)
- [Target Library Schema](references/target_library_schema.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, YAML/CSV configuration, JSON job data, and local draft text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local workflow artifacts such as profile.yaml, target_library.csv, candidates.csv, JD JSON, and message drafts; account-changing actions require explicit authorization.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter and CHANGELOG declare 1.0.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
