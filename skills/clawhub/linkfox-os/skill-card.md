## Description: <br>
Linkfox OS routes cross-border e-commerce prompts to specialized LinkFox agents for product research, market analysis, listing optimization, media generation, IP checks, file upload, and onboarding workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, e-commerce operators, and developers use this skill to submit one-shot LinkFox automation tasks for marketplace research, product selection, Amazon listing work, image or video generation, IP checks, file uploads, and account or billing onboarding. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles SMS login, API keys, payment orders, file uploads, local logs, and public share links. <br>
Mitigation: Use it only in trusted workspaces, prefer creating the LinkFox account and API key in the official web UI, and treat generated share links and local .linkfox-os outputs as sensitive. <br>
Risk: The skill can send prompts, API keys, and uploaded user materials to LinkFox or S3-backed services. <br>
Mitigation: Verify LINKFOX_* base URL environment variables point to expected LinkFox domains and avoid uploading confidential files unless the user intends to send them to those services. <br>


## Reference(s): <br>
- [LinkFox OS homepage](https://os.linkfox.com/) <br>
- [Linkfox OS ClawHub listing](https://clawhub.ai/linkfox-ai/skills/linkfox-os) <br>
- [Agent capabilities reference](references/capabilities.md) <br>
- [API reference](references/api.md) <br>
- [Onboarding guide](references/onboarding.md) <br>
- [Onboarding API contract](references/onboarding-api.md) <br>
- [Amazon ecosystem skills](references/skills-amazon.md) <br>
- [IP and compliance detection skills](references/skills-ip-compliance.md) <br>
- [Listing skills](references/skills-listing.md) <br>
- [Market analysis skills](references/skills-market-analysis.md) <br>
- [Media generation skills](references/skills-media.md) <br>
- [Product selection skills](references/skills-selection.md) <br>
- [Third-platform e-commerce skills](references/skills-third-platforms.md) <br>
- [General tool skills](references/skills-tools.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, code, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown and JSON with inline shell commands and local or remote file references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Tasks are submitted to an asynchronous LinkFox API, require LINKFOXAGENT_API_KEY, and may create local .linkfox-os outputs or share links.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
