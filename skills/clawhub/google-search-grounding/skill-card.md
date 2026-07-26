## Description: <br>
Google Search gives agents Google web search through Gemini Search Grounding for synthesized cited answers and through the Custom Search JSON API for raw results and image search. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shaharsha](https://clawhub.ai/user/shaharsha) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill when they need Google-backed web search, cited synthesized answers, raw links with snippets, or image results. It is especially oriented toward multilingual search with configurable language and country settings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to Google and Gemini services as part of normal operation. <br>
Mitigation: Avoid submitting private or sensitive information in queries and install the skill only when routing searches through Google/Gemini is acceptable. <br>
Risk: The required Google API key can incur quota usage or billing charges. <br>
Mitigation: Use a restricted Google API key, monitor quota and billing, and configure Custom Search only when raw or image modes are needed. <br>
Risk: Default Hebrew language and Israel country settings may affect returned results. <br>
Mitigation: Review the defaults and override GOOGLE_SEARCH_LANG, GOOGLE_SEARCH_COUNTRY, or command-line flags for the intended audience. <br>
Risk: The installer adds the google-genai Python dependency to the active environment. <br>
Mitigation: Install dependencies in an isolated Python environment when shared system packages should not be modified. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/shaharsha/skills/google-search-grounding) <br>
- [Google Programmable Search Engine](https://programmablesearchengine.google.com/) <br>
- [Google Custom Search JSON API endpoint](https://www.googleapis.com/customsearch/v1) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text or JSON search results, with Markdown documentation and shell command examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search mode can include synthesized answers, numbered sources, grounding details, and search queries; raw and image modes return links, snippets, image URLs, or structured JSON.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
