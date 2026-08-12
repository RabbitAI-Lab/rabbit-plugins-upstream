## Description:

AI Product Radar monitors AI product-launch feeds, enriches product items with categories and scores, captures screenshots when enabled, and produces trend reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, product teams, market analysts, and founders use this skill to track new AI product launches, monitor competitor activity, and generate ranked trend reports from RSS feeds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The default screenshot path can execute generated code influenced by feed-provided links.

Mitigation: Review the skill before use and run with `--no-screenshots` unless screenshot code is fixed to pass URLs and paths as arguments or JSON-escaped values.

Risk: Normal operation makes outbound requests to RSS feeds and linked product pages.

Mitigation: Run the skill only in environments where that outbound browsing is acceptable, and prefer approved custom feed lists for controlled deployments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/terrycarter1985/skills/ai-product-radar)
- [Product Hunt Feed](https://www.producthunt.com/feed)
- [TechCrunch AI Feed](https://techcrunch.com/category/artificial-intelligence/feed/)
- [The Verge AI Feed](https://www.theverge.com/rss/ai-artificial-intelligence/index.xml)
- [VentureBeat AI Feed](https://venturebeat.com/category/ai/feed/)
- [Hacker News Show Feed](https://hnrss.org/show)
- [MIT Technology Review AI Feed](https://www.technologyreview.com/topic/artificial-intelligence/feed)
- [Ars Technica Technology Lab Feed](https://feeds.arstechnica.com/arstechnica/technology-lab)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Files, Shell commands]

**Output Format:** [Markdown report, structured JSON files, screenshot or info-card files, and terminal status output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes artifacts to a user-selected output directory; screenshots can be disabled with --no-screenshots.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
