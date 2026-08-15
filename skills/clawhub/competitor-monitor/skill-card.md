## Description:

Monitors competitor or target web pages over time, compares each crawl against saved snapshots, and reports relevant changes in prices, copy, listings, or page structure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and business analysts use this skill to set up recurring web page monitoring and receive concise change summaries for competitive pricing, product listings, industry news, or compliance-sensitive pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The learner component can persist free-form notes, errors, and preferences locally beyond the immediate monitoring task.

Mitigation: Use the learner only when local persistence is acceptable, and avoid storing secrets, internal URLs, customer data, or other sensitive details in learner notes or error messages.

Risk: Recurring crawls can create compliance or availability risk if they ignore site policies or run too frequently.

Mitigation: Configure monitoring to respect robots.txt, site terms, and rate limits, and restrict monitoring to public pages appropriate for the intended business use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/competitor-monitor)
- [Publisher profile](https://clawhub.ai/user/qq435912743)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands plus optional JSON, CSV, or text diff files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local snapshots, diff reports, crawl outputs, and learned_patterns.json when the bundled scripts are used.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
