## Description:

Uses deterministic Chan theory scripts to analyze A-share stocks and have the agent report rule-based buy, hold, sell-reduce, or wait signals with invalidation prices instead of inventing chart structures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsorgcn](https://clawhub.ai/user/adsorgcn)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to analyze Chinese A-share stocks with Chan theory structures, rule-based operational posture, and invalidation levels. The output is decision-support analysis and not personal financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives contradictory guidance about optional API-key handling, including paths that may put the HITHINK key into chat history.

Mitigation: Prefer terminal-based setup via setup_env.py --set-key, avoid sending keys in chat, and revoke or rotate any key that may have been exposed.

Risk: On Linux and macOS, stored credentials are local plaintext protected by file permissions rather than OS-level encryption.

Mitigation: Keep credential files permission-restricted, use environment variables when appropriate, and rotate keys if local account access is in doubt.

Risk: Rule-based stock outputs may be mistaken for personal investment advice.

Mitigation: Present outputs as mechanical Chan theory signals with invalidation levels and preserve the artifact's statement that results are not personal financial advice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/adsorgcn/skills/chanlun-engine-skill)
- [Project homepage](https://github.com/adsorgcn/chanlun-engine-skill)
- [Chanlun theory core reference](references/chanlun-core.md)
- [Engine notes](references/engine-notes.md)
- [Getting started guide](references/getting-started.md)
- [Security notes](SECURITY.md)
- [HiThink Financial API](https://github.com/HiThink-Tech/Financial-API)
- [Chan theory source archive](https://github.com/stockServ/chzhshch-108-plus)
- [Chan theory blog archive](https://chzhshch.blog/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown analysis based on structured JSON from local scripts, with occasional shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports must preserve engine-provided verdicts, invalidation prices, caveats, and candidate-signal uncertainty.]

## Skill Version(s):

1.1.8 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
