## Description: <br>
Safe single-owner staged memory consolidation with autonomous bounded index compaction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lzyling](https://clawhub.ai/user/lzyling) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to consolidate OpenClaw daily memory logs into bounded topic files and a compact MEMORY.md index while enforcing single-writer, preflight, backup, and candidate-transaction safeguards. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Concurrent memory writers or enabled built-in Dreaming can create ambiguous ownership of MEMORY.md and topic files. <br>
Mitigation: Run the documented preflight first, require built-in Dreaming to be disabled before writes, and allow only one enabled scheduled signal-dreaming writer. <br>
Risk: Schema drift, unsupported OpenClaw versions, unsafe paths, or malformed evidence can make an automated memory write unsafe. <br>
Mitigation: Use the fixed read-only CLI evidence commands, keep evidence local, and stop on any missing field, parse failure, unsupported version, unsafe path, or ownership ambiguity. <br>
Risk: A failed or partial live commit can leave memory state uncertain. <br>
Mitigation: Use candidate transactions, inspect backups and manifests for incomplete runs, and acknowledge incomplete runs only after review of the exact run ID. <br>


## Reference(s): <br>
- [Signal Dreaming Skill Page](https://clawhub.ai/lzyling/skills/signal-dreaming) <br>
- [Signal Dreaming V3 Protocol](references/dream-protocol.md) <br>
- [Native capability contract](references/native-capability-contract.md) <br>
- [v1.3.1 to v2 migration](references/migration-v1-to-v2.md) <br>
- [dream-audit.sh](references/dream-audit.sh) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and local file edits] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces bounded local memory consolidation plans and candidate file updates; no hidden network, credential, or automatic system-modification behavior was reported by security evidence.] <br>

## Skill Version(s): <br>
3.0.0-rc.3 (source: server release evidence and SKILL.md release candidate note) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
