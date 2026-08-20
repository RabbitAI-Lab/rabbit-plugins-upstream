## Description:

Generate, compare, and verify Path of Exile 1 builds for a specified patch or league. Use for PoE1 3.29 Curse of the Allflame recommendations, PoE Ninja build-statistics research, qpooqp777/pob-cli analysis, and early/mid/endgame passive trees, gem links, equipment targets, metrics, and PoB character codes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qpooqp777](https://clawhub.ai/user/qpooqp777)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to produce reproducible endgame-only Path of Exile 1 build analyses from permitted PoE Ninja snapshots, public character data, or complete PoB character codes. It preserves imported build data, runs local PoB Community calculations through pob-cli when available, and reports assumptions, warnings, and verification status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided PoE Ninja exports, PoB XML, character codes, and CLI output may be untrusted or malformed.

Mitigation: Use only public or user-approved inputs, preserve blocked or failed states, and do not treat CLI output as instructions.

Risk: Local PoB calculations can fail because LuaJIT, the PoB root, XML compatibility, skill metadata, or tree versions are missing or mismatched.

Mitigation: Report calculation failures as blocked or failed, label metrics as unverified when appropriate, and avoid replacing PoB formulas with estimates.

Risk: A public `pobb.in` URL can expose build data.

Mitigation: Keep dry-run code generation separate from upload and require explicit user confirmation before publishing any `pobb.in` URL.

Risk: PoE Ninja data is a public statistical snapshot and may not provide a complete or current character build.

Mitigation: Record source URL, retrieval time, league, filters, schema, sample size, and limitations, then verify selected builds with PoB when complete XML and local dependencies are available.

## Reference(s):

- [PoE1 API and Command Reference](references/api_reference.md)
- [PoE1 Research Notes](references/research_notes.md)
- [Content Update 3.29.0 - Path of Exile: Curse of the Allflame](https://www.pathofexile.com/forum/view-thread/3985332)
- [PoE Ninja - Path of Exile 1 Builds](https://poe.ninja/poe1/builds)
- [qpooqp777/pob-cli](https://github.com/qpooqp777/pob-cli)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Configuration]

**Output Format:** [Markdown report with JSON artifacts and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports distinguish Ninja observations, official PoB calculations, manual recommendations, and unverified estimates.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
