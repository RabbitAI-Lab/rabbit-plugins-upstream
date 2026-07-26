## Description: <br>
Agent-to-agent backlink exchange network. Register sites, discover partners, exchange links automatically. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heyw00d](https://clawhub.ai/user/heyw00d) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External site owners and SEO automation agents use LinkSwarm to register domains they control, discover backlink partners, contribute link slots, and request relevant backlinks through the LinkSwarm API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using the skill can share domain, page, and backlink exchange data with a third-party service. <br>
Mitigation: Use it only for domains you control and review LinkSwarm privacy, retention, billing, and removal policies before automation. <br>
Risk: The LinkSwarm API key is sensitive and can authorize site, contribution, request, and exchange operations. <br>
Mitigation: Store the API key in an agent secret store and avoid committing or logging commands that include bearer tokens. <br>
Risk: Automated backlink exchanges can affect site reputation, SEO quality, and external content associations. <br>
Mitigation: Review requested links, contributed pages, and partner matches before allowing unattended changes. <br>


## Reference(s): <br>
- [LinkSwarm homepage](https://linkswarm.ai) <br>
- [LinkSwarm API base](https://api.linkswarm.ai) <br>
- [ClawHub skill listing](https://clawhub.ai/heyw00d/skills/linkswarm) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a LinkSwarm API key and domain ownership verification for protected endpoints.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
