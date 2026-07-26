## Description: <br>
List recently uploaded images on PixelVault with their CDN URLs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[facundofarias](https://clawhub.ai/user/facundofarias) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
PixelVault users use this skill to list recent uploads, find hosted image URLs, and optionally request JSON metadata or paginated results from the configured PixelVault CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Detailed JSON output may reveal upload metadata such as filenames, MIME types, sizes, folders, and timestamps in the conversation. <br>
Mitigation: Use default URL-only output unless metadata is needed, and confirm before using --json or broad pagination. <br>
Risk: Results expose PixelVault CDN URLs for hosted images. <br>
Mitigation: Share only the URLs the user requested and avoid reposting sensitive image links unnecessarily. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/facundofarias/skills/pixelvault-list) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Plain text URLs by default; JSON metadata when --json is requested; concise Markdown prose when reporting results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports optional pagination flags such as --page and --per-page; requires the PixelVault CLI to be installed and configured.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
