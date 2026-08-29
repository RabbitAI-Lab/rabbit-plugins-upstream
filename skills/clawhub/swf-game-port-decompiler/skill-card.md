## Description:

Decompile SWF games for engine ports using FFDec/JPEXS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stanestane](https://clawhub.ai/user/stanestane)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to decompile authorized SWF games into a porting workspace with extracted code, assets, timeline renders, tag data, XML structure, and an audit for rebuilding behavior in a modern engine.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill decompiles SWF files and can process content the user may not have rights to analyze or port.

Mitigation: Use it only on SWF files the user owns or is authorized to preserve, research, migrate, or port.

Risk: Untrusted SWF files may be risky inputs to external tooling.

Mitigation: Prefer FFDec extraction over running the SWF in Flash Player, and isolate any execution that is explicitly required.

Risk: The extraction process can create large output folders and many generated files.

Mitigation: Use a dedicated output folder, never overwrite the original SWF, and review generated files before relying on them.

Risk: Decompiled ActionScript can be incomplete, obfuscated, or misleading.

Mitigation: Treat decompiled code as behavioral reference and cross-check against P-code, tag structure, XML timelines, and rendered frames or sprites.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/stanestane/skills/swf-game-port-decompiler)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and generated workspace files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce extracted ActionScript, P-code, images, shapes, audio, fonts, text, binary data, timeline renders, SWF tag dumps, XML structure, manifests, and PORTING_AUDIT.md.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
