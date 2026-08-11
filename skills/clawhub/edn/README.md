# edn

[![skills.sh](https://skills.sh/b/skcache/edn)](https://skills.sh/skcache/edn)

**Engineering Dashboard Notebook**

AI coding agents can write most of the code now.

The problem is when they also start owning the architecture and you slowly stop knowing why your own system works the way it does.

`edn` keeps a local engineering notebook in sync with your repo so you can actually stay on top of:

- architecture
- components
- dependencies
- data flow
- tradeoffs
- failure modes
- security boundaries
- current vs proposed changes

The notebook lives locally as:

```text
engineering-notebook.html
```

and gets added to `.gitignore` automatically.

## How it works

For normal work, the agent just builds.

If something meaningfully changes the architecture, it shows you the current setup, the proposed change, tradeoffs, evidence, and simpler alternatives before implementing it.

You make the call.

After the task is done, `edn` updates the notebook to match the actual code.

## Learn while you build

On first use, `edn` picks an explanation level: it reuses one already stored in the notebook, asks when an interactive user is around, and otherwise defaults to **Junior** without blocking work.

```text
Intern
New Grad
Junior
Mid-Level
Senior
Staff
Principal
Distinguished
```

Same engineering rigor, just different levels of context.

So if the agent wants to throw Redis into your app, it should explain why it helps **your system**, what extra complexity it adds, and whether you've even measured a bottleneck yet.

## Install

```bash
npx skills add skcache/edn
```

For Codex:

```bash
npx skills add skcache/edn -a codex
```

For Claude Code:

```bash
npx skills add skcache/edn -a claude-code
```

The `skills` CLI supports a bunch of coding agents and installs skills directly from GitHub.

## Update

To update an existing install:

```bash
npx skills update edn
```

`metadata.version` in `SKILL.md` is for human release tracking; the CLI finds updates from the source repo, not this field.

## Use

Inside your repo:

```text
Use the edn skill.
Bootstrap the engineering notebook for this repository.
```

That's it.

The agent can own the typing.

You should still own the system.

## License

MIT
