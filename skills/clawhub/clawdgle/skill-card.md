## Description: <br>
Public API usage for the Clawdgle markdown-first search engine. Use when interacting with Clawdgle to: (1) search indexed markdown content, (2) fetch markdown for a URL, (3) request indexing of a URL via ingest, or (4) direct users to the donate link. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rubybrewsday](https://clawhub.ai/user/rubybrewsday) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to interact with Clawdgle's public API for markdown search, markdown retrieval by URL, self-serve URL indexing requests, and donation-link routing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may submit private URLs, sensitive markdown, or personal contact details to the ingest endpoint. <br>
Mitigation: Submit only information intended for clawdgle.com and omit sensitive contact details unless sharing them is acceptable. <br>
Risk: High-volume ingest requests can spam the public endpoint. <br>
Mitigation: Rate-limit ingest requests and use the endpoint only for URLs that need indexing. <br>


## Reference(s): <br>
- [Clawdgle API](https://clawdgle.com) <br>
- [Clawdgle skill page](https://clawhub.ai/rubybrewsday/skills/clawdgle) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands] <br>
**Output Format:** [Markdown with endpoint descriptions and inline curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Public endpoint guidance only; no credential handling is described.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
