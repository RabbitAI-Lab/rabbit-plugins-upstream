## Description: <br>
Search the web using a self-hosted SearXNG instance, with privacy-respecting metasearch that aggregates results from multiple engines. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clockworksquirrel](https://clawhub.ai/user/clockworksquirrel) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to configure and query a self-hosted SearXNG instance for web, image, news, video, technical, and science search. It provides setup guidance, API examples, expected JSON result fields, and a reusable shell function. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A self-hosted SearXNG service may be unintentionally exposed to the local network or internet. <br>
Mitigation: For local-only use, bind Docker or SearXNG to 127.0.0.1; for remote access, use firewall rules, a trusted reverse proxy, or authentication. <br>
Risk: The sample configuration includes a placeholder secret key. <br>
Mitigation: Replace the placeholder secret key with a random value before running the service. <br>
Risk: Using a floating Docker image tag can change runtime behavior across installs. <br>
Mitigation: Consider pinning the SearXNG Docker image version instead of using latest. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/clockworksquirrel/skills/searxng-self-hosted) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Code] <br>
**Output Format:** [Markdown with bash commands, YAML configuration snippets, and JSON response field descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses optional SEARXNG_URL configuration; examples assume a reachable SearXNG endpoint.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
