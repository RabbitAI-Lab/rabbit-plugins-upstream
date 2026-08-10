## Description: <br>
Extract structured data from HTML pages or URLs using CSS selectors, XPath, regex, or LLM natural-language extraction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation agents use this skill to extract named fields from HTML documents, local files, or fetched pages and return structured JSON for downstream workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: URL extraction can fetch user-directed pages, including untrusted or internal URLs if an agent is given those inputs. <br>
Mitigation: Allow URL fetching only for intended targets, prefer local HTML files for sensitive workflows, and review requested URLs before execution. <br>
Risk: LLM extraction can send raw page HTML and an API key to a configurable OpenAI-compatible endpoint. <br>
Mitigation: Use CSS, XPath, or regex for sensitive pages, and verify OPENAI_BASE_URL and OPENAI_API_KEY before calling extract_by_llm. <br>


## Reference(s): <br>
- [Usage documentation](references/usage.md) <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/extractor) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python and CLI examples; extractor runtime output is JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [CSS, XPath, and regex extraction return field-to-value JSON mappings; URL mode requires Playwright and Chromium.] <br>

## Skill Version(s): <br>
1.1.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
