# Capability and host boundaries

- `builtin-js`: dependency-free local CPU backend.
- `hf-peft`: local Python subprocess using an already-present model; measured CPU
  training, reload, generation, independent evaluation, gated export, CLI cancel
  and job-step resume. Resource bounds are not filesystem/network isolation.
- CPU fixture evidence does not validate real pretrained-model quality, CUDA,
  large-model memory requirements, enterprise data handling, or production use.
- Reduced precision and multi-GPU/distributed operation are not supported by the
  delivered backend. Do not infer them from upstream PyTorch/PEFT capabilities.
- CLI recovery is job-step granular, not guaranteed exact training-step resume.
  Cancellation is cooperative at orchestration level; bounded-latency forced
  abort and rollback of arbitrary backend steps are not guaranteed.
- Tailnet gives connectivity, not a verified remote scheduler or pooled VRAM.
  Remote execution needs an authorized host, isolated installation, resource
  agreement, explicit data-transfer scope, and durable state on that host.
- Colossal-AI is not an implemented Foundry backend.

## Agent portability

This skill is plain Markdown with YAML frontmatter; it does not depend on a
particular agent runtime or hard-coded tool name. Codex and other shell-capable
agents can execute the CLI. OpenClaw and Hermes can use the same CLI, or discover
their installed Foundry integration and inspect its actual schema before calling
it. Do not assume reading the skill installs/registers a host plugin. Follow the
repository's `docs/integration.md` for host-specific installation.

Copy the entire `taskforce-model-foundry/` skill directory, including references,
to the target agent's documented skill location. Discover that location from the
host configuration; do not assume all agents share a workspace or filesystem.
