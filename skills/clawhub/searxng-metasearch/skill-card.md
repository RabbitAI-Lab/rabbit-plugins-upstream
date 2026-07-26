## Description: <br>
Search the web using a self-hosted SearXNG instance. Privacy-respecting metasearch that aggregates results from multiple engines. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clockworksquirrel](https://clawhub.ai/user/clockworksquirrel) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and technical users use this skill to configure and query a self-hosted SearXNG metasearch instance for privacy-respecting web, image, news, video, IT, and science search results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The sample SearXNG settings include a placeholder secret key. <br>
Mitigation: Replace the placeholder with a random secret before running the service. <br>
Risk: The Docker example uses the latest image tag, which can change over time. <br>
Mitigation: Pin the SearXNG Docker image to a reviewed version for repeatable deployments. <br>
Risk: The sample server binds to 0.0.0.0 on port 8080. <br>
Mitigation: Bind to localhost or firewall port 8080 unless remote access is intentional. <br>
Risk: The sample search configuration sets safe_search to 0. <br>
Mitigation: Review and adjust safe_search if unfiltered results are not appropriate for the deployment environment. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash, Docker Compose, YAML, and curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance assumes a reachable SearXNG instance and optionally uses the SEARXNG_URL environment variable.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
