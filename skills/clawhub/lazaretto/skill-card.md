## Description: <br>
Verify a third-party skill, tool, or npm/GitHub package for malicious behavior before installing or running it, using known-bad hash lookup, Lazaretto API scans, and post-install hash verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jamesdfinance-dev](https://clawhub.ai/user/jamesdfinance-dev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and security-conscious users use Lazaretto before installing untrusted skills, MCP servers, npm packages, GitHub repositories, raw URLs, or ClawHub skills. It helps check known-bad hashes, request a Lazaretto scan, and verify that installed files match the scanned target hash. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using scan can send selected scan targets or inline file contents to a third-party Lazaretto service. <br>
Mitigation: Submit only artifacts you intend to share, use the default API or a trusted --api endpoint, and keep LAZARETTO_KEY scoped to this service. <br>
Risk: A clear scan result is a signal, not a warranty that an artifact is safe. <br>
Mitigation: Review the returned evidence, avoid scanning private secrets as inline files unless intentional, and use verify after installation to confirm on-disk bytes match the scanned target_hash. <br>


## Reference(s): <br>
- [Lazaretto homepage](https://lazaretto.dev) <br>
- [Lazaretto pricing](https://lazaretto.dev/#pricing) <br>
- [ClawHub Lazaretto skill page](https://clawhub.ai/jamesdfinance-dev/skills/lazaretto) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node and may use LAZARETTO_KEY for keyed scans.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter reports 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
