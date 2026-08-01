## Description: <br>
Publish HTML/JS/CSS demos as GitHub Gists and share gists.page preview links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zzir](https://clawhub.ai/user/zzir) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to publish small HTML, JavaScript, and CSS demos as GitHub Gists and share browser preview links through gists.page. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can help an agent publish files using GitHub authentication, which may expose content to anyone with the gist link. <br>
Mitigation: Review files before publishing and do not include secrets, credentials, private business data, or sensitive visitor input. <br>
Risk: Publishing through GitHub CLI, MCP tools, or the REST API requires valid GitHub authentication with gist permissions. <br>
Mitigation: Use the narrowest appropriate token scope, confirm authentication before publishing, and treat secret gists as unlisted rather than private. <br>
Risk: Preview behavior can be affected by browser Service Worker support, GitHub rate limits, and a short metadata cache window. <br>
Mitigation: Verify uploads through the GitHub API or a browser preview, and wait for the documented cache interval before treating a fresh edit as failed. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/zzir/gists.page/tree/main/skills/gists-page) <br>
- [ClawHub skill page](https://clawhub.ai/zzir/skills/gists-page) <br>
- [gists.page preview service](https://gists.page/) <br>
- [GitHub Gists](https://gist.github.com) <br>
- [GitHub Gists API](https://api.github.com/gists) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, API examples, and shareable preview URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce GitHub Gist identifiers and gists.page preview links when publishing succeeds.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
