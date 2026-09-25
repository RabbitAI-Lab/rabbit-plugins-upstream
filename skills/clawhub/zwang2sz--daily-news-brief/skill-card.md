## Description:

Collects public international, economic, and technology news each morning and generates a concise Markdown news brief with highlights and historical context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zwang2sz](https://clawhub.ai/user/zwang2sz)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to automate daily news monitoring and produce scheduled briefings for console output, local archives, and configured delivery channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer can add persistent scheduled execution and optional privileged service setup.

Mitigation: Review the installer before running it, prefer host-managed or clearly labeled per-user scheduling, and avoid systemd or administrator setup unless operationally required.

Risk: Generated briefs include scraped links and Markdown from external news sources.

Mitigation: Treat generated content as untrusted, verify links before redistribution, and sanitize Markdown before posting to shared channels.

Risk: Configured recipients and delivery channels may send briefs outside the intended audience.

Mitigation: Verify recipients and output channels before enabling Feishu, WeChat, email, SMS, or push delivery.

## Reference(s):

- [OpenClaw documentation](https://docs.openclaw.ai)
- [CCTV World News](https://news.cctv.com/world)
- [Reuters World News](https://www.reuters.com/world)
- [BBC World News](https://www.bbc.com/news/world)
- [Bloomberg Markets](https://www.bloomberg.com/markets)
- [Financial Times Markets](https://www.ft.com/markets)
- [TechCrunch](https://techcrunch.com)
- [The Verge Tech](https://www.theverge.com/tech)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown brief with source links, plus local archive files and console output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Briefs are generated from configured public news sources and may be scheduled for recurring execution.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
