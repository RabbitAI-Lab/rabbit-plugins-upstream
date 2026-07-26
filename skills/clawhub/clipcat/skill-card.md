## Description: <br>
Clipcat helps agents use the Clipcat CLI for TikTok commerce research, product insights, viral video replication, product-to-video generation, video breakdown analysis, image generation, and video downloads. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[a2888409](https://clawhub.ai/user/a2888409) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, commerce operators, and developers use this skill to drive Clipcat CLI workflows for TikTok Shop market research, AI image and video generation, viral-video replication, media analysis, downloads, and async task tracking. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill downloads and runs a third-party Clipcat CLI binary and uses Clipcat's hosted service. <br>
Mitigation: Install only if you trust Clipcat's binary and service; use the versioned download URLs recorded in the release metadata. <br>
Risk: Video generation and social-video replication can consume paid credits. <br>
Mitigation: Run clipcat quote with the same parameters, show the returned totalCredits to the user, get explicit approval, and submit with --expected-credits. <br>
Risk: API keys, private media, and signed URLs may be passed through Clipcat workflows. <br>
Mitigation: Configure only your own CLIPCAT_API_KEY and avoid private media or signed URLs unless you are comfortable sending them through Clipcat workflows. <br>


## Reference(s): <br>
- [Clipcat homepage](https://clipcat.ai) <br>
- [Clipcat API key settings](https://clipcat.ai/workspace?modal=settings&tab=apikeys) <br>
- [ClawHub skill page](https://clawhub.ai/a2888409/skills/clipcat) <br>
- [Publisher profile](https://clawhub.ai/user/a2888409) <br>
- [Clipcat CLI macOS Apple Silicon download](https://static.clipcat.ai/public/cli/v1.0.24/clipcat_darwin_arm64.tar.gz) <br>
- [Clipcat CLI macOS Intel download](https://static.clipcat.ai/public/cli/v1.0.24/clipcat_darwin_amd64.tar.gz) <br>
- [Clipcat CLI Linux x86_64 download](https://static.clipcat.ai/public/cli/v1.0.24/clipcat_linux_amd64.tar.gz) <br>
- [Clipcat CLI Linux arm64 download](https://static.clipcat.ai/public/cli/v1.0.24/clipcat_linux_arm64.tar.gz) <br>
- [Clipcat CLI Windows x86_64 download](https://static.clipcat.ai/public/cli/v1.0.24/clipcat_windows_amd64.zip) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented CLI output expectations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill requires CLIPCAT_API_KEY and asks agents to quote and confirm credit-consuming video commands before submission.] <br>

## Skill Version(s): <br>
1.0.24 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
