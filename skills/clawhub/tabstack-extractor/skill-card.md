## Description: <br>
Extract structured data from websites using the Tabstack API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[noblepayne](https://clawhub.ai/user/noblepayne) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to extract clean Markdown or schema-shaped JSON from public or approved web pages such as job listings, news articles, and product pages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends target URLs and extracted page content to the Tabstack API, which may expose private, secret-bearing, intranet, or regulated data if used on inappropriate pages. <br>
Mitigation: Use the skill only for public or approved web pages, and do not submit private intranet URLs, URLs containing secrets, or regulated data unless Tabstack processing is approved. <br>
Risk: The Tabstack API key can be exposed if copied into shared files, command history, logs, or committed configuration. <br>
Mitigation: Store TABSTACK_API_KEY in an environment variable or approved secret store, keep it out of repositories and logs, and rotate it if exposure is suspected. <br>
Risk: The artifact suggests installing Babashka by piping a remote install script into bash, which can run unreviewed remote code. <br>
Mitigation: Prefer Homebrew, Nix, or an inspected pinned Babashka release instead of piping a remote install script into bash. <br>


## Reference(s): <br>
- [Tabstack API Reference](references/api_reference.md) <br>
- [Schema Creation Guide](references/schema_guide.md) <br>
- [Job Listing Schema](references/job_schema.json) <br>
- [News Article Schema](references/news_schema.json) <br>
- [Simple Article Schema](references/simple_article.json) <br>
- [Tabstack Extract JSON API Docs](https://docs.tabstack.ai/api/extract-json-v-1) <br>
- [Tabstack API Docs](https://docs.tabstack.ai/api/tabs-api) <br>
- [JSON Schema Documentation](https://json-schema.org/learn/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, configuration examples, Python and curl wrappers, and Tabstack API responses as Markdown or JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Tabstack API key; extraction quality and response time depend on the target page, schema design, and Tabstack API availability.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
