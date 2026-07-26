## Description: <br>
High-accuracy web search and research via Parallel.ai API. Optimized for AI agents with rich excerpts and citations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pntrivedy](https://clawhub.ai/user/pntrivedy) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and research agents use this skill to run Parallel.ai web searches for deep research, fact-checking, company or person research, and multi-hop queries that need cited source excerpts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A bundled default API key can create an unclear account, quota, and billing boundary. <br>
Mitigation: Set PARALLEL_API_KEY to an account-controlled key before use and do not rely on the bundled fallback key. <br>
Risk: Research queries and searched content are sent to the Parallel.ai API. <br>
Mitigation: Avoid submitting secrets, regulated data, or proprietary research queries unless that third-party data transfer is approved. <br>
Risk: The setup installs the parallel-web Python dependency from the package ecosystem. <br>
Mitigation: Pin or verify the dependency version according to local supply-chain policy before deployment. <br>


## Reference(s): <br>
- [Parallel.ai Documentation](https://docs.parallel.ai) <br>
- [Parallel.ai Platform](https://platform.parallel.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown-formatted search results or JSON with search identifiers, result URLs, titles, excerpts, publish dates, and usage data.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search behavior depends on Parallel.ai API access, the PARALLEL_API_KEY environment variable, selected mode, and requested maximum results.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
