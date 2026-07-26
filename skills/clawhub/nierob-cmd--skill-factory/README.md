# skill-factory

A meta-skill for OpenClaw / Claude Code agents: it builds a **family of
skills** — one router skill plus 2-6 variant skills — for a problem that has
several recognizable variants, instead of one overloaded, branchy skill.

## What it produces

```
your-topic-router          → recognizes the variant, routes to the right one
your-topic-variant-1
your-topic-variant-2
...
your-topic-variant-N        (2-6 total)
```

Each variant skill is self-contained (it can be invoked directly, without
going through the router) and ends with a self-check checklist.

## When to use it

All three must be true:

1. A bounded set of variants (2-6).
2. The variants are distinguishable from the input up front (file type,
   keywords, explicit context).
3. The logic differs enough per variant that a single shared prompt would be
   confusing.

If you just need one plain skill with no variants, use a regular
skill-creation flow instead — this is specifically for the "router + N
variants" shape.

## Install

```bash
openclaw skills install <owner>/skill-factory
```

Or point your agent at ClawHub directly and ask for it — most OpenClaw
setups can discover it via `openclaw skills search "skill factory"`.

## Use it

Just describe the problem to your agent, in the shape of "I need a skill
that handles N different variants of X." The skill walks through:

0. Gathering the domain, the variant list, the recognition rule, and the
   expected output format (max 3-5 questions).
1. Designing the router + variants architecture.
2. Showing you the plan before creating anything (unless you said "just do
   it").
3. Creating the actual skill files.
4. Summarizing what was built.
5. (Optional) Building an eval set and tuning the descriptions for reliable
   triggering, then packaging.

See `SKILL.md` for the full step-by-step, and
`references/skill-mechanics.md` for the design rationale behind every rule
(progressive disclosure, eval-set-driven description tuning, the "Lack of
Surprise" security property, and more).

## License

MIT-0 (ClawHub's required license for published skills) — use it, fork it,
adapt it, no attribution required.
