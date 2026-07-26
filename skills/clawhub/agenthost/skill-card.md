## Description: <br>
Publishes a static site or a folder of Markdown docs to a hosted URL and returns a private, pre-authenticated share link. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ceifa](https://clawhub.ai/user/ceifa) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use Agenthost to publish static sites, HTML files, or Markdown documentation to a hosted URL and share the generated private link with a human reviewer or collaborator. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Publishing selected files to agenthost.page can expose private, proprietary, or secret content through the hosted site or generated private share link. <br>
Mitigation: Confirm the intended files before upload, avoid publishing secrets or sensitive material unless external hosting is acceptable, and keep generated share links out of public chats, logs, screenshots, and issue trackers. <br>
Risk: Losing the one-time ownerToken prevents redeploying or managing the same URL. <br>
Mitigation: Store the ownerToken securely when it is first returned, and treat it as an account credential for future redeploys or owner endpoints. <br>


## Reference(s): <br>
- [Agenthost homepage](https://agenthost.page) <br>
- [agenthost HTTP API](references/http-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include curl and tar commands, publish options, and guidance for handling shareUrl and ownerToken values.] <br>

## Skill Version(s): <br>
0.1.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
