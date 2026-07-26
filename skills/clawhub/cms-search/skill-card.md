## Description: <br>
Cms Search helps agents run web searches and retrieve current information through a CMS search endpoint. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[spzwin](https://clawhub.ai/user/spzwin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill when a user requests web search, current information, news, policies, announcements, market or competitor research, or other internet-dependent answers. It supports simple single-query lookups and multi-query retrieval for comparison, verification, and synthesis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms are sent to a remote CMS search service using the CMS_USER_KEY supplied by the runtime environment. <br>
Mitigation: Avoid submitting secrets, private personal data, confidential business details, or regulated medical or financial information unless that external transmission is acceptable. <br>
Risk: Search results can be incomplete, outdated, or misleading for time-sensitive or high-impact decisions. <br>
Mitigation: Use multiple search dimensions when needed, prefer official sources, and cross-check results before relying on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/spzwin/skills/cms-search) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown or JSON search results, with direct Python command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires CMS_USER_KEY in the runtime environment; optional source, format, and datetime parameters control search behavior.] <br>

## Skill Version(s): <br>
1.5.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
