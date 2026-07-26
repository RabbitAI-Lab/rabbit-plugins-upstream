## Description: <br>
Searches Wikimedia Commons for images and returns metadata, download URLs, and optional thumbnail composites for visual comparison. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agents use this skill to search Wikimedia Commons for relevant images, inspect returned metadata and download URLs, and compare thumbnail results before selecting images for a task. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on a third-party backend and requires a locally stored API key. <br>
Mitigation: Use a dedicated, least-privilege key, keep .env files out of shared repositories, and rotate the key if the skill is uninstalled or no longer trusted. <br>
Risk: Image search results may include externally hosted content and metadata selected by the upstream service. <br>
Mitigation: Review returned metadata and download URLs before using images in downstream work, especially for commercial or public outputs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/wikimedia-search-images) <br>
- [Publisher profile](https://clawhub.ai/user/alinklab) <br>
- [XiaoBenYang API key portal](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, configuration] <br>
**Output Format:** [Markdown summaries of JSON API results, including image metadata, download URLs, status messages, and optional thumbnail composite references.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY_APIKEY value before API calls can be made.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
