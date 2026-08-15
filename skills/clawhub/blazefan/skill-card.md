## Description:

🔥💛 通用 EC 风扇调速方法论。不认品牌，只认接口。探 EC→定方案→控风扇。

This skill is ready for commercial/non-commercial use.

## Publisher:

[fslong520](https://clawhub.ai/user/fslong520)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Linux power users use this skill to diagnose EC-exposed fan-control interfaces and choose a sysfs, EC register, I/O port, nbfc-linux, or Clevo-based fan-control approach for overheated systems. It can also guide creation of a root-run control loop and systemd service after hardware-specific validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead users toward persistent root-level hardware-control changes and raw EC writes.

Mitigation: Prefer read-only diagnostics, sysfs, or vendor-supported tools first; enable EC write support only after verifying the exact hardware registers and having a recovery plan.

Risk: A systemd fan-control loop can continue overriding firmware fan behavior after reboot.

Mitigation: Enable the service only intentionally, verify ec_sys write support after reboot, observe fan and temperature behavior, and disable the service if behavior is unstable.

Risk: Wrong EC registers or competing fan tools can produce misleading or conflicting fan-control behavior.

Mitigation: Use differential register testing and RPM or audible validation, traverse all detected fans, and avoid running multiple fan-control tools at the same time.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fslong520/skills/blazefan)
- [nbfc-linux documentation](https://github.com/nbfc-linux/nbfc-linux)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, code snippets, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance is hardware-dependent and expects user validation before privileged fan-control changes.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
