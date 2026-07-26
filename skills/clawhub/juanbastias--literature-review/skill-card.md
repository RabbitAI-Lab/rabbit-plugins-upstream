## Description: <br>
Assistance with writing literature reviews by searching for academic sources via Semantic Scholar, OpenAlex, Crossref and PubMed APIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juanbastias](https://clawhub.ai/user/juanbastias) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Researchers, students, and developers use this skill to find academic papers, inspect DOI-based metadata, compare sources, and draft literature review sections with citations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill documents workflows for a local lit_search.py script that is not included in the release. <br>
Mitigation: Use only a local script you trust, review it before execution, and adjust commands to the reviewed script path. <br>
Risk: Academic API searches may send queries, optional API keys, and email identifiers to external academic data providers. <br>
Mitigation: Avoid sensitive search terms, use approved API credentials, and configure email identifiers according to your organization or institution's policy. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Text, Markdown] <br>
**Output Format:** [Markdown guidance with shell command examples and structured literature metadata] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a trusted local lit_search.py script, Python 3, requests, and optional academic API keys.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence; artifact frontmatter lists 1.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
