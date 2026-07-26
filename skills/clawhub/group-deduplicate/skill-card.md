## Description: <br>
Provides command-line tools intended to search for WeChat, QQ, and industry groups, filter duplicate group names with memory-cache-backed MD5 keys, and cache discovered groups for 30 days. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiiang0529](https://clawhub.ai/user/xiiang0529) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and community operators use this skill to run group discovery and deduplication workflows, then inspect or manage cached group records. Because the security evidence says the included search implementation returns fabricated deterministic results, users should treat group discovery output as unverified until the publisher replaces it with a real search provider. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search results may be fabricated deterministic entries rather than real group discoveries. <br>
Mitigation: Review or replace the search implementation before relying on discovered groups, and treat returned group links as unverified. <br>
Risk: Cache operations depend on a memory-cache helper path under WORKSPACE, which can affect behavior if the helper is missing, unexpected, or untrusted. <br>
Mitigation: Install the expected memory-cache skill from a trusted source, validate WORKSPACE, and confirm Redis configuration before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xiiang0529/skills/group-deduplicate) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text command-line output with group entries, cache status, cache statistics, and warnings.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search and cache commands may write group-name records to memory-cache with a default 30-day TTL.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
