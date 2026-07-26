## Description: <br>
Search the web using a self-hosted SearXNG metasearch engine. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stperic](https://clawhub.ai/user/stperic) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to look up current web information through a SearXNG instance they configure with SEARXNG_URL. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to the SearXNG instance configured in SEARXNG_URL. <br>
Mitigation: Use a trusted HTTPS SearXNG instance and avoid searching for secrets, credentials, or highly sensitive private information. <br>


## Reference(s): <br>
- [SearXNG documentation](https://docs.searxng.org) <br>
- [ClawHub skill page](https://clawhub.ai/stperic/skills/local-websearch) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration] <br>
**Output Format:** [JSON search results with title, URL, description, source engines, and relevance score fields.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and a SEARXNG_URL environment variable; result count is bounded from 1 to 20.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and script version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
