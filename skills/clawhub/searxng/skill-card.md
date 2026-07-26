## Description: <br>
Privacy-respecting metasearch using your local SearXNG instance for web, image, news, and other searches without external API dependencies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[abk234](https://clawhub.ai/user/abk234) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to search web, image, news, video, and other SearXNG categories through a configured local, private, or public SearXNG instance. It is useful when agents need search results without relying on commercial search APIs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries and returned results are handled by the configured SearXNG instance, which may be local, private, or public. <br>
Mitigation: Install only with a trusted SEARXNG_URL, prefer localhost or a private instance, and avoid sending secrets or sensitive internal data as search queries. <br>
Risk: Remote HTTPS instances may have weaker transport assurance because the artifact documents support for self-signed certificates. <br>
Mitigation: Use a trusted HTTPS endpoint and enable proper TLS verification before using a remote SearXNG instance. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/abk234/skills/searxng) <br>
- [SearXNG](https://searxng.org) <br>
- [SearXNG Installation Documentation](https://docs.searxng.org/admin/installation.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration] <br>
**Output Format:** [Formatted search result tables or JSON returned from the configured SearXNG API] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and a SEARXNG_URL configuration; default instance URL is http://localhost:8080.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact frontmatter and changelog show 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
