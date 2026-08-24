# Project Engineering

> **Make your coding agent understand the repository before it changes the code.**
>
> *Understand the repo. Change with evidence. Deliver with proof.*

[简体中文](README.md) · [Usage guide](docs/USAGE.md) · [Changelog](CHANGELOG.md)

Most coding agents can generate code. The hard part is knowing **what should change, where it belongs, which constraints apply, and what evidence is enough**.

Project Engineering is a reusable Agent Skill for existing software repositories. It grounds decisions in repository rules, real code, build configuration, migrations, tests, and current workspace state—then guides the agent through architecture mapping, risk assessment, the smallest coherent implementation, layered validation, and a traceable handoff.

It is not a longer “do everything” prompt. It is an engineering method for reducing guesswork, scope creep, and unsupported claims in real codebases.

## What it changes

- **Evidence before assumptions** — traces real entry points, call paths, state, data, and side effects instead of guessing from names.
- **Architecture-aware decisions** — respects existing ownership and dependency direction without forcing DDD, microservices, or patterns.
- **Risk-calibrated depth** — separates operational authorization from the consequence of the target change.
- **The smallest coherent change** — reuses existing boundaries and avoids unrelated refactors or invented capabilities.
- **Layered proof** — distinguishes code completion, automated checks, integration validation, and real-environment acceptance.
- **Workspace safety** — preserves unrelated user changes and keeps credentials or local configuration out of delivery.
- **Cross-stack discovery** — recognizes common Java, Node.js, Python, Go, Rust, and .NET repository signals.

## Quick start

```text
Use $project-engineering.

Task: Implement order export.
Mode: Implementation.
Requirements:
1. Read repository rules and trace the existing call path first.
2. Preserve unrelated workspace changes.
3. Follow the repository's established architecture and conventions.
4. Run proportionate tests and report the evidence.
5. Do not commit or push.
```

## Install

For Codex and other Agent Skills clients:

```bash
git clone https://github.com/liubai00/project-engineering.git ~/.agents/skills/project-engineering
```

For OpenClaw through ClawHub:

```bash
openclaw skills install @liubai00/project-engineering
```

## Safety boundary

Invoking this Skill selects an engineering workflow. It does **not** authorize commits, pushes, pull requests, migrations, deployments, credential changes, production access, or device operations.

The bundled inventory script requires Python 3.10+ and uses only the standard library. It detects engineering signals without executing repository code, package-manager scripts, or builds, and it never prints secret values. Its report includes the repository root, branch, commit, and structural paths, so review the output before sharing it publicly.

## License

[MIT-0](LICENSE). Free to use, modify, redistribute, and use commercially without attribution.
