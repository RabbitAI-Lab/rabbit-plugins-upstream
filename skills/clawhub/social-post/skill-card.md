## Description: <br>
Post and reply to X/Twitter and Farcaster with text and images, including multi-account support, draft preview, character validation, threads, replies, image uploads, and optional text variation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[callmedas69](https://clawhub.ai/user/callmedas69) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, creators, and social media operators use this skill to prepare, preview, publish, and reply to posts on X/Twitter and Farcaster from an agent workflow. It is suited to multi-account announcements, image posts, threads, link shortening, and dry-run review before publishing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can publish public posts and replies to X/Twitter and Farcaster. <br>
Mitigation: Use dry-run previews and explicit confirmation for human review before posting; avoid unattended automation unless separate approval controls are added. <br>
Risk: The skill uses account tokens, private keys, and a Farcaster custody wallet that may spend funds. <br>
Mitigation: Use only dedicated accounts and wallets, isolate credentials, limit wallet funding, and keep API tokens and private keys out of shared environments. <br>
Risk: The text variation option is designed to bypass duplicate-content controls. <br>
Mitigation: Disable the variation option unless the user has confirmed the content complies with platform rules and account policies. <br>
Risk: Images and links may be uploaded to or shortened through third-party services. <br>
Mitigation: Avoid sensitive media or private links, and review generated public URLs before publishing. <br>
Risk: The scripts rely on unmanaged local dependencies and workspace-specific helper paths. <br>
Mitigation: Review local dependencies and script paths before installation, and run in a constrained environment with only the required tools and credentials. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/callmedas69/skills/social-post) <br>
- [Publisher Profile](https://clawhub.ai/user/callmedas69) <br>
- [X Developer Portal](https://developer.twitter.com/en/portal/dashboard) <br>
- [X API Pricing](https://developer.twitter.com/#pricing) <br>
- [Neynar Hub API](https://hub-api.neynar.com) <br>
- [Farcaster Developer Docs](https://docs.farcaster.xyz) <br>
- [OpenClaw](https://openclaw.ai) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce public posts, replies, thread URLs, dry-run previews, validation messages, and wallet balance output when the user runs the bundled scripts.] <br>

## Skill Version(s): <br>
1.4.0 (source: server release, frontmatter, changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
