## Description: <br>
Fetches Google web or news results with links, snippets, knowledge graph data, and related questions via the Serper.dev API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[samoppakiks](https://clawhub.ai/user/samoppakiks) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this plugin to retrieve Google web or news results when they need current search data with source links, snippets, knowledge graph facts, or related questions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to Serper.dev using the configured API key. <br>
Mitigation: Use only where that data sharing is allowed, keep the API key out of prompts and committed files, and avoid submitting secrets, credentials, private customer data, or sensitive investigations. <br>
Risk: Search and news results come from external web sources and may be incomplete, outdated, or unsuitable to act on without review. <br>
Mitigation: Review returned source links, snippets, and dates before relying on the results for decisions or downstream actions. <br>


## Reference(s): <br>
- [Serper.dev](https://serper.dev) <br>
- [ClawHub skill page](https://clawhub.ai/samoppakiks/skills/serper-search) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON] <br>
**Output Format:** [Text content containing pretty-printed JSON search results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns web organic results, knowledge graph data, related questions, or news results depending on the requested search type.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
