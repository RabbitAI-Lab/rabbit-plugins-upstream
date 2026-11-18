## Description:

Run EvoMap V2 evolution cycles — convert sessions to transcripts, ingest material, distill genes, run cycles, and manage the autoexec daemon. Use when running or debugging EvoMap evolution (evolver >= 2.0.23).

This skill is ready for commercial/non-commercial use.

## Publisher:

[147258xuan](https://clawhub.ai/user/147258xuan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using OpenClaw and EvoMap can convert session logs into transcripts, ingest and distill material, run evolution cycles, and manage the autoexec daemon.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Session transcripts can contain private prompts, assistant responses, and tool output, and may be sent to an external runner during a cycle.

Mitigation: Review and redact session material before ingestion or use with an external runner; use only material approved for that processing.

Risk: The security review flags shell handling and notes that several scripts were only partially inspected.

Mitigation: Avoid transcript filenames controlled by untrusted parties, and review the scripts before installation or execution.

## Reference(s):

- [Evolver on ClawHub](https://clawhub.ai/147258xuan/skills/evolver)

## Skill Output:

**Output Type(s):** [Files, Code, Shell commands, Guidance]

**Output Format:** [Markdown instructions and JavaScript scripts; JSONL transcripts and command-line output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transcript and cycle outputs depend on selected session material and the installed evolver CLI; full cycles require a configured runner.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
