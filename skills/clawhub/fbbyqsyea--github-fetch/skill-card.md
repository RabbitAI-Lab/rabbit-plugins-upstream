## Description: <br>
GitHub Fetch helps agents download GitHub repositories, release assets, and files with direct-download checks, proxy fallback, resumable transfers, checksum verification, and optional extraction or installation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fbbyqsyea](https://clawhub.ai/user/fbbyqsyea) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill when a workflow needs to fetch GitHub-hosted source, single files, or release assets despite slow, blocked, or unreliable direct GitHub access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can route downloads through third-party GitHub proxy mirrors. <br>
Mitigation: Use only trusted entries in GITHUB_PROXIES, prefer direct GitHub downloads when viable, and verify downloaded artifacts before use. <br>
Risk: The skill can extract and install downloaded artifacts, including into system-level locations. <br>
Mitigation: Prefer user-owned output directories, require pinned SHA-256 checksums before extracting or installing binaries, and avoid sudo or /usr/local/bin symlinks unless explicitly requested. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fbbyqsyea/skills/github-fetch) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Code, Files, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and local file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce downloaded files, cloned repositories, extracted archives, checksum results, and installation instructions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
