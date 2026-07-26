## Description: <br>
Search and fetch articles from Grokipedia.com - xAI's AI-generated encyclopedia. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kirillleventcov](https://clawhub.ai/user/kirillleventcov) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and agents use this skill to search for public Grokipedia articles and fetch article content for research, comparison, or answer preparation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to grokipedia.com. <br>
Mitigation: Use this skill for public lookups and avoid sensitive, private, or regulated search terms. <br>
Risk: Raw HTML output from fetched articles is untrusted external content. <br>
Mitigation: Prefer Markdown output for agent use and sanitize or review raw HTML before any rendering step. <br>
Risk: Reproducible installs may vary because dependency resolution depends on the package manager state. <br>
Mitigation: Use pinned dependencies or a lockfile when repeatable installation is required. <br>


## Reference(s): <br>
- [ClawHub Grokipedia Skill Page](https://clawhub.ai/kirillleventcov/skills/grokipedia) <br>
- [Grokipedia](https://grokipedia.com) <br>
- [Grokipedia Typeahead API](https://grokipedia.com/api/typeahead) <br>
- [Grokipedia Article Pages](https://grokipedia.com/page/{slug}) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [JSON search results and Markdown article content; fetch can optionally return raw HTML.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search accepts a query and limit from 1 to 50; fetch accepts a case-sensitive article slug.] <br>

## Skill Version(s): <br>
1.2.0 (source: package.json and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
