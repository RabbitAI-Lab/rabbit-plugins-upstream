## Description:

Build or refactor a GameLearningRuntime adapter, runtime bridge, trainable environment, knowledge research manifest, or reward configuration. Use when an agent must turn an authorized game runtime into a reusable GLR environment for RL, BC, IMPALA, evaluation, or offline collection while preserving privacy, provenance, action fencing, and learner-neutral contracts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to scaffold or refactor GLR adapters for authorized game runtimes, including synthetic training baselines, runtime bridges, knowledge manifests, reward safety configuration, and reproduction checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated setup commands and dependency manifests carry normal software supply-chain exposure.

Mitigation: Run generated setup in an isolated development environment without sensitive credentials and review dependency locks after creation.

Risk: Loader-plugin outputs could be misapplied to a game runtime without authorization or an approved mod policy.

Mitigation: Use loader outputs only with runtimes you own or are explicitly authorized to test, and confirm the target and mod policy before use.

## Reference(s):

- [Multi-engine development boundaries](references/multi-engine.md)
- [Authorized loader-plugin integrations](references/loader-plugins.md)
- [Gameplay research and reward design](references/research-and-reward.md)
- [Runtime Host and provider SDK boundary](references/runtime-host.md)
- [Adapter validation gates](references/validation-gates.md)
- [BepInEx](https://github.com/BepInEx/BepInEx)
- [UE4SS](https://github.com/UE4SS-RE/RE-UE4SS)
- [BepInEx plugin tutorial](https://docs.bepinex.dev/master/articles/dev_guide/plugin_tutorial/index.html)
- [UE4SS Lua mod guide](https://docs.ue4ss.com/dev/guides/creating-a-lua-mod.html)
- [UE4SS ExecuteInGameThread](https://docs.ue4ss.com/dev/lua-api/global-functions/executeingamethread.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command examples plus generated project files and JSON configuration.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated adapter lanes are synthetic-first and include validation artifacts; dependency setup and loader outputs require review before use.]

## Skill Version(s):

0.19.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
