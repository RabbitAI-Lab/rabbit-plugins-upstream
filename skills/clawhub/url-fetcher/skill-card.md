## Description: <br>
Fetch and save web content using only Python stdlib with URL and path validation, basic HTML-to-markdown conversion, and no API keys or external dependencies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[johstracke](https://clawhub.ai/user/johstracke) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to fetch static web pages, preview or save their content, and optionally convert basic HTML to markdown for content aggregation, research collection, and simple scraping workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can fetch user-provided URLs, including pages that may be untrusted or unsuitable for sensitive internal environments. <br>
Mitigation: Use it only with URLs you intend to retrieve, avoid relying on it as a security boundary, and review fetched content before using it downstream. <br>
Risk: The skill can save fetched content to local paths selected by the user. <br>
Mitigation: Keep file writes to intended workspace locations and rely on the included path validation as a safeguard, not as the only control for sensitive systems. <br>
Risk: Basic HTML-to-markdown conversion may omit, flatten, or misrepresent page structure. <br>
Mitigation: Review converted markdown before using it for research, publishing, or automated decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/johstracke/skills/url-fetcher) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, files] <br>
**Output Format:** [Terminal output and optional saved HTML or markdown files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses user-provided HTTP/HTTPS URLs and optional user-selected output paths.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
