## Description: <br>
Search the web using a self-hosted SearXNG instance. Privacy-respecting metasearch that aggregates results from multiple engines. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clockworksquirrel](https://clawhub.ai/user/clockworksquirrel) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to configure and query a local or self-hosted SearXNG instance for privacy-respecting web search. It provides setup guidance, API examples, category and language search patterns, pagination, and shell integration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The example service binds to port 8080 and may be reachable by others if the host is exposed. <br>
Mitigation: Restrict access to port 8080 with local binding, firewall rules, or network controls before deployment. <br>
Risk: The setup example uses a placeholder secret key and the latest Docker image tag. <br>
Mitigation: Replace the example secret key with a random value and consider pinning the SearXNG Docker image version. <br>
Risk: The example safe_search setting allows unfiltered results. <br>
Mitigation: Raise the safe_search setting when filtered results are required. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Code] <br>
**Output Format:** [Markdown with bash commands, YAML configuration snippets, and shell function examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the optional SEARXNG_URL environment variable to target a local or self-hosted SearXNG service.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
