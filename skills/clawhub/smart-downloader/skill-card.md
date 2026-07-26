## Description: <br>
Smart file downloader with multi-threading, resumable downloads, and progress display. <br>

This skill is for research and development only. <br>

## Publisher: <br>
[dkgee](https://clawhub.ai/user/dkgee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical users use this skill to download multiple or large files from user-provided URL lists with resumable transfers, progress reporting, retries, custom headers, and proxy support. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can download arbitrary URLs and save files to a user-selected folder. <br>
Mitigation: Use trusted URL lists and review downloaded files before opening or executing them. <br>
Risk: Custom request headers may include sensitive values. <br>
Mitigation: Avoid passing sensitive headers unless required and keep command history, logs, and shared URL lists free of credentials. <br>
Risk: High concurrency or large URL lists can burden target services or violate site rules. <br>
Mitigation: Keep concurrency reasonable and follow each target platform's terms of service, robots.txt rules, and rate expectations. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/dkgee/skills/smart-downloader) <br>
- [Sample URL list](references/sample_urls.txt) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and filesystem outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Downloads user-provided URLs to an output directory and uses output_dir/.temp for temporary files during transfer.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
