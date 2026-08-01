## Description: <br>
Upload images to img402.dev for embedding in GitHub PRs, issues, and comments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[img402](https://clawhub.ai/user/img402) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to upload screenshots, mockups, diagrams, or other images to img402.dev and embed the returned public URL in GitHub pull requests, issues, comments, and Markdown. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents may upload screenshots or images containing credentials, internal systems, customer data, or other private information to a public third-party host. <br>
Mitigation: Review each image before upload, remove sensitive content, and confirm that public access is acceptable before embedding the returned URL. <br>
Risk: Small uploads are described as permanent, and uploaded images are reachable by anyone with the URL. <br>
Mitigation: Use this skill only for content intended to be public or externally shareable, and request removal through the service contact when needed. <br>
Risk: Images larger than 1 MB may expire after 30 days unless uploaded through the paid permanent flow. <br>
Mitigation: Check the returned expiresAt value and either shrink the image below 1 MB or use the paid token workflow for images that must remain available. <br>


## Reference(s): <br>
- [img402.dev](https://img402.dev) <br>
- [Coinbase Payments MCP Tool](https://docs.cdp.coinbase.com/mcp) <br>
- [Paying x402 APIs](https://img402.dev/blog/paying-x402-apis) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Markdown, API Calls, Guidance] <br>
**Output Format:** [Markdown with inline bash commands, HTTP API examples, and GitHub image embed snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces public image URLs and GitHub Markdown; uploaded image retention depends on file size and paid-token use.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
