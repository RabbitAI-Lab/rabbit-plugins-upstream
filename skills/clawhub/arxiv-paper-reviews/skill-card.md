## Description: <br>
Interact with an arXiv Crawler API to fetch arXiv paper lists, view paper details and comments, search or import papers, and submit paper review comments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxrys](https://clawhub.ai/user/zxrys) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and research workflows use this skill to query arXiv paper metadata, inspect comments, search by title, import arXiv URLs, and submit review comments through a third-party API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paper searches, imports, comments, author names, and optional API credentials are sent to a third-party service over plain HTTP. <br>
Mitigation: Avoid API keys, private reviewer notes, unpublished research details, sensitive search terms, and identifying author names unless the publisher documents the service operator, retention practices, and provides an HTTPS endpoint. <br>
Risk: The skill can submit public review comments to the remote service. <br>
Mitigation: Review comment content before submission and avoid posting confidential, identifying, or unverified claims. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxrys/skills/arxiv-paper-reviews) <br>
- [Configured arXiv Crawler API endpoint](http://weakaccept.top:8000/) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration] <br>
**Output Format:** [Command-line text output with JSON-backed API responses and markdown usage examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses configurable API base URL, optional API key, optional default author name, and command parameters for date, category, interest, limits, offsets, paper keys, search queries, comments, and arXiv URLs.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
