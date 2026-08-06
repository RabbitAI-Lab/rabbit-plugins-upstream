## Description: <br>
Searches live web information with Google Programmable Search Engine for research, SEO keyword analysis, ranking review, and search traffic optimization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and operations teams use this skill to retrieve current web information and organize Google search results for keyword analysis, search traffic review, and general information lookup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release requests broad command execution and local file inspection that is not tightly scoped to web search. <br>
Mitigation: Use it in a constrained workspace, review command and file-access requests before approval, and narrow permissions before deployment where possible. <br>
Risk: Search queries can expose secrets, internal project names, or private data to external services. <br>
Mitigation: Redact sensitive inputs, avoid private data in queries, and use approved API credentials managed outside the skill text. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/google-search) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown or JSON search-result summaries with setup commands when configuration is needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require Google API credentials and a custom search engine identifier; avoid putting secrets or private data in search queries.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter reports 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
