## Description:

Builds or refactors a GameLearningRuntime adapter, runtime bridge, trainable environment, knowledge research manifest, or reward configuration for authorized game runtimes while preserving privacy, provenance, action fencing, and learner-neutral contracts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to scaffold or refactor GLR adapter projects for authorized Unity, Unreal, Godot, external, or loader-based runtimes. It helps agents produce adapter code, project manifests, research and reward configuration, validation guidance, and bounded setup commands for reinforcement learning, behavioral cloning, evaluation, or offline collection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated setup commands and dependency manifests can carry normal supply-chain risk.

Mitigation: Run generated commands in an isolated development environment, review dependencies and lockfiles, and pin versions before serious use.

Risk: Loader or live-runtime lanes can interact with game runtimes beyond the synthetic scaffold boundary.

Mitigation: Use only games and systems the operator is explicitly authorized to instrument, require exact target binding, and treat live acceptance as a separate bounded trace.

Risk: Gameplay research or guide-derived claims can be stale, inaccurate, or advisory only.

Mitigation: Record provenance, access time, confidence, and volatility, then require runtime verification before claims affect actions or authoritative reward terms.

Risk: Generated adapter artifacts may expose local paths, identifiers, observations, actions, screenshots, or proprietary data if published without review.

Mitigation: Publish only aggregate synthetic conformance evidence unless a reviewed authorized trace exists, and exclude local paths, credentials, account identifiers, process or window handles, and private traces.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/loonghao/skills/glr-adapter-builder)
- [GLR adapter builder skill](SKILL.md)
- [Multi-engine development boundaries](references/multi-engine.md)
- [Authorized loader-plugin integrations](references/loader-plugins.md)
- [Gameplay research and reward design](references/research-and-reward.md)
- [Runtime Host and provider SDK boundary](references/runtime-host.md)
- [Adapter validation gates](references/validation-gates.md)
- [BepInEx upstream repository](https://github.com/BepInEx/BepInEx)
- [UE4SS upstream repository](https://github.com/UE4SS-RE/RE-UE4SS)
- [BepInEx plugin tutorial](https://docs.bepinex.dev/master/articles/dev_guide/plugin_tutorial/index.html)
- [UE4SS Lua mod guide](https://docs.ue4ss.com/dev/guides/creating-a-lua-mod.html)
- [UE4SS ExecuteInGameThread documentation](https://docs.ue4ss.com/dev/lua-api/global-functions/executeingamethread.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands plus generated project files and JSON/TOML configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates scaffolded adapter projects, validation scripts, runtime packaging instructions, research manifests, reward-safety policies, demonstration policies, and training configuration; generated setup commands should be reviewed before execution.]

## Skill Version(s):

0.15.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
