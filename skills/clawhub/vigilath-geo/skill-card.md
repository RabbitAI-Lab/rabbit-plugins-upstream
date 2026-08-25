## Description:

Connects an agent to Vigilath GEO so it can run website GEO and SEO checks, query AI-search visibility data, inspect industry rankings, review account reports, monitor sentiment, and generate optimization guidance through the Vigilath service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dz1995](https://clawhub.ai/user/dz1995)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to assess a site's AI-search and SEO readiness, inspect brand visibility and sentiment in AI search results, and request optimization or reporting workflows. Anonymous checks are available for website and industry diagnostics, while account-specific reporting, monitoring, content, wallet, and top-up operations require Vigilath authorization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer can write skill files into multiple local agent skill directories and store a reusable Vigilath token in ~/.vigilath/config.

Mitigation: Review the installer before use, prefer a manual or OpenClaw-native install path, and use --dir to target only the intended skills directory.

Risk: Account-specific commands rely on a long-lived service token.

Mitigation: Protect ~/.vigilath/config as a secret, avoid committing it, and rotate or reauthorize the token if it is exposed or no longer needed.

Risk: Wallet and top-up commands are payment-adjacent account actions.

Mitigation: Run wallet or top-up commands only after explicit user intent, and preserve service-returned amounts, addresses, and payment instructions exactly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dz1995/skills/vigilath-geo)
- [Server-resolved GitHub provenance](https://github.com/dz1995/GEO-skills/tree/main/vigilath-geo)
- [Project homepage](https://github.com/dz1995/GEO-skills)
- [Vigilath skill installation endpoint](https://vigilath.cn/skill)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and terminal-oriented text with JSON service responses where returned by the client]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some commands call external Vigilath APIs; account-specific commands require a stored or environment-provided Vigilath token.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
