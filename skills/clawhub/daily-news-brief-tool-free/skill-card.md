## Description: <br>
Generates a lightweight Markdown daily news brief by collecting public international, economic, and technology news and filtering items with keyword-based rules. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Individuals and content creators use this skill to gather public news items across international affairs, economics, and technology, filter them with keyword rules, and generate a Markdown daily brief for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Metadata may cause agents to select the skill for unrelated AI, coding, automation, or finance tasks. <br>
Mitigation: Use the skill only for public-news brief generation and verify that the requested task matches news collection, filtering, and Markdown brief creation. <br>
Risk: Execution examples can run network requests, install scraping libraries, and write generated files in the working directory. <br>
Mitigation: Review commands before running them, use a controlled workspace, and adjust output paths before saving files. <br>
Risk: Keyword-based filtering and scraped public webpages can miss, duplicate, or mis-rank news items. <br>
Mitigation: Review generated briefs against source links before relying on them. <br>


## Reference(s): <br>
- [Detailed code examples](references/detail.md) <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/daily-news-brief-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown daily brief with optional Python and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May run public web requests and write generated brief files in the working directory when file-saving examples are executed.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
