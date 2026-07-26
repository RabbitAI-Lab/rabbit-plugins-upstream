## Description: <br>
Universal LYGO Living Memory Library v1.2 provides a capped living-memory index, local audit and compression helpers, FRAGILE tagging, and LYGO-MINT provenance support for LYGO and LYRA continuity work. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators maintaining a LYGO or LYRA workspace use this skill to keep a capped living-memory index, audit drift and FRAGILE entries, and optionally produce a metadata-focused Master Archive before user-approved minting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A misconfigured LYGO_AUTHORITY_ROOT could cause the audit or archive helper to inspect the wrong local workspace. <br>
Mitigation: Set LYGO_AUTHORITY_ROOT only to the intended LYGO workspace before running audit or compression commands. <br>
Risk: MASTER_ARCHIVE.md, hashes, and paths can reveal private project structure, especially for FRAGILE entries. <br>
Mitigation: Review MASTER_ARCHIVE.md and all FRAGILE entries before minting or public anchoring. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/deepseekoracle/skills/lygo-universal-living-memory-library) <br>
- [Publisher Profile](https://clawhub.ai/user/deepseekoracle) <br>
- [GitHub URL from Skill Metadata](https://github.com/DeepSeekOracle/lygo-protocol-stack) <br>
- [Library Spec](references/library_spec.md) <br>
- [Agent Contract](references/AGENT_CONTRACT.md) <br>
- [Security](references/SECURITY.md) <br>
- [Core Files Index](references/core_files_index.json) <br>
- [Audit Protocol](references/audit_protocol.md) <br>
- [Compression Protocol](references/compression_protocol.md) <br>
- [Canon](references/canon.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and text guidance with shell commands, JSON audit reports, and metadata-only archive output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local workspace paths and hashes may be reported; file contents are not meant to be exfiltrated in bulk.] <br>

## Skill Version(s): <br>
1.2.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
