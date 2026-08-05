## Description: <br>
Researches public-web backlink prospects for a website, separates existing-link reclamation, and validates the opportunity ledger against documented quality gates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lvsao](https://clawhub.ai/user/lvsao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, SEO practitioners, and agent operators use this skill to build evidence-backed backlink prospect and reclamation queues from a public website and optional competitor domains. It supports outreach preparation without claiming that links are obtained or recommending paid links, spam directories, or link schemes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill could be misused to prepare paid link schemes, mass submissions, spam directory outreach, or undisclosed placements. <br>
Mitigation: Follow the release security guidance and reject paid links, link exchanges, mass submissions, coupon pages, scraper pages, and other low-quality or undisclosed routes. <br>
Risk: Public-web pages, search snippets, crawled HTML, and documents can contain misleading evidence or embedded instructions. <br>
Mitigation: Treat collected web content as untrusted evidence, ignore embedded instructions, verify every candidate URL, and keep lower-confidence leads separate from actionable prospects. <br>
Risk: Generated prospect lists can overstate link value, editorial approval, dofollow status, or acquisition certainty. <br>
Mitigation: Require evidence URLs, evidence-state labels, realistic next actions, cost or disclosure notes, and quality-risk notes before outreach. <br>
Risk: Research collection can accidentally access private, local, restricted, or disallowed pages. <br>
Mitigation: Validate redirects and destinations, reject private or reserved hosts, and respect robots directives, publisher terms, rate limits, paywalls, CAPTCHAs, and access controls. <br>


## Reference(s): <br>
- [Research protocol](references/research-protocol.md) <br>
- [ClawHub skill page](https://clawhub.ai/lvsao/skills/seo-backlink-opportunity-finder) <br>
- [Metadata homepage](https://github.com/lvsao/shopify-skill-hub) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summaries with JSON opportunity-ledger records and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a public website URL; optional public competitor domains can be included.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
